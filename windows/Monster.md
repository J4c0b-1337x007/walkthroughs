# 🏴 Monster (Windows)

## 🧠 Initial Foothold

- Guessed the credentials `admin:wazowski` based on clues from the main page and directory enumeration with `feroxbuster`.

- Used these credentials to log in and obtained remote code execution by exploiting a known vulnerability:  
  [monstra-cms/monstra#470](https://github.com/monstra-cms/monstra/issues/470)

---

## 🚀 Privilege Escalation

- Ran `winPEASany.exe` and noticed XAMPP was installed.

- Identified the XAMPP version in the `xampp-control.ini` file.

- Searched for privilege escalation exploits and found:  
  [EDB-ID 50337](https://www.exploit-db.com/exploits/50337)

- Created a reverse shell payload with `msfvenom`, replaced the vulnerable service binary.

- Triggered a system reboot with:
  ```cmd
  shutdown /r
  ```

- Successfully received a SYSTEM-level reverse shell.

---

🧼 **Post-Exploitation Note:**  
Revert modified service binaries and remove payloads when complete.

> ⚠️ This walkthrough is for educational purposes only.
