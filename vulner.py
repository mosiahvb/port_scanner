# The following requests information from the NVD database in regards 
# to CVE's on known vulnerabilities for open ports
import requests

def use_nvd_api(service, version, api_key,max_results=3):
    '''
    Takes a service and its version, queries the NVD API using the provided 
    key, and returns a list of up to 3 vulnerability IDs (CVEs)
    '''
    url = 'https://services.nvd.nist.gov/rest/json/cves/2.0' # the url needed to acsses cve data
    headers = {'apiKey': api_key} # conects and aplyes the key ihave to make a request from the api

    query = f'{service} {version}'.strip() # prepars the service and version for use in query
    specifics = {'keywordSearch': query, 'resultsPerPage': max_results} # spesifying what im looking for
    try:
        response = requests.get(url, headers=headers, params=specifics, timeout=10) # making the request from the API
        response.raise_for_status()# If the request fails trigers the except
        data = response.json() # taking API data as json and turns it into a dictionary
        cve_list = []

        for item in data.get('vulnerabilities', []):# Makes request for vulnerabilities suction of the json, if not there returns empty list
            cve_id = item['cve']['id'] # grabs the info in the id section of the dictionary 
            cve_list.append(cve_id) # adding to the cve_list
        # for i in cve_list:
        #     print(i)
        return cve_list
        

    except requests.RequestException as e: # handaling errors 
        print(f'[ERROR] Failed to query NVD API: {e}')

        return []
