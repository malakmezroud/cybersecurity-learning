# The OSI Model

> **Topic:** Networking Fundamentals  
> **Date:** April 2026  
> **Status:** ✅ Complete

## What is the OSI Model?

The OSI (Open Systems Interconnection) model is a conceptual framework that standardizes how different network protocols communicate. It splits network communication into **7 layers**, each with a specific role.

Understanding OSI is foundational for cybersecurity — it helps identify *where* attacks happen and *which tools/defenses* apply.

---

## The 7 Layers

| Layer | Name | Protocol Examples | Key Function |
|---|---|---|---|
| 7 | Application | HTTP, HTTPS, DNS, FTP, SMTP | End-user interface; where apps communicate |
| 6 | Presentation | SSL/TLS, JPEG, ASCII | Data formatting, encryption, compression |
| 5 | Session | NetBIOS, RPC | Manages sessions/connections between devices |
| 4 | Transport | TCP, UDP | End-to-end delivery, port numbers, segmentation |
| 3 | Network | IP, ICMP, ARP | Logical addressing (IP), routing between networks |
| 2 | Data Link | Ethernet, Wi-Fi (802.11), MAC | Physical addressing (MAC), frames, switches |
| 1 | Physical | Cables, radio waves, hubs | Raw binary transmission over physical medium |

**Memory trick:** *"Please Do Not Throw Sausage Pizza Away"* (Physical, Data Link, Network, Transport, Session, Presentation, Application)

---

## Why It Matters for Cybersecurity

- **Layer 3 (Network):** IP spoofing, ICMP attacks (ping flood), routing attacks
- **Layer 4 (Transport):** Port scanning (Nmap), SYN flood DoS attacks, TCP hijacking
- **Layer 6 (Presentation):** SSL/TLS vulnerabilities, weak encryption
- **Layer 7 (Application):** SQL injection, XSS, phishing, DNS poisoning, HTTP attacks
- **Layer 2 (Data Link):** ARP poisoning/spoofing, MAC flooding

---

## TCP vs UDP (Layer 4)

| Feature | TCP | UDP |
|---|---|---|
| Connection | Connection-oriented (3-way handshake) | Connectionless |
| Reliability | Guaranteed delivery | Best-effort |
| Speed | Slower | Faster |
| Use cases | HTTP, SSH, FTP, email | DNS, VoIP, video streaming |
| Attack relevance | SYN flood, TCP hijacking | UDP flood, DNS amplification |

---

## Common Port Numbers

| Port | Protocol | Notes |
|---|---|---|
| 21 | FTP | File transfer (unencrypted) |
| 22 | SSH | Secure remote shell |
| 23 | Telnet | Insecure (avoid!) |
| 53 | DNS | Domain name resolution |
| 80 | HTTP | Web (unencrypted) |
| 443 | HTTPS | Web (TLS encrypted) |
| 3306 | MySQL | Database |
| 3389 | RDP | Windows remote desktop |

---

*Source: Personal study notes + Cisco NetAcad, TryHackMe Pre-Security path*
