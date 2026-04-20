# Linux Command Cheat Sheet

> **Topic:** Linux for Cybersecurity  
> **Date:** April 2026  
> **Status:** 🔄 In Progress

Essential Linux commands for cybersecurity, SOC analysis, and pen testing.

---

## Navigation & Files

```bash
pwd                     # Print current directory
ls -la                  # List all files with permissions
cd /path/               # Change directory
find / -name "*.log"    # Find files by name
cat file.txt            # Print file
tail -f file.log        # Live log monitoring
grep "Failed" auth.log  # Search in file
```

---

## File Permissions

```bash
chmod 755 script.sh     # Set permissions
chmod +x script.sh      # Make executable
chown user:group file   # Change ownership
ls -l                   # View permissions
```

| Number | Permission |
|---|---|
| 7 | rwx |
| 6 | rw- |
| 5 | r-x |
| 4 | r-- |

---

## Networking

```bash
ip a / ifconfig         # View interfaces and IPs
ping 8.8.8.8            # Test connectivity
netstat -tulnp          # Open ports and services
ss -tulnp               # Modern alternative
nslookup google.com     # DNS lookup
dig google.com          # Detailed DNS query
curl -I https://site    # Get HTTP headers
```

---

## Users & System

```bash
whoami                  # Current user
id                      # UID, GID, groups
ps aux                  # All running processes
top                     # Live process monitor
kill -9 PID             # Force kill process
uname -a                # Kernel/OS info
history | grep ssh      # Search command history
```

---

## Log Analysis (SOC)

```bash
# Key log files
/var/log/auth.log       # Auth attempts
/var/log/syslog         # System messages
/var/log/apache2/       # Web server logs

# Watch live logins
tail -f /var/log/auth.log

# Find failed SSH logins
grep "Failed password" /var/log/auth.log

# Count failed logins by IP (attacker detection)
grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -rn
```

---

## SSH

```bash
ssh user@192.168.1.1        # Connect remotely
scp file.txt user@host:/    # Secure file copy
ssh-keygen -t rsa           # Generate SSH keys
```

---

*Updated as I progress through TryHackMe Linux rooms and home lab practice.*
