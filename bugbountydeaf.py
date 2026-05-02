#!/usr/bin/env python3

import os
import argparse
import subprocess
import requests

# ================= TITLE =================
def set_terminal_title():
    os.system("printf '\033]0;BUG BOUNTY DEAF\007'")

# ================= BANNER =================
def banner():
    print("""
██████╗ ██╗   ██╗ ██████╗     ██████╗  ██████╗  ██████╗ ██╗   ██╗████████╗██╗   ██╗
██╔══██╗██║   ██║██╔════╝     ██╔══██╗██╔═══██╗██╔═══██╗██║   ██║╚══██╔══╝╚██╗ ██╔╝
██████╔╝██║   ██║██║  ███╗    ██████╔╝██║   ██║██║   ██║██║   ██║   ██║    ╚████╔╝ 
██╔══██╗██║   ██║██║   ██║    ██╔══██╗██║   ██║██║   ██║██║   ██║   ██║     ╚██╔╝  
██████╔╝╚██████╔╝╚██████╔╝    ██████╔╝╚██████╔╝╚██████╔╝╚██████╔╝   ██║      ██║   
╚═════╝  ╚═════╝  ╚═════╝     ╚═════╝  ╚═════╝  ╚═════╝  ╚═════╝    ╚═╝      ╚═╝   

                BUG BOUNTY DEAF - RECON AUTOMATION TOOL
    """)

# ================= RUN COMMAND =================
def run(cmd, output=None):
    try:
        if output:
            with open(output, "w") as f:
                subprocess.run(cmd, stdout=f, stderr=subprocess.DEVNULL)
        else:
            subprocess.run(cmd)
    except FileNotFoundError:
        print(f"[-] Tool missing: {cmd[0]}")

# ================= SUBDOMAINS =================
def subdomains(domain, out):
    print("[+] Subdomain enumeration (Subfinder + Amass)")
    run(["subfinder", "-d", domain, "-silent"], out)
    run(["amass", "enum", "-passive", "-d", domain], out)

# ================= LIVE HOSTS =================
def live_hosts(input_file, out):
    print("[+] Checking live hosts (httpx)")
    run(["httpx", "-l", input_file, "-silent"], out)

# ================= WAYBACK =================
def wayback(domain, out):
    print("[+] Collecting Wayback URLs")
    url = f"https://web.archive.org/cdx/search/cdx?url=*.{domain}/*&output=text&fl=original&collapse=urlkey"
    try:
        r = requests.get(url, timeout=10)
        with open(out, "w") as f:
            f.write(r.text)
    except:
        print("[-] Wayback failed")

# ================= FILTER =================
def filter_juicy(file_in, file_out):
    keywords = ["api", "admin", "login", "upload", "auth", "redirect"]
    results = []

    try:
        with open(file_in, "r") as f:
            for line in f:
                if any(k in line.lower() for k in keywords):
                    results.append(line.strip())
    except:
        pass

    with open(file_out, "w") as f:
        f.write("\n".join(results))

# ================= MAIN =================
def main():
    parser = argparse.ArgumentParser(
        prog="bugbountydeaf.py",
        description="Bug Bounty Deaf - Simple Recon Automation Tool"
    )

    parser.add_argument("-d", "--domain", help="Target domain (example.com)")
    parser.add_argument("-o", "--output", default="bbd", help="Output prefix")
    parser.add_argument("--all", action="store_true", help="Run full recon")
    parser.add_argument("--subs", action="store_true", help="Only subdomains")
    parser.add_argument("--live", action="store_true", help="Only live hosts")
    parser.add_argument("--wayback", action="store_true", help="Only wayback URLs")

    args = parser.parse_args()

    set_terminal_title()
    banner()

    if not args.domain:
        print("[-] Please provide a domain with -d")
        return

    subs = f"{args.output}_subs.txt"
    live = f"{args.output}_live.txt"
    way = f"{args.output}_wayback.txt"
    juicy = f"{args.output}_juicy.txt"

    print(f"[+] Target: {args.domain}")

    if args.all or args.subs:
        subdomains(args.domain, subs)

    if args.all or args.live:
        live_hosts(subs, live)

    if args.all or args.wayback:
        wayback(args.domain, way)
        filter_juicy(way, juicy)

    print("\n[+] DONE - Check output files")

# ================= ENTRY =================
if __name__ == "__main__":
    main()
