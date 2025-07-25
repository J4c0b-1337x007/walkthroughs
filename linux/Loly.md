
# 🐧 Loly (Linux) Walkthrough

## 🔍 Initial Foothold

- Ran `nmap` and discovered **port 80** open.
- Visited the site and identified a **WordPress installation**.
- Added the following to `/etc/hosts`:
  ```
  10.x.x.x loly.cl
  ```
- Ran `wpscan --update` followed by enumeration using:
  ```bash
  wpscan --url http://loly.cl --enumerate u
  ```
- Recovered a valid **username and password** for WordPress.
- Logged in to the **WordPress admin panel**.
- Navigated to **AdRotate plugin > Manage Media** and uploaded a **ZIP file** containing a PHP web shell.
- WordPress automatically extracted it to:
  ```
  /wp-content/banners/shell.php
  ```
- Triggered the shell by visiting the uploaded path and received a **reverse shell** back. 🎯

---

## 🚀 Privilege Escalation

- Navigated to:
  ```
  /var/www/html/
  ```
- Found `wp-config.php` and extracted **database credentials**.
- Attempted to switch user:
  ```bash
  su loly
  ```
  using the password found in `config.php`, and successfully got a shell as `loly`.

- Uploaded and ran `linpeas.sh` – discovered the system was running a vulnerable **Linux Kernel < 4.13.9** (specifically Ubuntu 16.04).
- Chose the following local privilege escalation exploit:
  > [Linux Kernel < 4.13.9 (Ubuntu 16.04 / Fedora 27) - Local Privilege Escalation](https://www.exploit-db.com/exploits/45010)

- Steps:
  1. Transferred the `.c` file to the target machine.
  2. Gave full permissions:
     ```bash
     chmod 777 exploit.c
     ```
  3. Compiled it:
     ```bash
     gcc exploit.c -o rootme
     ```
  4. Executed the binary and popped a **root shell**! 🦍

---

## ✅ Summary

- **Initial Access:** WordPress AdRotate media upload + reverse shell
- **User Shell:** Password reuse from `wp-config.php`
- **Privilege Escalation:** Linux Kernel < 4.13.9 LPE (exploit-db 45010)
