# 🦂 Mzeeav (Linux)

## 🚪 Initial Foothold

Discovered a `backup.zip` archive containing a file named `upload.php`. This file checks the magic bytes (first 2 bytes) of an uploaded file. If the file starts with `MZ`, it allows execution — hinting at a bypass using PE file header bytes (`4D5A` in hex).

🔍 Used this trick to bypass the filter:
- Prepended `MZ` to the beginning of a PHP reverse shell script.
- Used this [reverse shell](https://github.com/xdayeh/Php-Reverse-Shell/blob/master/PHP-Reverse-Shell.php) because the default one didn’t work.
- Uploaded the file to: `http://<IP>/upload/shell.php`
- Got shell via listener on port 80.

🧠 **Understand the logic** in `upload.php`:
```php
if ( strpos($magicbytes, '4D5A') === false ) {
    echo "Error no valid PEFILE\n";
    exit ();
}
```

## 🧑‍💻 Privilege Escalation

Searched for SUID binaries:
```bash
find / -perm /4000 2>/dev/null
```

Found: `/opt/fileS`  
🧪 This binary lists files in a given directory. Running `/opt/fileS --version` reveals it uses the `find` command.

Used `find` from GTFOBins for escalation:
```bash
/opt/fileS . -exec /bin/sh -p \; -quit
```

⬆️ Gained root shell!

---

## 🧩 Key Takeaways

🔐 Inspect zip backups — they often leak important files.  
📜 Understand logic in PHP scripts — magic byte checks can be bypassed.  
🧰 Identify and abuse custom SUID binaries.  
🔎 Use `--version`, `-h`, and trial commands to fingerprint unknown binaries.  
🪄 GTFOBins is a lifesaver when SUID is involved!

