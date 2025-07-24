# 🏴 Shenzi (Windows)

## 🧠 Initial Foothold

- Tried multiple wordlists with Gobuster but couldn't find the key URL.

- Eventually, after discovering `/dashboard/phpinfo.php/` and seeing file paths with the user `shenzi`, manually guessed and accessed:
  ```
  http://$IP/shenzi
  ```

- Logged in to the WordPress admin panel at:
  ```
  http://$IP/shenzi/wp-admin/
  ```
  Using credentials obtained via `smbclient`.

- Instead of uploading a plugin, navigated to:  
  “Appearance” → “Theme Editor” and edited the `404.php` file.

- Added an Ivan Sincek PHP reverse shell and started a listener:
  ```bash
  nc -nlvp 4444
  ```

- Triggered the shell by visiting:
  ```
  http://$IP/shenzi/404.php
  ```

- Obtained a shell on the target system.

---

## 🚀 Privilege Escalation

- Ran `winPEASany.exe` and discovered:
  - Both `HKLM` and `HKCU` had `AlwaysInstallElevated` set to `1`.

- This meant any `.msi` file could be installed with administrative privileges.

- Generated a malicious `.msi` payload using `msfvenom`, uploaded it, and executed it.

- Successfully escalated privileges to SYSTEM.

---

🧼 **Post-Exploitation Note:**  
Unset `AlwaysInstallElevated` registry keys and remove payloads after use.

> ⚠️ This walkthrough is for educational purposes only.
