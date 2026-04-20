# Networking Basics for Cybersecurity

> **Topic:** Networking Fundamentals
> **Date:** April 2026
> **Status:** 🔄 In Progress

Understanding networking is essential for cybersecurity — most attacks exploit network protocols and misconfigurations.

---

## The OSI Model

| Layer | Name | Role | Example Protocols |
|---|---|---|---|
| 7 | Application | User-facing services | HTTP, DNS, FTP, SMTP |
| 6 | Presentation | Encryption, encoding | SSL/TLS, JPEG |
| 5 | Session | Manage sessions | NetBIOS, RPC |
| 4 | Transport | End-to-end delivery | TCP, UDP |
| 3 | Network | Logical addressing/routing | IP, ICMP, ARP |
| 2 | Data Link | Physical addressing | Ethernet, MAC, Switches |
| 1 | Physical | Raw bits over media | Cables, Wi-Fi |

**Security tip:** Most attacks target Layers 3–7. Know which layer each attack operates on.

---

## TCP vs UDP

| Feature | TCP | UDP |
|---|---|---|
| Connection | Connection-oriented | Connectionless |
| Reliability | Reliable (ACK) | Unreliable |
| Speed | Slower | Faster |
| Use case | HTTP, SSH, FTP | DNS, VoIP, streaming |

**TCP 3-Way Handshake:** SYN → SYN-ACK → ACK

**Security relevance:** SYN flood attacks exploit the TCP handshake to exhaust server resources.

---

## Key Ports to Know

| Port | Protocol | Service |
|---|---|---|
| 21 | TCP | FTP |
| 22 | TCP | SSH |
| 23 | TCP | Telnet (insecure!) |
| 25 | TCP | SMTP |
| 53 | UDP/TCP | DNS |
| 80 | TCP | HTTP |
| 443 | TCP | HTTPS |
| 445 | TCP | SMB |
| 3389 | TCP | RDP |
| 8080 | TCP | HTTP alt |

---

## IP Addressing

### IPv4
- 32-bit address (e.g., 192.168.1.1)
- Classes: A (1–126), B (128–191), C (192–223)
- Private ranges: 10.x.x.x, 172.16–31.x.x, 192.168.x.x

### Subnetting
- CIDR notation: 192.168.1.0/24
- /24 = 255 hosts, /16 = 65535 hosts
- Useful for network segmentation (reduces attack surface)

### IPv6
- 128-bit address
- No broadcasts — uses multicast
- Example: 2001:0db8:85a3::8a2e:0370:7334

---

## DNS (Domain Name System)

- Translates domain names → IP addresses
- Record types: A, AAAA, MX, CNAME, TXT, NS

**Security risks:**
- DNS poisoning / spoofing
- DNS tunneling (C2 over DNS)
- Zone transfer exploitation (AXFR)

```bash
# Check DNS records
nslookup example.com
dig example.com ANY
```

---

## Common Network Attacks

| Attack | Description |
|---|---|
| ARP Spoofing | Link fake MAC to valid IP (enables MITM) |
| DNS Poisoning | Corrupt DNS cache to redirect traffic |
| SYN Flood | Exhaust TCP connections (DoS) |
| MITM | Intercept traffic between two parties |
| Port Scanning | Enumerate open ports (Nmap) |
| VLAN Hopping | Escape VLAN segmentation |

---

## Firewalls & Defense

- **Packet filtering** – Checks IP/port headers
- **Stateful inspection** – Tracks connection state
- **WAF (Web Application Firewall)** – Layer 7 protection
- **IDS/IPS** – Detects/prevents intrusions
  - Snort, Suricata (open source)
  - Zeek for network analysis

---

*Next: Practice Wireshark packet captures, run Nmap scans in a lab environment.*
