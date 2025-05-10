# Port Scanner

A Python-based network reconnaissance tool designed to identify open ports and known vulnerabilities on a specified domain or IP address. This command-line utility uses DNS resolution, socket communication, `nmap`, and the National Vulnerability Database (NVD) to surface actionable insights about a host's security profile.

---

## What It Is

This is a CLI tool for scanning networks or websites to:

- Resolve domain names to IP addresses using sockets  
- Scan the resolved IP with `nmap` to detect open ports, service types, and versions  
- Query the NVD (National Vulnerability Database) for known CVEs based on open ports and versions  
- Output the findings directly to the user for analysis and remediation  

It's designed for internal security auditing and learning more about network security using Python automation.

---

## Why I Built It

I created this project to:

- Better understand how attackers can identify weaknesses in a network  
- Perform vulnerability scans on my home and company networks  
- Learn how to automate security tasks using Python  
- Get hands-on experience using tools like `nmap` and the NVD API  
- Help my company identify known vulnerabilities in our web infrastructure  

This project also served as a personal deep-dive into how network scanning tools work behind the scenes.

---

## How I Built It

Technologies and libraries used:

- **Python** as the main programming language  
- **Socket** for DNS resolution and IP handling  
- **Nmap (via python-nmap)** for scanning open ports and service versions  
- **Requests** to query the [National Vulnerability Database (NVD)](https://nvd.nist.gov/)  
- **OS** to securely access environment variables (API key stored in `.env` file)  

### Workflow Overview:

1. User inputs a domain name or IP address  
2. Domain is resolved to an IP (if needed)  
3. `nmap` is run against the target IP  
4. Open ports, service names, and version numbers are extracted  
5. The tool queries the NVD for related CVEs  
6. Results are printed to the terminal for review  

---

## Challenges I Faced

- **Choosing the scanning method**: I debated between building a custom scanner using sockets or using `nmap`. I chose `nmap` for its speed, accuracy, and advanced capabilities  
- **Parsing `nmap` output**: Extracting meaningful info required careful parsing  
- **Using the NVD API**: Matching service versions with vulnerabilities took extra effort due to inconsistencies and rate limits  
- **Environment security**: I used a `.env` file and Python's `os` module to manage sensitive keys securely  

---

## Tools & Tech Used

- Python  
- Socket  
- Nmap / python-nmap  
- Requests  
- OS (for system calls)  
- National Vulnerability Database (NVD) API  

---

## What I'd Do Differently

When I expand this tool in the future, I’d like to:

1. **Add a GUI** using **PyQt** to make it more user-friendly  
2. **Implement SQLite** to log scan history and results for later review  
3. **Add export options** like CSV or JSON for easier data sharing  
4. **Improve error handling** and API rate-limiting compliance  
5. Package it as a standalone app for cross-platform use  

---