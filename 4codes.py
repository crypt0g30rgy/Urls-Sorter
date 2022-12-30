#!/usr/bin/python3

import os
import requests
import re
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Check for correct number of arguments
if len(sys.argv) != 2:
    print("Error: Incorrect number of arguments.")
    print("Usage: python 4codes.py [input_file]")
    sys.exit(1)

# Open file
try:
    input_file = open(sys.argv[1], 'r')
except IOError as err:
    print("Error: Could not open file: %s" % err)
    sys.exit(2)

# Create a folder called codes
if not os.path.exists('codes'):
    os.makedirs('codes')

# Create output files
out_2xx = open("codes/2XX_urls.txt", 'w')
out_3xx = open("codes/3XX_urls.txt", 'w')
out_4xx = open("codes/4XX_urls.txt", 'w')
out_5xx = open("codes/5XX_urls.txt", 'w')

# Read lines in input file
for line in input_file:
    line = line.strip()
    # Check if line contains a URL
    if re.search("^http[s]?://", line):
        # Visit the URL
        url = line
        response = requests.get(url, verify=False,allow_redirects=False)
        status = response.status_code

        # Write URL to appropriate file
        if status // 100 == 2:
            out_2xx.write(url+"\n")
        elif status // 100 == 3:
            out_3xx.write(url+"\n")
        elif status // 100 == 4:
            out_4xx.write(url+"\n")
        elif status // 100 == 5:
            out_5xx.write(url+"\n")

# Close files
input_file.close()
out_2xx.close()
out_3xx.close()
out_4xx.close()
out_5xx.close()