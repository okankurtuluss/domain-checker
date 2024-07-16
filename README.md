# Domain Availability and WHOIS Checker
This script checks the availability of domain names and retrieves WHOIS information for the specified domains. It supports checking multiple TLDs and generates variations of the given domain name to identify possible typosquatting.

## Requirements
Python 3.x

The following Python libraries:

colorama
argparse

You can install the required libraries using pip:
pip install colorama argparse

## Usage
Run the script with the base domain name as an argument. You can also specify a specific TLD to check and an output file to save the results.

-d or --domain (required): Base domain name to check.
-t or --tld (optional): Specific TLD to check (e.g., com, net, org, etc.). If not specified, the script checks multiple common TLDs (com, net, org, info, biz, com.tr).
-o or --output (optional): Output file to save results.

Check the availability of the domain targetdomain across multiple TLDs:
python script.py -d targetdomain

Check the availability of the domain targetdomain with the specific TLD .com:
python script.py -d targetdomain -t com

Save the results to a file named results.txt:
python script.py -d targetdomain -o results.txt

Check the availability of the domain targetdomain with the specific TLD .com and save the results to a file named results.txt:
python script.py -d targetdomain -t com -o results.txt

## Notes
The script uses the whois command-line tool to fetch WHOIS information. Ensure that the whois tool is installed on your system.





