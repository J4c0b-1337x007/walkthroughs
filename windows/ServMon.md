# ServMon - Walkthrough

## 🧗 Initial Foothold

### 🔍 1. FTP Enumeration
- Found **port 21 (FTP)** open.
- Discovered two usernames by reviewing downloaded files.
- Found a hint toward `Passwords.txt` on Nathan's desktop.

### 🌐 2. Port 80 Web Service
- Accessed a web interface.
- Ran `searchsploit` for **NVMS 1000** and found:
  ```
  NVMS 1000 - Directory Traversal (hardware/webapps/47774.txt)
  ```
- Used directory traversal to read `C:\\Users\\Nathan\\Desktop\\Passwords.txt`.

### 🗝️ 3. Brute-force SSH Access
- Retrieved potential passwords from `Passwords.txt`.
- Ran `hydra` on usernames **Nadine** and **Nathan**.
  - Successful login with **Nadine** credentials.
- SSH into the machine using Nadine’s credentials.

---

## ⚙️ Privilege Escalation

### 🔎 1. NSClient++ Service on Port 8443
- Found **NSClient++** running over HTTPS on port `8443`.
- Located exploit:
  ```
  NSClient++ 0.5.2.35 - Privilege Escalation
  (windows/local/46802.txt)
  ```

### 🧠 2. Discovering Password
- Navigated to:
  ```
  C:\\Program Files\\NSClient++
  ```
- Retrieved the service password by:
  - Running:
    ```
    nscp web -- password --display
    ```
  - Or inspecting:
    ```
    nsclient.ini
    ```

### 🔁 3. Bypass Localhost Restriction
- Discovered that **localhost-only** restriction was configured in `nsclient.ini`.
- Used **SSH port forwarding** to bypass:
  ```bash
  ssh -L <local-port>:127.0.0.1:8443 nadine@<target-ip>
  ```

### 💣 4. Exploit NSClient++
- Used this public exploit:
  [xtizi/NSClient-0.5.2.35---Privilege-Escalation](https://github.com/xtizi/NSClient-0.5.2.35---Privilege-Escalation/tree/master)
- Uploaded `nc.exe` to:
  ```
  C:\\Users\\Nadine\\AppData\\Local\\Temp
  ```
- Gained SYSTEM shell.

---

## 🧠 Notes

- Always check `nsclient.ini` for restrictions.
- Directory traversal + misconfigured service = full compromise.
- SSH port forwarding is essential for exploiting localhost-bound services remotely.
