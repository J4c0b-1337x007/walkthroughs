# Craft - Walkthrough

## 🧗 Initial Foothold

### 📎 1. Malicious `.odt` File via LibreOffice
- Same technique as in `Hepet` machine.
- Used a malicious `.odt` document with embedded **macro reverse shell**.

🔗 References:
- [How to reverse shell an odt file](obsidian://open?vault=Obsidian%20Vault&file=LibraOffice%20Calc%20macro%20reverse%20shell)
- [YouTube Walkthrough](https://www.youtube.com/watch?v=is82gWkM3Jc)

---

## ⚙️ Privilege Escalation

### 📤 1. Web Shell via XAMPP
- Uploaded `shell.php` to:
  ```
  C:\xampp\htdocs
  ```
- Triggered it from browser to get a **reverse shell**.

### 🛡️ 2. SeImpersonatePrivilege + PrintSpoofer
- Ran:
  ```cmd
  whoami /priv
  ```
  - Noticed `SeImpersonatePrivilege` enabled for `apache` user.

- Used **PrintSpoofer64.exe** to escalate to **NT AUTHORITY\SYSTEM**.

---

## 🧠 Notes

- Malicious ODT files via LibreOffice macros are very effective initial footholds.
- XAMPP environments often expose writable `htdocs` folders.
- SeImpersonatePrivilege + PrintSpoofer is a classic and reliable PE combo on misconfigured services.
