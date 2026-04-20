# SOC Fundamentals

> **Topic:** Security Operations Center  
> **Date:** April 2026  
> **Status:** ⏳ In Progress

## What is a SOC?

A **Security Operations Center (SOC)** is a team of cybersecurity professionals who monitor, detect, analyze, and respond to security incidents 24/7.

---

## SOC Analyst Tiers

| Tier | Role |
|---|---|
| Tier 1 | Alert triage — monitors dashboards, filters false positives, escalates |
| Tier 2 | Incident response — deeper investigation, contain/remediate |
| Tier 3 | Threat hunting — proactively finds hidden threats |

**Targeting: Tier 1 SOC Analyst roles as a new grad.**

---

## Daily Tier 1 Workflow

1. Monitor SIEM dashboard for alerts
2. Triage: Is this real or a false positive?
3. Investigate suspicious activity (logs, network, endpoints)
4. Escalate real incidents to Tier 2
5. Document findings

---

## Key SOC Tools

| Tool | Purpose |
|---|---|
| SIEM (Splunk, Sentinel) | Log collection and alerting |
| EDR (CrowdStrike, Defender) | Endpoint detection & response |
| Firewall / IDS / IPS | Block and detect network threats |
| VirusTotal, AbuseIPDB | IOC lookups |
| ServiceNow / JIRA | Incident ticketing |

---

## Key Concepts

**IOC (Indicator of Compromise)** — evidence of a breach:
- Malicious IP addresses or domains
- Known malware file hashes
- Unusual outbound connections

**MITRE ATT&CK** — knowledge base of adversary tactics. Every SOC analyst should know it.
- [attack.mitre.org](https://attack.mitre.org)

**Cyber Kill Chain** (Lockheed Martin):
1. Reconnaissance → 2. Weaponization → 3. Delivery → 4. Exploitation → 5. Installation → 6. C2 → 7. Actions

---

## Common Alert Types

| Alert | Indicators |
|---|---|
| Brute force | Many failed logins from one IP |
| Phishing | Suspicious links/attachments in email |
| Malware execution | Unusual process spawning |
| Data exfiltration | Large unusual outbound transfer |
| Privilege escalation | User gaining admin rights unexpectedly |

---

## SIEM Basics

SIEM collects logs from everywhere, normalizes them, and generates alerts.

**Popular SIEMs:** Splunk, Microsoft Sentinel, IBM QRadar, Elastic SIEM

**Ingests:** Firewall logs, Windows Event Logs, Linux auth logs, application logs, network flows

---

*Next: Splunk free tier practice + TryHackMe SOC Level 1 path.*
