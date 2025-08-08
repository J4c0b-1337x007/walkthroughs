# Gaara - Walkthrough

## 🧗 Initial Foothold

### 🌐 1. Web Enumeration
- Used tools like `feroxbuster` and `gobuster` to enumerate multiple websites.
- Discovered multiple references to the word **"Gaara"**, often capitalized.
- Eventually determined the correct username was `gaara` (lowercase).

### 📝 2. Wordlist Tips
- When in doubt, generate a custom wordlist using `cewl`:
  ```bash
  cewl http://<target-ip> -w gaara_wordlist.txt
  ```

### 🔓 3. Brute-force Login
- Used `hydra` with `rockyou.txt` and the username `gaara`:
  ```bash
  hydra -l gaara -P /usr/share/wordlists/rockyou.txt ssh://<target-ip>
  ```
- Successfully discovered valid SSH credentials.

---

## ⚙️ Privilege Escalation

### 🔍 1. Run linPEAS
- Discovered that `/usr/bin/gdb` had the **SUID** bit set.

### ⚒️ 2. Exploit SUID GDB
- Abused `gdb` to get a root shell with:
  ```bash
  gdb -nx -ex '!sh' -ex quit
  ```
- Root shell obtained.

---

## 🧠 Notes

- Pay close attention to subtle patterns in usernames — capitalization can be misleading.
- Don’t hesitate to build your own wordlist with `cewl` when standard ones fail.
- SUID binaries like `gdb` are a classic escalation path — always scan for them with linPEAS or manually.
