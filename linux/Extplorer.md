# Extplorer (Linux)

## Initial Foothold

Used `gobuster` to enumerate directories and found `/filemanager` running on port 80. Logged in with default credentials `admin:admin`.
Uploaded a PHP reverse shell via the file manager to gain initial shell access.
Located the file `filemanager/config/.htusers.php`, extracted the password hash, and cracked it with John the Ripper using the rockyou wordlist.
Switched user to `dora` with the cracked password.

## Privilege Escalation

Ran `linpeas.sh` and discovered that the user belonged to the `disk` group.
Used this privilege escalation vector ([HackTricks reference](https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/interesting-groups-linux-pe/index.html)).
Accessed `/etc/shadow`, obtained the root hash, cracked it, and used `su root` to gain root access.

The box is rooted.
