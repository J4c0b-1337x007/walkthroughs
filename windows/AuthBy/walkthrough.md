# 🏴 AuthBy (Windows)

## 🧠 Initial Foothold

- Connected to **FTP on port 21** using `anonymous:anonymous`.
- Discovered potential usernames: `offsec`, `anonymous`, and `admin`.
- Attempted to access the **HTTP service on port 242**, but it required authentication.
- Logged into FTP with `admin:admin`, which revealed a `.htpasswd` file containing Offsec's credentials.
- Used the same FTP access (`admin:admin`) to **upload a PHP reverse shell**.
- Triggered the shell through the web server, gaining a **reverse shell as `apache`** on the Windows system.

## 🚀 Privilege Escalation

- Executed `systeminfo` to determine the OS version.
- Found a suitable local privilege escalation exploit: [EDB-ID 40564](https://www.exploit-db.com/exploits/40564).
- Followed the instructions in the exploit and successfully escalated to **SYSTEM**.

---

🧼 **Post-Exploitation Note:**
Make sure to clean up the uploaded PHP shell and any dropped binaries.

> ⚠️ This walkthrough is for educational purposes only.
