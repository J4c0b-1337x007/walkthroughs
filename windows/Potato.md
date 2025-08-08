
# 🥔 Potato (Linux) Walkthrough

## 🔍 Initial Foothold

- Discovered an **admin login page**.
- Ran `nmap` and found **FTP open on port 2112**.
- Downloaded `index.php.bak` via FTP and found a suspicious use of:
  ```php
  strcmp($password, $input)
  ```
- Researched **strcmp PHP bypass** and found:
  > [PHP strcmp Bypass (ABCTF2016 - L33t H4xx0r)](https://www.doyler.net/security-not-included/bypassing-php-strcmp-abctf2016)

- Using Burp Suite, modified the request:
  ```
  password=password[]=%22%22
  ```
  This bypassed the login!

- After logging in, navigated to the **log page**, which allowed downloading logs.

- Intercepted the request with Burp and manipulated:
  ```
  file=../../../../../../etc/passwd
  ```
  Retrieved `/etc/passwd` and found a **username and password hash**.

- Cracked the hash with `john` and logged in via **SSH**. 🔑

---

## 🚀 Privilege Escalation

- Ran:
  ```bash
  sudo -l
  ```
  and found:
  ```
  (ALL) NOPASSWD: /bin/nice /notes/*
  ```

- Inside `/notes/` were two `.sh` files.

- Tried reading them using the same **directory traversal technique** from earlier.

- Tried uploading custom scripts and using **GTFObins**.

- Ultimately, the following command worked to get a root shell:
  ```bash
  sudo /bin/nice /notes/../../../bin/bash
  ```

🧨 Root shell achieved!

---

## ✅ Summary

- **Initial Access:** FTP → Bypass strcmp login → LFI → hash cracking → SSH
- **Privilege Escalation:** Directory traversal with `nice` to execute bash as root
