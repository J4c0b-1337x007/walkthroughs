
# 🧪 Vmdak (Linux) Walkthrough

## 🔍 Initial Foothold

- Discovered web service on port **9443** (HTTPS).
- Identified login portal for a **Prison Management System**.
- Found exploit: [Exploit 52017.txt](https://www.exploit-db.com/exploits/52017).
- Discovered credentials:
  - **Username**: `Malcom`
  - **Password**: `RonnyCache001`
- Located the vulnerable **fast5** service.
  - Exploit sources:
    - https://github.com/Aa1b/mycve/blob/main/Readme.md
    - https://github.com/CveSecLook/cve/issues/31
- Uploaded `shell.php` using the exploit.
- Triggered reverse shell by browsing to:
  ```
  https://<IP>:9443/uploadImage/Profile/shell.php
  ```
- Used `su vmdak` with `RonnyCache001` to get user shell.

---

## 🚀 Privilege Escalation

- Tried MySQL enumeration – unsuccessful.
- Found local port **8080** open.
- Used **Ligolo** to pivot and access Jenkins UI on `http://240.0.0.1:8080`.
- Jenkins initial password found in:
  ```
  /root/.jenkins/secrets/initialAdminPassword
  ```
- Used exploit:
  ```
  python3 51993.py -u http://240.0.0.1:8080 -p /root/.jenkins/secrets/initialAdminPassword
  ```
- Logged into Jenkins as admin.
- Created **New Item** → **Freestyle project**.
- Configured **Build Step** with **Execute shell** using `busybox` reverse shell.
- Triggered job via **Build Now** to obtain reverse root shell.

---

## 📤 Git Commands

```bash
# Move the file to the linux walkthroughs folder
mv ~/Downloads/Vmdak.md ~/Downloads/walkthroughs_project_template/linux/Vmdak.md

# Change directory to the project root
cd ~/Downloads/walkthroughs_project_template

# Add all changes to git
git add .

# Commit the changes with a descriptive message
git commit -m "🧪 Added Vmdak (Linux) walkthrough"

# Push the commit to GitHub
git push
```
