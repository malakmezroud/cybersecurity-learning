# Lab: Nmap Network Scanning

> **Lab Type:** Hands-On Practice
> **Difficulty:** Beginner
> **Tools:** Nmap, Linux terminal
> **Environment:** Use on your own machine, local network, or TryHackMe/HackTheBox lab VMs only

---

## Objectives

- Learn to run basic Nmap scans
- Understand different scan types and when to use them
- Identify open ports, services, and OS information
- Document findings professionally

---

## Background

**Nmap (Network Mapper)** is the industry-standard open-source tool for network discovery and security auditing. It's used by penetration testers, security engineers, and network admins worldwide.

**Legal note:** Only scan systems you own or have explicit written permission to test. Unauthorized scanning is illegal.

---

## Part 1: Basic Host Discovery

```bash
# Check if a host is up (ping scan - no port scan)
nmap -sn 192.168.1.0/24

# Single host discovery
nmap -sn 192.168.1.1

# Scan without DNS resolution (faster)
nmap -n -sn 192.168.1.0/24
```

**Expected output:** List of hosts that responded to ping probes.

---

## Part 2: Port Scanning

```bash
# Default scan (top 1000 ports, SYN scan if root)
nmap 192.168.1.1

# Scan all 65535 ports
nmap -p- 192.168.1.1

# Scan specific ports
nmap -p 22,80,443,3389 192.168.1.1

# Scan a port range
nmap -p 1-1024 192.168.1.1

# Fast scan (top 100 ports)
nmap -F 192.168.1.1
```

---

## Part 3: Scan Types

```bash
# SYN scan (stealth scan, requires root)
sudo nmap -sS 192.168.1.1

# TCP connect scan (no root needed, more detectable)
nmap -sT 192.168.1.1

# UDP scan (slower, finds DNS/SNMP/DHCP services)
sudo nmap -sU 192.168.1.1

# Comprehensive scan: SYN + UDP
sudo nmap -sSU 192.168.1.1
```

---

## Part 4: Service & Version Detection

```bash
# Detect service versions
nmap -sV 192.168.1.1

# Aggressive version detection
nmap -sV --version-intensity 9 192.168.1.1

# OS detection (requires root)
sudo nmap -O 192.168.1.1

# All-in-one: version + OS + scripts + traceroute
sudo nmap -A 192.168.1.1
```

---

## Part 5: Nmap Scripting Engine (NSE)

```bash
# Run default scripts
nmap -sC 192.168.1.1

# Run a specific script
nmap --script=http-title 192.168.1.1

# Run vulnerability scripts
nmap --script=vuln 192.168.1.1

# Check for SMB vulnerabilities (EternalBlue)
nmap --script=smb-vuln-ms17-010 192.168.1.1

# HTTP enumeration
nmap --script=http-enum 192.168.1.1
```

---

## Part 6: Output & Reporting

```bash
# Save output to all formats
nmap -oA scan_results 192.168.1.1

# Normal output
nmap -oN scan.txt 192.168.1.1

# XML output (for tools like Metasploit)
nmap -oX scan.xml 192.168.1.1

# Grepable output
nmap -oG scan.gnmap 192.168.1.1
```

---

## Lab Exercise

1. Run a ping sweep on your local /24 subnet
2. Pick one live host and run a full port scan
3. Run service/version detection on the open ports
4. Run default NSE scripts and note the output
5. Save results in all three formats

**Document your findings:**

| Port | State | Service | Version |
|---|---|---|---|
| | | | |

---

## Key Flags Reference

| Flag | Description |
|---|---|
| `-sS` | SYN (stealth) scan |
| `-sV` | Version detection |
| `-O` | OS detection |
| `-A` | Aggressive (OS + version + scripts) |
| `-p-` | All ports |
| `-F` | Fast (top 100 ports) |
| `-oA` | Output all formats |
| `-v` / `-vv` | Verbose output |
| `--script` | Run NSE script |

---

*Next: Try scanning a TryHackMe room like "Nmap" or "Further Nmap".*
