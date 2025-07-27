# Compromised - Walkthrough

## 🧗 Initial Foothold

### 🗂️ 1. SMB Enumeration
- Discovered open SMB shares.
- While enumerating, found a user named `scripting` with PowerShell:
  ```powershell
  $credential = New-Object System.Management.Automation.PSCredential ('scripting', $password)
  ```

### 🔍 2. Found Encoded Password
- Accessed the `Users$` share.
- Navigated to:
  ```
  Users$/scripting/Documents/profile.ps1
  ```
- Found a **Base64-encoded password** inside `profile.ps1`.

### 🔓 3. Decode and Access
- Decoded the Base64 password.
- Logged in via `evil-winrm` as `scripting`.

---

## ⚙️ Privilege Escalation

### 🧪 1. Analyze `C:\Troubleshooting`
- Inside `C:\Troubleshooting` found:
  - `ps.1` script
  - Ran it and it generated an output `.csv` file

### 🧠 2. Decode the CSV
- Inside the `.csv` file was encoded Base64 content.
- Decoded the Base64 using [CyberChef](https://gchq.github.io/CyberChef/)

### 🔐 3. Use CyberChef to Extract Admin Password
- Important tips:
  - You **don’t need to understand the full script**
  - Focus on **keywords** like:
    - Base64
    - gzip
    - hex
  - Use decoding flows like:
    - Base64 → gzip → UTF-8
    - HEX → DEFLATE → ASCII

### ✅ 4. Login as Administrator
- Extracted the Administrator password successfully from decoded content.
- Logged in with full admin access.

---

## 🧠 Notes

- Creative decoding and forensic-style analysis were key to success.
- Use CyberChef early when dealing with encoded or suspicious blob data.
- Don't overthink the script — just try transformations until it clicks.
