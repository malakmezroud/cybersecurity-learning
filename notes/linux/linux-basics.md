# Linux Basics for Cybersecurity

> **Topic:** Linux Fundamentals  
> **Date:** April 2026  
> **Status:** ✅ Done

Linux is the backbone of cybersecurity. Most servers, SIEM tools, and security appliances run Linux. As a SOC analyst you'll read Linux logs and run commands daily.

---

## The Linux File System

```
/               Root
├── /bin        Essential commands (ls, cp, cat)
├── /etc        Config files (network, users, services)
├── /home       User home directories
├── /var        Variable data — LOGS at /var/log/
├── /tmp        Temp files (world-writable — attacker favorite!)
├── /proc       Running process info
└── /root       Root user home
```

**Security note:** Attackers often drop files in `/tmp`. Always check it during incident response.

---

## Users & Privileges

```bash
whoami              # Current username
id                  # UID, GID, groups
sudo command        # Run as root
cat /etc/passwd     # All users on the system
cat /etc/shadow     # Password hashes (root only!)
last                # Login history
lastb               # Failed login history
```

---

## Key Log Files (SOC Must-Know)

| File | What It Contains |
|---|---|
| `/var/log/auth.log` | Login attempts, sudo, SSH |
| `/var/log/syslog` | General system messages |
| `/var/log/apache2/access.log` | Web requests |
| `/var/log/ufw.log` | Firewall events |
| `/var/log/fail2ban.log` | Banned IPs |

```bash
# Watch live logins
tail -f /var/log/auth.log

# Find failed SSH logins
grep "Failed password" /var/log/auth.log

# Count failed logins by IP (detect brute force)
grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -rn | head -10

# Find successful logins
grep "Accepted password\|Accepted publickey" /var/log/auth.log
```

---

## Process & Service Management

```bash
ps aux              # All running processes
top / htop          # Live process monitor
lsof -i :80         # What's using port 80?
netstat -tulnp      # All listening ports
crontab -l          # Scheduled tasks (check for persistence!)
ls /etc/cron.d/     # System cron jobs
```

**Red flag:** Processes running from `/tmp` or unknown paths can indicate malware.

---

## Security One-Liners

```bash
# Find world-writable files (attacker landing spots)
find / -perm -002 -type f 2>/dev/null

# Find SUID binaries (priv esc vectors)
find / -perm -4000 -type f 2>/dev/null

# Recently modified files in /etc
find /etc -mtime -1 -type f 2>/dev/null

# Search for plaintext passwords
grep -r "password" /etc/ 2>/dev/null | grep -v "#"
```

---

*See also: `tools/linux-commands/linux-cheatsheet.md`*  
*Source: Personal study notes + TryHackMe Linux Fundamentals path*
