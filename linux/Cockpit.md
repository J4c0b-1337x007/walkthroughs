# Cockpit (Linux)

## Initial Foothold

Found two login pages: `$IP:80/login.php` and `$IP:9090`. Attempted SQL injection on the first login page; the payload `' OR 1=1 --` did not work, but `' AND 1=1 -- -` successfully bypassed authentication. Retrieved valid credentials and used them to log in to the admin interface on port 9090.

## Privilege Escalation

Ran `sudo -l` as user `james` and saw permission to run `tar` with root privileges:

    (ALL) NOPASSWD: /usr/bin/tar -czvf /tmp/backup.tar.gz *

Consulted [GTFOBins](https://gtfobins.github.io/gtfobins/tar/#sudo) and executed:

    sudo /usr/bin/tar -czvf /tmp/backup.tar.gz * --checkpoint=1 --checkpoint-action=exec=/bin/sh

to gain a root shell.
