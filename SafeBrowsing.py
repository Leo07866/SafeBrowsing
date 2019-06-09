# Download and install the pysafe library from github:https://github.com/Te-k/pysafe
# Author: Leo07866
# Date: 09 June 2019

from pysafebrowsing import SafeBrowsing
# from termcolor import colored
import os 

# Create a variable for my Google API key.
google_api_key = SafeBrowsing(API-KEY-HERE)

'''creates a funtion that asks the path of the urlList file from the user
if the user enters wrong path the programme returne "file does not exists "
if path is correct, open the file and read through the lines and loop through each line
and then checks url with lookup client and prints both malicious and safe urls.'''

def safe_browsing():
        global line
        user_input = input('[!][!] Enter path: ')

        if not os.path.exists(user_input):
                raise IOError ('[X][X] file does not exsit,please check path again!!')
        url_dir = open(user_input)
        line = url_dir.readline()
        while line:
                threat_list = google_api_key.lookup_urls([line])
                print ('==============================================')
                print ('[x][x] URL: ' +str([line]) +str(threat_list))
                print ('==============================================')
                line = url_dir.readline()
        url_dir.close()
safe_browsing()
