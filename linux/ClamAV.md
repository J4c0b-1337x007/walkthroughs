# ClamAV (Linux)

## Initial Foothold

Scanned the target and found several open ports, including 25 (Sendmail SMTP) and 80 (HTTP). Used `searchsploit` to identify a remote code execution vulnerability in ClamAV-milter via Sendmail (`4761.pl`). Downloaded the exploit with `searchsploit -m 4761.pl`, then executed:

    perl 4761.pl 192.168.164.42

## Privilege Escalation

Connected to the target with:

    nc 192.168.164.42 31337

Interacted with the shell and immediately received a root shell, as the exploit grants root access upon connection.
