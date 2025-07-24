# 🏴 Apex (Linux)

## 🧠 Initial Foothold

- Enumerated the target with Nmap and discovered:
  - HTTP (port 80)
  - SMB (port 445)
  - MySQL (port 3306)

- Found accessible SMB share "docs" containing PDFs; one PDF referenced **OpenEMR**.

- Searched the OpenEMR GitHub repository and noted a potential SQL password in `sqlconf.php`.

- Identified possible usernames from the hospital’s website.

- Located the OpenEMR login page and found it was running version **5.0.1**.

- Attempted known OpenEMR exploits (needed credentials).

- Used directory brute-forcing and discovered a vulnerable **file manager with upload capabilities**.

- Exploited the file manager to copy sensitive files (e.g. `sqlconf.php`) into the SMB share, retrieved them, and extracted valid MySQL credentials.

- Accessed the database and dumped password hashes from `users_secure` table.

- Cracked the admin hash using `hashcat`.

- Logged in as OpenEMR administrator.

---

## 🚀 Privilege Escalation

- With admin access to OpenEMR, used:  
  [EDB-ID 45161](https://www.exploit-db.com/exploits/45161) to get a reverse shell as `www-data`.

- Discovered the SQL password was reused for the `root` account.

- Switched user to root with:
  ```bash
  su
  ```
  Using the same password.

- Successfully obtained full root access.

---

🧼 **Post-Exploitation Note:**  
Always verify password reuse for privilege escalation and clean file uploads from file managers.

> ⚠️ This walkthrough is for educational purposes only.
