#!/usr/bin/env python3
"""
Port Scanner - Basic TCP Port Scanner
Author: Malak Mezroud
Description: Scans a target host for open TCP ports within a specified range.
             For educational purposes only. Only scan systems you own or have permission to scan.
"""

import socket
import sys
import argparse
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed


def scan_port(host: str, port: int, timeout: float = 1.0) -> tuple[int, bool, str]:
    """
    Attempt to connect to a specific port on the target host.
    Returns: (port, is_open, service_name)
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "unknown"
            return (port, True, service)
        return (port, False, "")
    except socket.error:
        return (port, False, "")


def resolve_host(host: str) -> str:
    """Resolve hostname to IP address."""
    try:
        return socket.gethostbyname(host)
    except socket.gaierror:
        print(f"[!] Could not resolve hostname: {host}")
        sys.exit(1)


def scan_target(host: str, start_port: int, end_port: int, threads: int = 100, timeout: float = 1.0):
    """
    Scan a range of ports on the target host using threading for speed.
    """
    ip = resolve_host(host)
    print(f"\n{'='*55}")
    print(f"  Port Scanner - by Malak Mezroud")
    print(f"{'='*55}")
    print(f"  Target    : {host} ({ip})")
    print(f"  Ports     : {start_port} - {end_port}")
    print(f"  Threads   : {threads}")
    print(f"  Started   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*55}\n")

    open_ports = []
    ports = range(start_port, end_port + 1)

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(scan_port, ip, port, timeout): port for port in ports}

        for future in as_completed(futures):
            port, is_open, service = future.result()
            if is_open:
                open_ports.append((port, service))
                print(f"  [+] Port {port:5d}/tcp  OPEN   ({service})")

    open_ports.sort(key=lambda x: x[0])

    print(f"\n{'='*55}")
    print(f"  Scan complete. {len(open_ports)} open port(s) found.")
    print(f"  Finished  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*55}\n")

    return open_ports


def main():
    parser = argparse.ArgumentParser(
        description="Simple TCP Port Scanner for educational purposes",
        epilog="Example: python port_scanner.py -t 192.168.1.1 -p 1-1024"
    )
    parser.add_argument("-t", "--target", required=True, help="Target host (IP or hostname)")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port range (e.g. 1-1024 or 80,443,8080)")
    parser.add_argument("--threads", type=int, default=100, help="Number of threads (default: 100)")
    parser.add_argument("--timeout", type=float, default=1.0, help="Connection timeout in seconds (default: 1.0)")

    args = parser.parse_args()

    # Parse port range
    if "-" in args.ports:
        start, end = args.ports.split("-")
        start_port, end_port = int(start), int(end)
    elif "," in args.ports:
        ports_list = [int(p) for p in args.ports.split(",")]
        start_port, end_port = min(ports_list), max(ports_list)
    else:
        start_port = end_port = int(args.ports)

    if not (0 < start_port <= 65535 and 0 < end_port <= 65535):
        print("[!] Port range must be between 1 and 65535")
        sys.exit(1)

    scan_target(args.target, start_port, end_port, args.threads, args.timeout)


if __name__ == "__main__":
    main()
