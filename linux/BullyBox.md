# 🏴 BullyBox (Linux)

## 🧠 Initial Foothold

- Ran `dirb` and discovered a hidden `.git` directory.

- Used `git-dumper` to retrieve the repo:
  ```bash
  git-dumper http://bullybox.local/ git_loot
  ```

- Read `bb-config.php` and found admin credentials.

- In `bb-config-sample.php`, identified the login path:
  ```
  http://www.yourdomain.com/index.php?_url=/bb-admin
  ```

- Logged into the CMS with credentials.

- Located and used [Exploit 51108](https://www.exploit-db.com/exploits/51108), which requires admin access.

- Crafted a valid POST request (based on exploit + [adjusted request](obsidian://open?vault=Obsidian%20Vault&file=BullyBox%20POST%20request%20to%20get%20RCE)).

- Started a listener on port 80:
  ```bash
  nc -nlvp 80
  ```

- Visited `/ax.php` and received a shell.

---

## 🚀 Privilege Escalation

- Ran:
  ```bash
  sudo -l
  ```

- Found permission to run:
  ```bash
  (ALL) NOPASSWD: /bin/su
  ```

- Escalated with:
  ```bash
  sudo su
  ```

- Gained root access.

---

🧼 **Post-Exploitation Note:**  
Clear `.git` folder exposure and CMS credentials. Clean up web shell if uploaded.

> ⚠️ This walkthrough is for educational purposes only.
