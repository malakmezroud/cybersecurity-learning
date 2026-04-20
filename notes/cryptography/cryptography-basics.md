# Cryptography Basics

> **Topic:** Cryptography Fundamentals  
> **Date:** April 2026  
> **Status:** ⏳ In Progress

Cryptography is the foundation of cybersecurity — it protects data in transit, at rest, and proves identity.

---

## Symmetric Encryption
The **same key** encrypts and decrypts.

| Algorithm | Notes |
|---|---|
| AES-256 | Current gold standard |
| AES-128 | Still secure, faster |
| DES | Broken — never use |

**Use cases:** File encryption, VPN tunnels, disk encryption (BitLocker), database encryption  
**Weakness:** Key distribution — how do you securely share the key?

---

## Asymmetric Encryption (Public Key Cryptography)
Uses a **key pair**: public key (share freely) + private key (keep secret).

| Algorithm | Use Case |
|---|---|
| RSA | Key exchange, signatures |
| ECC | Smaller keys, same strength as RSA |
| Diffie-Hellman | Key exchange protocol |

**Use cases:** HTTPS (TLS handshake), SSH, digital certificates, PGP email  
**Weakness:** Much slower than symmetric — used only to exchange a symmetric key

---

## How HTTPS/TLS Works (Both Combined)

```
1. Server sends public key in certificate
2. Client verifies certificate via trusted CA
3. Client generates random session key
4. Client encrypts session key with server's public key
5. Server decrypts with private key
6. Both now use AES (symmetric) for the session
```

---

## Hashing
A **one-way function** — input → fixed fingerprint. Cannot be reversed.

| Algorithm | Output | Notes |
|---|---|---|
| MD5 | 128-bit | Broken — don't use for security |
| SHA-1 | 160-bit | Deprecated |
| SHA-256 | 256-bit | Current standard |
| bcrypt | Variable | Best for password storage |
| Argon2 | Variable | Modern password hashing |

**Use cases:** Password storage, file integrity checks, digital signatures, blockchain

```python
import hashlib
password = "mypassword123"
hash_result = hashlib.sha256(password.encode()).hexdigest()
print(hash_result)
```

---

## Salting
Random data added to a password before hashing.

- Prevents **rainbow table attacks** (precomputed hash lookups)
- Even if two users have the same password, their hashes will differ

---

## PKI & Certificates

- **CA (Certificate Authority)** — trusted third party that signs certs (DigiCert, Let's Encrypt)
- **Certificate** — public key + identity info, signed by CA
- **Chain of trust** — browser trusts root CA → intermediate CA → server cert

**Security relevance:** Expired/rogue certs are red flags. SSL stripping attacks bypass TLS.

---

## Common Cryptographic Attacks

| Attack | Description |
|---|---|
| Brute force | Try all possible keys |
| Dictionary attack | Try common passwords |
| Rainbow table | Precomputed hashes (defeated by salting) |
| Birthday attack | Find hash collisions (MD5/SHA-1 vulnerable) |
| MITM | Intercept key exchange |

---

*Next: TryHackMe Cryptography rooms, practice Python hashing scripts.*
