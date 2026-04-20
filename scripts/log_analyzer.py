#!/usr/bin/env python3
"""
log_analyzer.py

A simple Python script to analyze Linux auth logs for suspicious activity.
Practice script for cybersecurity learning - SOC / log analysis skills.

Author: Nor Malak Mezroud
Date: April 2026

Usage:
    python3 log_analyzer.py --file /var/log/auth.log
    python3 log_analyzer.py --file sample_auth.log --top 10
"""

import argparse
import re
from collections import Counter
from datetime import datetime


def parse_args():
    parser = argparse.ArgumentParser(
        description="Analyze auth.log for failed SSH logins and suspicious IPs"
    )
    parser.add_argument(
        "--file", required=True, help="Path to the auth log file (e.g. /var/log/auth.log)"
    )
    parser.add_argument(
        "--top", type=int, default=5, help="Number of top offending IPs to show (default: 5)"
    )
    return parser.parse_args()


def find_failed_logins(log_file):
    """
    Parse the log file and extract failed SSH login attempts.
    Returns a list of (timestamp, ip_address, username) tuples.
    """
    failed_logins = []

    # Pattern for failed password attempts in auth.log
    # Example: Apr 19 22:01:15 server sshd[1234]: Failed password for root from 192.168.1.100 port 22 ssh2
    pattern = re.compile(
        r"(\w+\s+\d+\s+\d+:\d+:\d+).*Failed password for (\S+) from (\d+\.\d+\.\d+\.\d+)"
    )

    try:
        with open(log_file, "r") as f:
            for line in f:
                match = pattern.search(line)
                if match:
                    timestamp = match.group(1)
                    username = match.group(2)
                    ip_address = match.group(3)
                    failed_logins.append((timestamp, ip_address, username))
    except FileNotFoundError:
        print(f"[ERROR] File not found: {log_file}")
        return []
    except PermissionError:
        print(f"[ERROR] Permission denied: {log_file} (try running with sudo)")
        return []

    return failed_logins


def analyze(failed_logins, top_n=5):
    """
    Analyze the failed logins and print a summary report.
    """
    if not failed_logins:
        print("[INFO] No failed login attempts found.")
        return

    total = len(failed_logins)
    ip_counts = Counter(ip for _, ip, _ in failed_logins)
    user_counts = Counter(user for _, _, user in failed_logins)

    print("=" * 60)
    print("          SSH FAILED LOGIN ANALYSIS REPORT")
    print("=" * 60)
    print(f"Total failed login attempts : {total}")
    print(f"Unique IPs attacking        : {len(ip_counts)}")
    print(f"Unique usernames targeted   : {len(user_counts)}")
    print()

    print(f"--- Top {top_n} Attacking IP Addresses ---")
    for ip, count in ip_counts.most_common(top_n):
        bar = "#" * min(count, 40)
        flag = "  <-- BRUTE FORCE LIKELY" if count >= 10 else ""
        print(f"  {ip:<20} {count:>5} attempts  {bar}{flag}")
    print()

    print(f"--- Top {top_n} Targeted Usernames ---")
    for user, count in user_counts.most_common(top_n):
        print(f"  {user:<20} {count:>5} attempts")
    print()

    # Show the most recent 5 attempts
    print("--- Most Recent Failed Attempts ---")
    for timestamp, ip, user in failed_logins[-5:]:
        print(f"  [{timestamp}]  IP: {ip:<18}  User: {user}")
    print("=" * 60)

    # Simple threshold alert
    top_ip, top_count = ip_counts.most_common(1)[0]
    if top_count >= 10:
        print(f"\n[ALERT] Possible brute force attack detected!")
        print(f"        IP {top_ip} had {top_count} failed attempts.")
        print(f"        Recommend: block with 'sudo ufw deny from {top_ip}'")


if __name__ == "__main__":
    args = parse_args()
    print(f"\n[*] Analyzing log file: {args.file}")
    print(f"[*] Showing top {args.top} results\n")

    failed = find_failed_logins(args.file)
    analyze(failed, top_n=args.top)
