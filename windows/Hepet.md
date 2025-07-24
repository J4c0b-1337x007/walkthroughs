# 🏴 Hepet (Windows)

## 🧠 Initial Foothold

- Used `cewl` to enumerate the username `jonas`.
- Ran `hydra` to brute-force credentials on port 143 (IMAP) and found valid login details.
- Connected to port 143 with `nc` and ran IMAP commands to access emails ([see reference](obsidian://open?vault=Obsidian%20Vault&file=Port%20143%20and%20993%20-%20imap)). Determined that a macro-based reverse shell was needed.
- Exploited [LibreOffice Macros](obsidian://open?vault=Obsidian%20Vault&file=LibraOffice%20Calc%20macro%20reverse%20shell) to obtain an initial shell.

---

## 🚀 Privilege Escalation

- Enumerated running services using:

  ```powershell
  Get-CimInstance -ClassName win32_service | Select Name,State,PathName | Where-Object {$_.State -like 'Running'}
  ```

- Renamed the original service binary with:  
  `move veyon-service.exe veyon-service.exe.bak`

- Uploaded a malicious `veyon-service.exe` reverse shell payload, replaced the original, and restarted the system with `shutdown /r`.

- Obtained a reverse shell as SYSTEM after the reboot.

---

🧼 **Post-Exploitation Note:**  
Remove the replaced binary and restore the original service if applicable.

> ⚠️ This walkthrough is for educational purposes only.
