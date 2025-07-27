# Compromised - Walkthrough

## 🧗 Initial Foothold

### 🗂️ 1. SMB Enumeration
- Discovered open SMB shares.
- Enumerated shares and identified a user called `scripting` using PowerShell:
  ```powershell
  $credential = New-Object System.Management.Automation.PSCredential ('scripting', $password)
  ```

### 🔍 2. Extract Credentials from Share
- Accessed the `Users$` share.
- Navigated to:
  ```
  Users$/scripting/Documents/profile.ps1
  ```
- Found a **Base64-encoded password** inside the PowerShell profile script.

### 🔓 3. Decode and Gain Shell
- Decoded the Base64 string to retrieve the password.
- Logged into the machine using `evil-winrm` as user `scripting`.

---

## ⚙️ Privilege Escalation

### 🔍 1. Investigate `C:\Troubleshooting`
- Inside the `C:\Troubleshooting` directory, found:
  - `ps.1`
  - `runit`
  - An output `.csv` file

### 🧪 2. Analyze CSV Output
- The CSV contained suspicious Base64 data.
- Decoded the string using tools like [CyberChef](https://gchq.github.io/CyberChef/).

### 🧠 3. CyberChef Tips
- Use keyword searches inside CyberChef (e.g., "decode", "gzip", "hex", etc.)
- You don’t need to fully understand the PowerShell or encoded data — just experiment.
- The key is to **try multiple decoding layers** — e.g.,:
  - Base64 → gzip → ASCII
  - HEX → DEFLATE → UTF-8

### 🔑 4. Final Step
- Successfully extracted the **Administrator password**.
- Logged in and gained full access.

---

## 🧠 Notes

- This machine rewards creative enumeration and smart decoding.
- Look for base64, gzip, and other encoding layers in Windows environments.
- CyberChef is your friend — don’t overlook encoded data blobs.
