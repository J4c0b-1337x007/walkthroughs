# GlasgowSmile - Walkthrough

## 🧗 Initial Foothold

### 🌐 1. Web Enumeration
- Port **80** open.
- Found **Joomla** login panel: `/joomla/administrator`.
- Detected a Joomla extension.

### 🛠️ 2. Wordlist and Burp
- Created custom wordlist with `cewl`.
- Cleaned out default/noisy entries manually.
- Performed **Cluster Bomb** attack using **Burp Suite**.
- Discovered login credentials:
  ```
  Username: joomla
  Password: Gotham
  ```

### 🧨 3. Template Injection
- Logged in to Joomla admin panel.
- Navigated to:
  ```
  System → Configuration → Templates
  ```
- Selected the template: **Protostar**  
  *(Right corner under Beez3)*

- Edited `index.php` to include reverse shell payload.
- Got a shell.

---

## ⚙️ Privilege Escalation

### 🔐 1. Extracting MySQL Credentials
- Found `configuration.php` file after initial shell access.
- Extracted MySQL credentials.

### 🗄️ 2. Exploring the `batjoke` DB
- In table `taskforce`, found a **base64-encoded password** for user `rob`.
- Decoded the password → SSH as `rob`.

### 🧩 3. Abner User Enumeration
- Found a root-owned script running:
  ```
  /home/penguin/SomeoneWhoHidesBehindAMask/.trash_old
  ```

- Found `abner` file in `rob`'s home directory.
  - Decrypted it using:
    - **ROT1**
    - Then base64 decoding

- Logged in as user `abner`.

### 🔎 4. Finding Penguin Clues
- Ran:
  ```bash
  find / 2>/dev/null | grep "trash"   # or any pattern relevant
  ```
- Found a **zip file**, cracked it using Abner's password.
- Inside was a file that revealed **Penguin’s password**.

### 🐧 5. Root via Shell Change
- SSH as user `penguin`.
- In Penguin’s home directory, found a shell file.
- Used `nano` to change the shell code → got **root** shell.

---

## 🧠 Notes

- Joomla’s admin panel gives a huge attack surface. Template editing = RCE.
- ROT1 + base64 is a common double obfuscation trick.
- Local scripts owned/run by root are always worth reviewing.
- Changing shell scripts directly is a powerful privilege escalation path if permissions allow.

