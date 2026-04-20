# Web Application Security

> **Topic:** Web Security Fundamentals
> **Date:** April 2026
> **Status:** 🔄 In Progress

Web applications are the #1 attack surface. Understanding OWASP Top 10 is essential for any security role.

---

## OWASP Top 10 (2021)

| # | Vulnerability | Description |
|---|---|---|
| A01 | Broken Access Control | Users access resources they shouldn't |
| A02 | Cryptographic Failures | Weak/missing encryption |
| A03 | Injection | SQL, OS, LDAP injection attacks |
| A04 | Insecure Design | Missing security controls in design |
| A05 | Security Misconfiguration | Default configs, open cloud storage |
| A06 | Vulnerable Components | Outdated libraries/frameworks |
| A07 | Auth Failures | Weak passwords, broken session mgmt |
| A08 | Software Integrity Failures | Unsigned updates, insecure CI/CD |
| A09 | Logging Failures | Insufficient logging and monitoring |
| A10 | SSRF | Server-Side Request Forgery |

---

## SQL Injection

Attacker injects SQL code into input fields to manipulate the database.

**Example:**
```sql
-- Login form input:
' OR '1'='1

-- Resulting query (bypasses auth):
SELECT * FROM users WHERE username='' OR '1'='1' AND password='';
```

**Prevention:**
- Parameterized queries / prepared statements
- Input validation and sanitization
- Principle of least privilege on DB accounts
- Web Application Firewall (WAF)

---

## Cross-Site Scripting (XSS)

Attacker injects malicious JavaScript into pages viewed by other users.

**Types:**
- **Stored XSS** – Script saved in database, runs for every visitor
- **Reflected XSS** – Script in URL, reflected back to user
- **DOM-based XSS** – Script executes via DOM manipulation

**Prevention:**
- Output encoding (HTML escape user input)
- Content Security Policy (CSP) headers
- HttpOnly and Secure cookie flags

---

## Cross-Site Request Forgery (CSRF)

Tricks authenticated users into making unintended requests.

**Prevention:**
- CSRF tokens (unique per session/request)
- SameSite cookie attribute
- Check Origin/Referer headers

---

## Security Headers

| Header | Purpose |
|---|---|
| Content-Security-Policy | Restrict script/resource sources |
| X-Frame-Options | Prevent clickjacking |
| Strict-Transport-Security | Force HTTPS |
| X-Content-Type-Options | Prevent MIME sniffing |
| Referrer-Policy | Control referrer info |

---

## Tools for Web Security Testing

- **Burp Suite** – Intercept and modify HTTP requests
- **OWASP ZAP** – Free web app scanner
- **Nikto** – Web server vulnerability scanner
- **SQLMap** – Automated SQL injection testing
- **Gobuster/ffuf** – Directory and file brute forcing

---

*Next: Practice on HackTheBox web challenges and PortSwigger Web Security Academy.*
