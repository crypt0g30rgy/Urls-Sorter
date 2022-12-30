#!/usr/bin/python3
import os
import re
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# read URLs from the file
file_path = input('Please enter the file path: ')
urls = open(file_path, 'r').readlines()

# Create a folder called codes
if not os.path.exists('codes'):
    os.makedirs('codes')


for url in urls:
    url = url.strip()
    response = requests.get(url, verify=False,allow_redirects=False)
    status_code = response.status_code
    
    # use regex to save URLs according to response code
    if re.match(r'2\d\d', str(status_code)):
        with open('codes/2xx.txt', 'a') as f:
             f.write('\n')
             f.write(url)
    elif re.match(r'3\d\d', str(status_code)):
        with open('codes/3xx.txt', 'a') as f:
            f.write(url)
    elif re.match(r'4\d\d', str(status_code)):
        with open('codes/4xx.txt', 'a') as f:
            f.write(url)
    elif re.match(r'5\d\d', str(status_code)):
        with open('codes/5xx.txt', 'a') as f:
            f.write(url)
    else:
        # for other status codes
        with open('codes/others.txt', 'a') as f:
            f.write(url)  