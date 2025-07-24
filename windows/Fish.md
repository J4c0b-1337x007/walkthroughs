# 🏴 Fish (Windows)

## 🧠 Initial Foothold

- Discovered an exploit for Oracle GlassFish Server 4.1:  
  Directory Traversal - Multiple webapps Exploit.

- Initially assumed credentials would grant access to the GlassFish HTTP login page, but soon realized the actual credentials were for the synaman application used for RDP access on port 6060.

- This was confusing due to the presence of two distinct login pages.

- Used the directory traversal vulnerability to read configuration files containing credentials, including:  
  - `admin-keyfile`  
  - `local-password`  
  - `AppConfig.xml` for the synaman app

- Extracted valid credentials from these files to proceed.

---

## 🚀 Privilege Escalation

- Ran `winpeasny.exe` to gather system information and identify privilege escalation paths.

- Noticed TotalAV antivirus software running a service named `SecurityService.exe`.

- Exploited this by renaming the original service executable and replacing it with a custom reverse shell payload.

- Restarted the system with `shutdown /r` to trigger the modified service.

- Gained a SYSTEM shell after reboot.

- Encountered confusion because many publicly available exploits for this service were outdated and didn’t work as expected.

---

🧼 **Post-Exploitation Note:**  
Be cautious when dealing with outdated exploits, always verify and test thoroughly.

> ⚠️ This walkthrough is for educational purposes only.
