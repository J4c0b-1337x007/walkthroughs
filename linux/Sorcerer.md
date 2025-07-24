# 🧙 Sorcerer (Linux)

## 🌐 Initial Foothold

- Found a restrictive SSH setup that prevents normal access, even with the private key.
- 💡 However, we **have the id_rsa** file and can use `scp` to bypass this restriction and overwrite `authorized_keys`.

### ✅ Command to Overwrite Authorized Keys:
```bash
scp -O -i id_rsa authorized_keys USERNAME@IP:/home/$USERNAME/.ssh/authorized_keys
```
- `-O`: Overwrite mode.

Once the key is replaced with our own, we can SSH into the machine with full access.

---

## 🧨 Privilege Escalation

- Uploaded and ran `linpeas.sh`.
- 🔍 Found an interesting **SUID binary**: `/sbin/start-stop-daemon`.

### 🚀 Abusing `start-stop-daemon` (GTFObins):
```bash
/sbin/start-stop-daemon -S -x /bin/bash
```
- This spawns a root shell.

---

## 🔑 Summary

- 🔐 Overwrite `authorized_keys` using `scp` and a valid `id_rsa`.
- 📈 Escalate with SUID binary `start-stop-daemon`.
