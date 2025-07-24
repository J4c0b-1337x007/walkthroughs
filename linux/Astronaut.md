# 🏴 Astronaut (Linux)

## 🧠 Initial Foothold

- Exploited a **GravCMS** vulnerability:  
  [EDB-ID 49973](https://www.exploit-db.com/exploits/49973)

- Modified the exploit to append `/grav-admin` to the target URL.

- Crafted a **base64-encoded reverse shell payload** pointing to attacker IP on port 80.

- Started listener:
  ```bash
  sudo nc -nlvp 80
  ```

- Triggered the exploit and received a shell.

---

## 🚀 Privilege Escalation

- Ran `linpeas.sh` and found **PHP 7.4** binary with the **SUID** bit set.

- Verified via `cron` output and manual inspection.

- Used GTFOBins SUID abuse for PHP:
  ```bash
  CMD="/bin/sh"
  /usr/bin/php7.4 -r "pcntl_exec('/bin/sh', ['-p']);"
  ```

- Ensured correct PHP path and version were used.

- Successfully obtained a **root shell**.

---

🧼 **Post-Exploitation Note:**  
Remove reverse shell payloads and double-check SUID binaries for cleanup.

> ⚠️ This walkthrough is for educational purposes only.
