# Fanatastic (Linux)

## Initial Foothold

Exploited a vulnerability with:

```bash
python3 50581.py -H http://192.168.110.181:3000
```

to access sensitive files such as `/etc/passwd`, `/etc/grafana/grafana.ini`, and `/var/lib/grafana/grafana.db`. Found an encoded admin password in the database. Used [Grafana-Decryptor-for-CVE-2021-43798](https://github.com/Sic4rio/Grafana-Decryptor-for-CVE-2021-43798) to decrypt the password after installing required Python modules:

```bash
pip install requests questionary termcolor cryptography --break-system-packages
```

Ran the provided `decrypt.py` script and successfully recovered admin credentials.

## Privilege Escalation

Executed `linpeas.sh` and discovered membership in the `disk` group, which allowed reading sensitive files. Read `/root/.ssh/id_rsa`, transferred the private key to Kali, set proper permissions with:

```bash
chmod 600 root_id_rsa
```

Then connected as root via SSH:

```bash
ssh -i root_id_rsa root@$IP
```
