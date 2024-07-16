import socket
import sys
import argparse
import subprocess
from colorama import init, Fore, Style

init(autoreset=True)

def check_domain_availability(domain):
    try:
        socket.gethostbyname(domain)
        return True
    except socket.error:
        return False

def generate_variants(domain):
    variants = set()
    for i in range(len(domain)):
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if domain[i] != c:
                variants.add(domain[:i] + c + domain[i+1:])
    for i in range(len(domain)):
        variants.add(domain[:i] + domain[i+1:])
    for i in range(len(domain) + 1):
        for c in 'abcdefghijklmnopqrstuvwxyz':
            variants.add(domain[:i] + c + domain[i:])
    return variants

def get_whois_info(domain):
    try:
        result = subprocess.run(['whois', domain], capture_output=True, text=True, check=False)
        if result.returncode == 0:
            return result.stdout
        else:
            return None
    except Exception as e:
        return None

def main(base_domain, tld=None, output_file=None):
    if tld:
        tlds = [tld]
    else:
        tlds = ['com', 'net', 'org', 'info', 'biz', 'com.tr']
    
    domain_variants = generate_variants(base_domain)

    all_domains = [f"{base_domain}.{tld}" for tld in tlds] + \
                  [f"{variant}.{tld}" for variant in domain_variants for tld in tlds]

    available_domains = []
    taken_domains = []
    whois_infos = []

    for domain in all_domains:
        available = not check_domain_availability(domain)
        if available:
            available_domains.append(domain)
        else:
            whois_info = get_whois_info(domain)
            taken_domains.append(domain)
            whois_infos.append({'domain': domain, 'whois_info': whois_info})

    print(Fore.CYAN + "\n********** AVAILABLE DOMAINS **********")
    output_lines = ["********** AVAILABLE DOMAINS **********"]
    for domain in available_domains:
        line = f"Domain {domain} is available."
        print(Fore.GREEN + line)
        output_lines.append(line)

    print(Fore.CYAN + "\n********** TAKEN DOMAINS **********")
    output_lines.append("\n********** TAKEN DOMAINS **********")
    for domain in taken_domains:
        line = f"Domain {domain} is taken."
        print(Fore.RED + line)
        output_lines.append(line)

    print(Fore.CYAN + "\n********** WHOIS INFORMATION **********")
    output_lines.append("\n********** WHOIS INFORMATION **********")
    for entry in whois_infos:
        line = f"WHOIS info for {entry['domain']}:\n{entry['whois_info']}"
        print(Fore.YELLOW + line)
        output_lines.append(line)

    if output_file:
        with open(output_file, 'w') as file:
            file.write("\n".join(output_lines))
        print(Fore.CYAN + f"Results saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Domain availability and WHOIS checker.")
    parser.add_argument("-d", "--domain", required=True, help="Base domain name to check.")
    parser.add_argument("-t", "--tld", help="Specific TLD to check.")
    parser.add_argument("-o", "--output", help="Output file to save results.")
    args = parser.parse_args()

    main(args.domain, args.tld, args.output)
