# Clue (Linux)

## Initial Foothold

Exploited a vulnerable Cassandra Web interface to read sensitive files like `/etc/passwd`, `/proc/self/cmdline`, and `/etc/ssh/sshd_config`, which revealed user credentials and SSH access details. Used this access to retrieve the FreeSWITCH event socket password from `/etc/freeswitch/autoload_configs/event_socket.conf.xml`. Modified a FreeSWITCH exploit to use the correct password and launched a reverse shell (using busybox) on port 3000, successfully obtaining shell access.

## Privilege Escalation

Switched to the `cassie` user with discovered credentials and checked `sudo -l`, finding permission to run `/usr/local/bin/cassandra-web` as root. Started a new vulnerable Cassandra server instance as root with:

```bash
sudo cassandra-web -B 0.0.0.0:4444 -u cassie -p SecondBiteTheApple330
```

Opened a second shell, transferred the Cassandra Web exploit to the target, changed the port to 4444 in the exploit, and used it to read `/home/anthony/.ssh/id_rsa`. Tried SSH access as both `anthony` and `root` with the private key—root access was successful.
