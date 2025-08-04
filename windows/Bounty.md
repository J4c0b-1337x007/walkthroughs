# Bounty - Walkthrough (Windows)

## 🎯 Initial Foothold

### 🌐 1. Web Enumeration
- Found port **80** open, hosting a web app.
- Located a file upload feature on `transfer.aspx`.

### 🛡️ 2. Bypassing Upload Restrictions
- Tested file types manually and with Burp Suite.
- Successfully uploaded a **web.config** file.

### 💡 3. Using web.config for Code Execution
- Used a malicious `web.config` file with an embedded **ASP reverse shell**.

#### Helpful References:
- [Nanobyte Security | Bypassing File Upload Restrictions and Leveraging web.config](https://nanobytesecurity.com/2021/09/13/web-config-file-upload-bypass.html)
- [Upload a web.config File for Fun & Profit | Soroush Dalili](https://soroush.me/blog/2014/07/upload-a-web-config-file-for-fun-profit/)
- [Lonewolf Tech - RCE via web.config](https://lonewolfzero.wordpress.com/2018/05/28/rce-by-uploading-a-web-config-asp/)
- [Reverse Shell Generator](https://www.revshells.com/)

### 🐚 4. Execution
- Uploaded the web.config payload
- Started listener and triggered the upload path
- Gained reverse shell successfully.

---

## ⚙️ Privilege Escalation

### 🧾 1. Check for Vulnerabilities
- Ran:
  ```cmd
  systeminfo
  ```

- Noticed no hotfixes or security patches applied.

### 🔍 2. Kernel Exploit - CVE-2018-8120
- Searched OS version on:
  [SecWiki/windows-kernel-exploits](https://github.com/SecWiki/windows-kernel-exploits)

- Found matching exploit:
  [CVE-2018-8120 Exploit Code](https://github.com/SecWiki/windows-kernel-exploits/tree/master/CVE-2018-8120)

### ⚙️ 3. Exploiting
- Compiled/Downloaded the `x64.exe` payload.
- Transferred it to target (via web or SMB).
- Ran it from the shell.
- Gained SYSTEM-level shell.

---

## ✅ Summary
- Uploaded web.config to bypass restrictions and get RCE
- Used known Windows kernel exploit due to unpatched system
- Classic Windows privilege escalation via public exploit
