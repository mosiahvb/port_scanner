# test IP: 54.149.241.98
from connect import is_ip_valid ,dns_resolution, perform_scan 
from vulner import use_nvd_api
import os

# Next steps create a GUI and add the data to a sqlite3 database for future resurch

api_key = os.getenv("NVD_API_KEY") # calls and hold my API key 

def main():
    running = True
    while running:
        print()
        print('Welcome to the Port scanner!')
        print('----MENU----')
        print('1. Scan Port or Domain')
        print('Please pick from the MENU options "1"')
        choice = int(input(': '))
        if choice == 1:
            print('Enter a IP address or domain name')
            ip = input(': ')

            # This checks to make sure the entry fits the IPv4 address format
            if not is_ip_valid(ip):
                # If it's not an IP address, but it's a domain this performs 
                # the DNS resolution to retrieve the IP address.
                ip = dns_resolution(ip)
                if not ip:
                    print(ip)
                    print('invalid entry, this is not an IP or a domain')
            else:
                print(ip)

            # Performs the scan using NMAP, Collecting and presenting data, 
            # such as port number, the services providing the virgin type, 
            # if available.
            print('----Scanning----')
            rezolts = perform_scan(ip)
            for i in rezolts:
                # print(i)
                port = i['port']
                service = i['service']
                version = i['version']

                print(f'OPEN - Port:{port} - Service:{service} - Version:{version}')

                # Takes the information collected and runs it through the NVD database 
                # for known CVE's For that open port, service and version 
                cves = use_nvd_api(service, version,api_key)
                if cves:
                    for cve in cves:
                        print(f'  - Vulnerability: {cve}')
                else:
                    print('  - No CVEs found')
            print('----Scan Complete----')
            print()
            print('--Would you like to end this session or scan agian? y/n--')
            stop = input(': ').lower()
            if stop == 'y':
                running = False
            else:
                print('Lets go again!')
                print('\n' * 10)

        else:
            print('Invalid entry try again, Example: 1')
            print('\n' * 5)

if __name__ == '__main__':
    main()