# 🏴 BitForge (Linux)

## 🧠 Initial Foothold

- Added the target host to `/etc/hosts` and found a secondary login page.

- Discovered a `.git` directory and used `git-dumper` to retrieve the repository.

- Examined the commit history using:
  ```bash
  git log
  git show
  ```

- Found a file with credentials and used them to access MySQL.

- Found info about the **soplanning** application.

- Research (see [this blog](https://blog.quarkslab.com/pwn-everything-bounce-everywhere-all-at-once-part-2.html)) showed the password format should be `cle|password`.

- Resulting credentials:
  ```
  admin:dbee8fd60fd4244695084bd84a996882|77ba9273d4bcfa9387ae8652377f4c189e5a47ee
  ```

- Used exploit `52082.py` to gain shell:
  ```bash
  python3 52082.py -t http://plan.bitforge.lab/www/ -u admin -p 'dbee8fd60fd4244695084bd84a996882|77ba9273d4bcfa9387ae8652377f4c189e5a47ee'
  ```

---

## 🚀 Privilege Escalation

- Upgraded to a normal shell using `Perl`.

- Ran `pspy32s` and captured the `jack` password from a running process.

- Ran `sudo -l` and found:
  ```bash
  (ALL) NOPASSWD: /usr/bin/flask_password_changer
  ```

- This script launches Flask from `/opt/password_change_app/app.py` (writable).

- Overwrote `app.py` with a reverse shell and triggered the service.

- Received a **root shell**.

---

🧼 **Post-Exploitation Note:**  
Restore Flask script, secure `.git` folders, and reset exposed credentials.

> ⚠️ This walkthrough is for educational purposes only.
