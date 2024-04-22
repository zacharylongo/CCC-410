import json
import shodan
import pandas as pd
import sys

# Read API key from config.json
with open('config.json', 'r') as f:
    config = json.load(f)
    api_key = config['api_key']

# Function to get host information and save it to an Excel file
def host_info(api_key):
    try:
        api = shodan.Shodan(api_key)
        ip = input("Enter target IP address: ")
        result = api.host(ip)
        
        # Extract relevant information from the result
        ip_str = result.get('ip_str', '')
        hostnames = ', '.join(result.get('hostnames', []))
        org = result.get('org', '')
        location = result.get('location', '')
        ports = ', '.join(str(port.get('port', '')) for port in result.get('data', []))
        
        # Create a DataFrame
        df = pd.DataFrame({
            "IP": [ip_str],
            "Hostname": [hostnames],
            "Organization": [org],
            "Location": [location],
            "Ports": [ports]
        })
        
        # Save the DataFrame to an Excel file
        df.to_excel("host_information.xlsx", index=False)
        
        print("Host information saved to host_information.xlsx")
    except Exception as e:
        print('Error: %s' % e)


def host_count(api_key):
    try:
        api = shodan.Shodan(api_key)
        query = input("Enter search query: ")
        facets = input("Enter facets (optional): ")
        result = api.host_count(query=query, facets=facets)
        print(result)
    except Exception as e:
        print('Error: %s' % e)

def host_search(api_key):
    try:
        api = shodan.Shodan(api_key)
        query = input("Enter search query: ")
        facets = input("Enter facets (optional): ")
        page = input("Enter page number (optional): ")
        minify = input("Enter minify option (optional): ")
        result = api.search(query=query, facets=facets, page=page, minify=minify)
        print(result)
    except Exception as e:
        print('Error: %s' % e)

def domain_info(api_key):
    try:
        api = shodan.Shodan(api_key)
        domain = input("Enter target domain: ")
        history = input("Include historical DNS data? (True/False): ")
        type = input("Enter DNS type (optional): ")
        page = input("Enter page number (optional): ")
        result = api.dns_domain(domain, history=history, type=type, page=page)
        print(result)
    except Exception as e:
        print('Error: %s' % e)

def dns_resolve(api_key):
    try:
        api = shodan.Shodan(api_key)
        hostnames = input("Enter comma-separated list of hostnames: ")
        result = api.dns_resolve(hostnames)
        print(result)
    except Exception as e:
        print('Error: %s' % e)

def dns_reverse(api_key):
    try:
        api = shodan.Shodan(api_key)
        ips = input("Enter comma-separated list of IP addresses: ")
        result = api.dns_reverse(ips)
        print(result)
    except Exception as e:
        print('Error: %s' % e)

def api_info(api_key):
    try:
        api = shodan.Shodan(api_key)
        result = api.info()
        print(result)
    except Exception as e:
        print('Error: %s' % e)

def query_summary(api_key):
    try:
        # Configuration
        FACETS = [
            'org',
            'domain',
            'port',
            'asn',
            ('country', 3),  # Limiting to top 3 countries
        ]

        FACET_TITLES = {
            'org': 'Top 5 Organizations',
            'domain': 'Top 5 Domains',
            'port': 'Top 5 Ports',
            'asn': 'Top 5 Autonomous Systems',
            'country': 'Top 3 Countries',
        }

        # Setup the API
        api = shodan.Shodan(api_key)

        # Get the search query from the user
        query = input("Enter search query: ")

        # Use the count() method because it doesn't return results and doesn't require a paid API plan
        # Also, it runs faster than doing a search()
        result = api.count(query, facets=FACETS)

        # Print summary information
        print("\nShodan Summary Information")
        print("Query: %s" % query)
        print("Total Results: %s\n" % result['total'])

        # Print the summary info from the facets
        for facet in result['facets']:
            print(FACET_TITLES[facet])

            for term in result['facets'][facet]:
                print('%s: %s' % (term['value'], term['count']))

            # Print an empty line between summary info
            print('')

    except Exception as e:
        print('Error: %s' % e)


# Main function to select and execute queries

def main():
    try:

        while True:
            print("\nSelect a query type:")
            print("1. Host Information")
            print("2. Host Count")
            print("3. Host Search")
            print("4. Domain Information")
            print("5. DNS Resolve")
            print("6. DNS Reverse")
            print("7. API Information")
            print("8. Query Summary")
            print("9. Quit")

            choice = input("Enter your choice: ")

            if choice == '1':
                host_info(api_key)
            elif choice == '2':
                host_count(api_key)
            elif choice == '3':
                host_search(api_key)
            elif choice == '4':
                domain_info(api_key)
            elif choice == '5':
                dns_resolve(api_key)
            elif choice == '6':
                dns_reverse(api_key)
            elif choice == '7':
                api_info(api_key)
            elif choice == '8':
                query_summary(api_key)
            elif choice == '9':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 9.")

            another_query = input("Do you want to perform another query? (yes/no): ").lower()
            if another_query != 'yes':
                break
    except Exception as e:
        print('Error: %s' % e)
        sys.exit(1)

if __name__ == "__main__":
    main()