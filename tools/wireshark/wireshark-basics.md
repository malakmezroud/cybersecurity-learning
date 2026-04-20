# Wireshark Basics

> **Topic:** Network Traffic Analysis  
> **Date:** April 2026  
> **Status:** ⏳ In Progress

## What is Wireshark?

Wireshark is a free, open-source **packet analyzer** (network sniffer). It captures network traffic in real-time and lets you inspect individual packets at every OSI layer.

**Key cybersecurity uses:**
- Analyzing suspicious traffic
- Detecting unencrypted credentials in transit
- Investigating potential malware/C2 communication
- Learning how protocols actually work at the packet level

---

## Essential Display Filters

```wireshark
# By protocol
http
dns
tcp
udp
icmp

# By IP
ip.addr == 192.168.1.1
ip.src == 10.0.0.5
ip.dst == 8.8.8.8

# By port
tcp.port == 80
udp.port == 53

# HTTP method
http.request.method == "GET"
http.request.method == "POST"

# Combine
ip.addr == 192.168.1.1 && tcp.port == 443
http || dns
```

---

## Red Flags to Look for (SOC Context)

| Indicator | What it Could Mean |
|---|---|
| HTTP POST with credentials | Unencrypted login — credential theft risk |
| Unusual DNS queries to unknown domains | C2 (command & control) communication |
| Large outbound transfers | Data exfiltration |
| Many SYN packets, no ACK | Port scan or SYN flood attack |
| Excessive ARP broadcasts | ARP scan or ARP poisoning |

---

## Practice Checklist

- [ ] Capture HTTP traffic and find plaintext credentials
- [ ] Filter and analyze DNS queries
- [ ] Follow a TCP stream (right-click > Follow > TCP Stream)
- [ ] Identify a port scan in a .pcap file
- [ ] Analyze a sample .pcap from [Wireshark Wiki](https://wiki.wireshark.org/SampleCaptures)

---

*Resources: Wireshark docs, TryHackMe Wireshark rooms*
