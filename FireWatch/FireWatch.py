#!/usr/bin/env python3
# File name   : Firewatch.py
# Tool name   : FireWatch
# Author      : Zachary Longo
# Version     : V2.1
# Licence     : MIT
# Script Info 


# Py Libraries
import pandas as pd
import re
import whois
import socket
import requests
import time
import sys
# import readline
import json
from pprint import pprint
from pycrtsh import Crtsh
from dateutil.parser import parse
from requests import get



class MyCrtsh:
    def search(self, query, timeout=None):
        """
        Search crt.sh with the give query
        Query can be domain, sha1, sha256...
        """
        r = requests.get('https://crt.sh/', params={'q': query, 'output': 'json'}, timeout=timeout)
        nameparser = re.compile("([a-zA-Z]+)=(\"[^\"]+\"|[^,]+)")
        certs = []
        try:
            for c in r.json():
                if not c['entry_timestamp']:
                    continue
                certs.append({
                    'id': c['id'],
                    'logged_at': parse(c['entry_timestamp']),
                    'not_before': parse(c['not_before']),
                    'not_after': parse(c['not_after']),
                    'name': c['name_value'],
                    'ca': {
                        'caid': c['issuer_ca_id'],
                        'name': c['issuer_name'],
                        'parsed_name': dict(nameparser.findall(c['issuer_name']))
                    }
                })
        except json.decoder.JSONDecodeError:
            pass
        return certs


# FireWatch Banner
print("""\033[0;31m
 (                                                    
 )\ )                 (  (               )         )  
(()/(  (   (      (   )\))(   '    )  ( /(      ( /(  
 /(_)) )\  )(    ))\ ((_)()\ )  ( /(  )\()) (   )\()) 
(_))_|((_)(()\  /((_)_(())\_)() )(_))(_))/  )\ ((_)\  
| |_   (_) ((_)(_))  \ \((_)/ /((_)_ | |_  ((_)| |(_) 
| __|  | || '_|/ -_)  \ \/\/ / / _` ||  _|/ _| | ' \  
|_|    |_||_|  \___|   \_/\_/  \__,_| \__|\__| |_||_| 
                                                      
\033[0m\033[0;33m 
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Improved and Repackaged by Zachary Longo
    https://github.com/zacharylongo
    
    Original Skeleton derived from: CentralIntelAgency
    

  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  \033[0:33m""")

time.sleep(3)

# Display Feature List
def display_feature_list():
    print("🔥 Domain Registration 🔥"
          "\n🔥 Domain IP and Data 🔥"
          "\n🔥 IP Search (Duplicate IP scan) 🔥"
          "\n🔥 FDNS Records 🔥"
          "\n🔥 Whois Domain Information 🔥"
          "\n🔥 Domain CERT scan (Certificate Information) 🔥"
          "\n🔥 Domain Reputation 🔥"
          "\n🔥 Subdomain scan 🔥"
          "\n🔥 Historical Whois Data 🔥")


with open('config.json', 'r') as f:
    config = json.load(f)

WHOIS_XML_API_KEY = config['WHOIS_XML_API_KEY']
HACKERTARGET_API_KEY = config['HACKERTARGET_API_KEY']
WHOIS_FREAKS_API_KEY = config['WHOIS_FREAKS_API_KEY']

import json

def update_config(config_file='config.json', default_config_file='default_config.json'):
    # Load config.json and default_config.json
    with open(config_file, 'r') as f:
        config = json.load(f)
        
    with open(default_config_file, 'r') as f:
        default_config = json.load(f)
        
    # Check if config matches default_config
    if config == default_config:
        print("Config file matches default configuration.")
        # Prompt user for API keys
        config['WHOIS_XML_API_KEY'] = input("Enter WHOIS XML API key: ")
        config['HACKERTARGET_API_KEY'] = input("Enter HackerTarget API key: ")
        config['WHOIS_FREAKS_API_KEY'] = input("Enter WHOIS Freaks API key: ")
        # Optionally add more keys as needed
        # Save updated config to config.json
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=4)
        print("Config updated successfully.")
    else:
        print("Config file is customized. Confirm if it's good to go.")

# Call the function
update_config()


# Registration Check
def registrationstatus(domain_name):
    """
    Checking whether the domain is registered or not
    """

    try:
        dn = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(dn.domain_name)

        # User input to open Feature List
option = input("\nEnter 'FL' to open Feature List or press 'Enter' to continue. ")
if option == "FL":
    display_feature_list()


print("\nVerifying Domain Registration...")
query = input("\n\033[0;33m\033[1mDomain Name: \033[0m")
domain = query
print(domain, "\033[0;33m...scouring for domain registration\n")
print(domain, "\033[0;33m\033[1m is registered ✅ \033[0m" if registrationstatus(
    domain) else "\033[0;33m\033[1m is not registered ❌ \033[0m")


# Fetch domain IP Address
def domain_ip():
    """
    Find Domain ip address
    """

    website = query
    try:
        domain_ip = socket.gethostbyname(website)

    except Exception as e:
        return


    print("\n\033[0;33m\033[1mDomain IP: \033[1m\033[0;32m\n")
    print(domain_ip)

    ip_address = domain_ip
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    print("\n\033[0;33m\033[1mIP Data:\n\033[0m\033[0;32m")
    pprint(response)

    print("\n\n\033[0;33m\033[1mDouble IP verification using IPinfo.io")
    print("\n\033[0;33m\033[1mResults:\033[0m\033[0;32m")

    response = requests.get(f'https://ipinfo.io/{ip_address}/json')
    data = json.loads(response.text)

    ip = data['ip']
    organization = data['org']
    city = data['city']
    region = data['region']
    country = data['country']
    location = data['loc']
    postal = data['postal']
    timezone = data['timezone']

    print("ip:", ip)
    print("organization:", organization)
    print("city:", city)
    print("region:", region),\
    print("country:", country)
    print("postal:", postal)
    print("location:", location)
    print("timezone", timezone)

    choice = input("\n\n\033[0;33m\033[1mExtract domains with the same IP?\033[0m y/n: ")
    if choice == "y" or choice == "Y":
        rev_ip(domain_ip, website)
    if choice == "n" or choice == "N":
        dns_records(website)
    else:
        print("Bad Input; choose Y or N, and start over")
        sys.exit(1)


# Reverse IP lookup
def rev_ip(domain_ip, domain):
    """
    Choose Reverse ip for free or with your API
    """

    print(
        "\n\n\033[1m!!! Hacker Target provides trial queries, however advanced/bulk searches will require subscription.\033[0m")

    choice = input(
        """\n\033[0;33m\033[1mType -F for Free Search, or Type -API for usage with your own API Key: \033[0m""")
    if choice == "-F" or choice == "-f" or choice == "F" or choice == "f":
        rev_ip_free(domain_ip, domain)
    if choice == "-API" or choice == "-api" or choice == "API" or choice == "api":
        rev_ip_api(domain_ip, domain)

    else:
        print(
            "Bad Input; Select -F for free search or -API for usage with your API Key, please start over")
        sys.exit(1)


# Free reverse IP fetch
def rev_ip_free(domain_ip, domain):
    print("\n\033[0;32mPlease be patient ...checking Hackertarget.com status\033[0m")
    URL = 'http://api.hackertarget.com/reverseiplookup'
    request = requests.get(URL)

    print(f"\n\033[0;32mstatus code {request.status_code}!\033[0m Hacker Target is \033[0;32m\033[1monline\033[0m\033[0;33m\033[1m\n\nReverse IP search results:\033[0m\033[0;32m\n") if request.status_code == 200 else print('\033[0;32mResponse Failed, try again later')

    response = requests.get("http://api.hackertarget.com/reverseiplookup", params={"q": domain_ip})
    print(response.text)

    choice = input("\n\n\033[0;33m\033[1mContinue to DNS Records search?\033[0m y/n: ")
    if choice.lower() == "y": dns_records(domain)
    elif choice.lower() == "n": whois_search()
    else: print("Bad Input; choose Y or N, please start over"); sys.exit(1)


# Premium Lookup
def rev_ip_api(domain_ip, domain):
    """
    Reverse IP search with API
    """

    # Returning and printing the status code (200 means the server was reached).
    print("\n\033[0;32mOne moment ...checking Hackertarget.com status\033[0m")
    URL = 'http://api.hackertarget.com/reverseiplookup'

    request = requests.get(URL)
    if request.status_code == 200:
        print(
            "\n\n\033[0;32mstatus code 200!\033[0m Hacker Target is \033[0;32m\033[1monline\033[0m\033[0;33m\033[1m\n\nReverse IP search results:\033[0m\033[0;32m\n")

    else:
        print('\033[0;32mResponse Failed, try again later')

    # Using your own Hacker Target API to avoid restrictions
    query = domain_ip
    domain_ip = {"q": query}
    api = f"https://api.hackertarget.com/reverseiplookup/?q={query}&apikey={HACKERTARGET_API_KEY}"
    response = requests.request("GET", api, params=domain_ip)
    print(response.text)

    choice = input("\n\n\033[0;33m\033[1mContinue to DNS Records search?\033[0m y/n: ")

    if choice == "y" or choice == "Y":
        dns_records(domain)
    if choice == "n" or choice == "N":
        whois_search()

    else:
        print("Bad Input; choose Y or N, please start over")
        sys.exit(1)


# DNS record search
def dns_records(domain):
    """
    Choose Free Search or API
    """

    choice = input(
        """\n\033[0;33m\033[1mType -F for Free Search, or Type -API for usage with your own API Key: \033[0m""")
    if choice == "-F" or choice == "-f" or choice == "F" or choice == "f":
        dns_records_free(domain)
    if choice == "-API" or choice == "-api" or choice == "API" or choice == "api":
        dns_records_api(domain)

    else:
        print(
            "You pressed the wrong key; choose -F for free search or -API for usage with your API Key, please start again")
        sys.exit(1)


# Free DNS Search
def dns_records_free(domain):
    """
    DNS Records check
    """

    print("\n\033[0;33m\033[1mDNS Records search results:\033[0m\033[0;32m\n")
    dnsrecords_api = "https://api.hackertarget.com/dnslookup/"

    dns_records = {"q": domain}
    response = requests.request("GET", dnsrecords_api, params=dns_records)
    print(response.text)

    choice = input("\n\n\033[0;33m\033[1mDo a Whois scan? y/n: \033[0m")
    if choice == "y" or choice == "Y":
        whois_search()
    if choice == "n" or choice == "N":
        sys.exit(1)

    else:
        print("Bad Input; choose Y or N, please start over")
        sys.exit(1)


# DNS Records using Subscription
def dns_records_api(domain):
    """
    DNS Records check with API
    """
    print("\n\033[0;33m\033[1mDNS Records search results:\033[0m\033[0;32m\n")
    dns_records = {"q": domain}
    api = f"https://api.hackertarget.com/dnslookup/?q={domain}&apikey={HACKERTARGET_API_KEY}"
    response = requests.request("GET", api, params=dns_records)
    print(response.text)

    choice = input("\n\n\033[0;33m\033[1mDo a Whois scan? y/n: \033[0m")
    if choice == "y" or choice == "Y":
        whois_search()
    if choice == "n" or choice == "N":
        sys.exit(1)

    else:
        print("Bad Input; choose Y or N, please start over")
        sys.exit(1)


# Extended search using WhoIS
def whois_search():
    """
    WHOis information search
    """

    print("\n\n\033[0;33m\033[1mLets take a deeper look....\033[0m")
    webdomain = query
    domain_name = webdomain
    whois_information = whois.whois(domain_name)

    # Results.
    print("\n\033[0;32mDomain Name:", whois_information.domain_name)
    print("\nDomain registrar:", whois_information.registrar)
    print("\nWHOis server:", whois_information.whois_server)
    print("\nDomain creation date:", whois_information.creation_date)
    print("\nExpiration date:", whois_information.expiration_date)
    print("\nUpdated Date:", whois_information.updated_date)
    print("\nServers:", whois_information.name_servers)
    print("\nStatus:", whois_information.status)
    print("\nEmail Addresses:", whois_information.emails)
    print("\nName:", whois_information.name)
    print("\nOrg:", whois_information.org)
    print("\nAddress:", whois_information.address)
    print("\nCity:", whois_information.city)
    print("\nState:", whois_information.state)
    print("\nZipcode:", whois_information.zipcode)
    print("\nCountry:", whois_information.country)

    # Slow down for readability
    time.sleep(3)

    choice = input("\n\n\033[0;33m\033[1mCheck domain CERT (Certificate)?\033[0m y/n: ")
    if choice == "Y" or choice == "y":
        crt_sh(domain_name)
    if choice == "N" or choice == "n":
        domain_reputation(domain_name)

    else:
        print("Bad Input; choose Y or N, please start over")
        sys.exit(1)


# CRT.SH Certificate Search
def crt_sh(domain_name):
    c = MyCrtsh()
    certs = c.search(domain_name)
    print("\n\033[0;33m\033[1mWebsite cert. search results:\033[0m\n\033[0;32m")
    pprint(certs[:6])

    time.sleep(3)

    choice = input("\n\n\033[0;33m\033[1mDomain reputation scan?\033[0m y/n: ")
    if choice == "Y" or choice == "y":
        domain_reputation(domain_name)
    if choice == "N" or choice == "n":
        print("\n\n\n\033[0;33m\033[1mLooks like you're burnt out... that's it for now.")
        sys.exit(1)

    else:
        print("Bad Input; choose Y or N, please start over")
        sys.exit(1)


# Domain Reputation Scan
def domain_reputation(domain_name):
    """
    Domain reputation scan
    """

    print("\n\033[0;33m\033[1mOK! Domain reputation scan using WhoisXML API\n\033[0m")

    query = domain_name
    reputation = {"q": query}
    api = f"https://domain-reputation.whoisxmlapi.com/api/v2?apiKey={WHOIS_XML_API_KEY}&domainName={query}"
    response = requests.request("GET", api, params=reputation)

    print("\n\n\033[0;33m\033[1mDomain Reputation check results:\n\n\033[0;32m")
    pprint(response.text)

    time.sleep(3)

    choice = input("\n\n\033[0;33m\033[1mReady for a subdomain scan?\033[0m y/n: ")
    if choice == "Y" or choice == "y":
        subdomain_scanner(domain_name)
    if choice == "N" or choice == "n":
        whois_history(domain_name)


# Subdomain Scan
def subdomain_scanner(domain_name):
    """
    Subdomain scan
    """

    subdomains_found = []

    sdsreq = requests.get(f'https://crt.sh/?q={domain_name}&output=json')

    if sdsreq.status_code == 200:
        print('\033[0;32m\033[1m\n\nScanning for subdomains now...')

    else:
        print("\033[0;32mThe subdomain scanner tool is currently offline, try again later.\033[0m")
        sys.exit(1)

    for (key, value) in enumerate(sdsreq.json()):
        subdomains_found.append(value['name_value'])

    print(
        f"\n\n\033[0;33m\033[1mYour chosen targeted Domain for the Subdomain scan:\033[0;32m{domain_name}\033[0m\033[0;32m\n")

    subdomains = sorted(set(subdomains_found))

    for sub_link in subdomains:
        print(f'\033[1m[✅ Subdomain Found]\033[0m\033[0;32m -->{sub_link}')

    print("\n\033[1m\033[0;33m\033[1mSubdomain Scan Completed!  \033[0;32m\033[1m- ALL Subdomains have been Found")

    time.sleep(3)

    choice = input("\n\n\033[0;33m\033[1mLast Run a Whois History search?\033[0m y/n: ")
    if choice == "Y" or choice == "y":
        whois_history(domain_name)
    if choice == "N" or choice == "n":
        print("\n\n\n\033[0;33m\033[1mLooks like you're burnt out... that's it for now.")
        sys.exit(1)


#  WhoisFreaks Whois History
def whois_history(domain_name):
    """
    Whois History search
    """

    print("\n\033[0;33m\033[1mOK Fetching historical WhoIS data...\n\033[0m")

    time.sleep(2)

    print("\n\033[0;33m\033[1mHistorical Whois results:\n\n\033[0;32m")

    query = domain_name
    whoishistory = {"q": query}
    api = f"https://api.whoisfreaks.com/v1.0/whois?apiKey={WHOIS_FREAKS_API_KEY}&whois=historical&domainName={query}"
    response = requests.request("GET", api, params=whoishistory)
    pprint(response.text)

    time.sleep(3)

    # Termination Message
    print("\n\n\n\033[0;33m\033[1m Looks like you're burnt out... that's it for now.")
    sys.exit(1)


# Dig/No Dig
choice = input("""\n\n\033[0;33m\033[1mFind domain IP?\033[0m  y/n: """)
if choice == "Y" or choice == "y":
    domain_ip()
if choice == "N" or choice == "n":
    dns_records(query)
else:
    print("\n\n\033[0;31m\033[1mDomain IP not found for:")
    print(domain)
    print("\033[0;32mThis means that you will now be taken straight to the Reverse DNS search module...")
    dns_records(domain)


# Main
def main():
    registrationstatus()
    domain_ip()
    rev_ip()
    rev_ip_free()
    rev_ip_api()
    dns_records()
    dns_records_free()
    dns_records_api()
    whois_search()
    crt_sh()
    domain_reputation()
    subdomain_scanner()
    whois_history()


if __name__ == '__main__':
    main()
