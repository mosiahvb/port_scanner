# Contains functions used for Identifying IP addresses and domains,
# and connecting and scanning ports of those IP address is in domains.
import socket
import nmap

def is_ip_valid(ip):
    '''
    Takes in a input of "ip" and check if it fits within 
    a Valid IPv4 address template (0-255.0-255.0-255.0-255)
    '''
    try:
        socket.inet_aton(ip) # Checks to see if the IP V4 format is correct
        # print('ITS A IP!') - for testing
        return True 
    except socket.error: # Handles error prevents program from crashing 
        # print('not an ip!') - for testing
        return False  


def dns_resolution(domain_name):
    '''
    Performs DNS resolution, Putting the domain name to a IP address,
    From google.com -> 142.251.211.238
    '''
    try:
        ip = socket.gethostbyname(domain_name) # Takes the domain name and find the IP address if it exists (through DNS resolutionthrough DNS resolution)
        print(f'the ip of {domain_name} is: {ip}')
        return ip
    except socket.gaierror: # Handles the errer of the DNS resolution
        return None


def perform_scan(ip):
    '''
    Uses nmap to scan open ports on the "ip" address designated
    collects the service the port provides and the version if available,
    then returns the list of dictionary's with the findings for later use.  
    '''
    scanner = nmap.PortScanner() # Creating the scanner object throug nmap
    scanner.scan(ip, arguments='-sV -p 22,80,443')# <--- FOR TESTING (-p 22,80,443) # Specifies scanning the IP address and collecting the service version of the open port
    # For testing purposes, I designated specific ports to check (to reduce loading times)

    findings = [] # Contains the findings of the port scan in a list of dictionary's
    for protocol in scanner[ip].all_protocols(): # Identifies which protocol that can connect to tcp udp
        print(protocol)
        for port in scanner[ip][protocol]: # iterates through all ports detected as open under the given protocol 
            service = scanner[ip][protocol][port].get('name', 'unknown') # Collects the name running on the port, and presents Unknown if not Identified. 
            version = scanner[ip][protocol][port].get('version', '') # Collects the version of the service if Available 
            findings.append({ # all information is saved to the findings List of dictionary's  
                'port': port,
                'service': service,
                'version': version
            })
    
    return findings

