#!/usr/bin/python3

# subdomain_analyzer
# created by ~ 0xApt_

# subdomin_analyzer takes a list of subdomains, and sends a get request to each one, returning the status code
# will go over the same subdomain TWICE, the first one for http (port 80) and the second for https (port 443)


import requests
from requests.exceptions import HTTPError
import sys
import time
import os


#colors
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'



#head title
def title():

    print("""  
                   _         _                       _                                             
                  | |       | |                     (_)                                     
         ___ _   _| |__   __| | ___  _ __ ___   __ _ _ _ __             
        / __| | | | '_ \ / _` |/ _ \| '_ ` _ \ / _` | | '_ \          
        \__ \ |_| | |_) | (_| | (_) | | | | | | (_| | | | | |       
        |___/\__,_|_.__/ \__,_|\___/|_| |_| |_|\__,_|_|_| |_|         
                                  _  
                                 | |                  
                 __ _ _ __   __ _| |_   _ _______ _ __ 
                / _` | '_ \ / _` | | | | |_  / _ \ '__|
               | (_| | | | | (_| | | |_| |/ /  __/ |   
                \__,_|_| |_|\__,_|_|\__, /___\___|_|   
                                    __/ |             
                                   |___/              
                        
                            
                          Created by 0xApt_
   
   
   
          """)

# for when the user needs help on how to use the tool
def help():

    print("""

    subdomain_analyzer is a tool used to output the status codes of a list of domains

    {Checks both http & https status codes}

    -h  - Display help information

    -f  - Specify subdomain file

    Ex. 'python3 subdomain_analyzer.py -f list_of_domains.txt'
    
    
    To save the output, you can do so using following command 
    
    'python3 subdomain_analyzer.py -f list_of_domains.txt > filetosaveoutput.txt'
    
    Note: It may seem like it is hanging, but it's just program running in the background until it is done.


    That's about it.

    """)


#shows the status codes along with domain name for https
def ez_status(name,TYPE):
    
    
    code = response_code(name)
    if code == 200:
        ncode = "200 -> OK"
        print(OKGREEN + "[*] "+ TYPE + " -> %s -> " % (name) + "%s" % (ncode) + ENDC)
    elif code == 401:
        ncode = "401 -> Unauthorized"
        print( WARNING + "[*] "+ TYPE + " -> %s -> " % (name) + "%s" % (ncode) + ENDC)
    elif code == 403:
        ncode = "403 -> Forbidden @_@"
        print( WARNING + "[*] "+ TYPE + " -> %s -> " % (name) + "%s" % (ncode) + ENDC)
    elif code == 404:
        ncode = "404 -> Not found | Possible Subdomain Takeover?"
        print(OKBLUE + "[*] "+ TYPE + " -> %s -> " % (name) + "%s" % (ncode) + ENDC)
    elif code == 408:
        ncode = "408 ->  Request Timed out"
        print( WARNING + "[*] "+ TYPE + " -> %s -> " % (name) + "%s" % (ncode) + ENDC)
    elif code == 500:
        ncode = "500 -> Internal Server Error"
        print( FAIL + "[*] "+ TYPE + "-> %s -> " % (name) + "%s" % (ncode) + ENDC)
    elif code == 502:
        ncode = "502 -> Bad Gateway"
        print( WARNING + "[*] "+ TYPE + " -> %s -> " % (name) + "%s" % (ncode) + ENDC)
    elif code == 503:
        ncode = "503 -> Service Unavailable"
        print( WARNING + "[*] "+ TYPE + " -> %s -> " % (name) + "%s" % (ncode) + ENDC)
    elif code == 504:
        ncode = "504 -> Gateway Timeout"
        print( WARNING + "[*] "+ TYPE + " -> %s -> " % (name) + "%s" % (ncode) + ENDC)
    elif code == 999:
        ncode = "Can't Connect..."
        print( FAIL + "[*] " + TYPE + " -> %s -> " % (name) + "%s" % (ncode) + ENDC)
    else:
        ncode = "Error"
        print( FAIL + "[*] "+ TYPE + " -> %s -> " % (name) + "%s" % (ncode) + ENDC)
    
   


        
# create a function that takes the usersfile and outputs the details on the screen
def subdomain_list(list):
    
    os.system("clear")
    title()
    print("[*] Sit back.. this may take some time...")
    time.sleep(2)
    print("[*] Starting scan...\n")
    time.sleep(1)
    

    li = [i.strip().split() for i in open(list).readlines()]

    for domain in li[:-1]:
        # turns each item from the list into a string
        each_domain = ''.join(domain)

        # if it contains https already, don't alter it, and scan with it, then scan using http
        if each_domain[:8] == "https://":

            # say which domain it is testing
            print(BOLD + "[*] Testing -> %s" % (each_domain) + ENDC)

            # send https get request
            ez_status(each_domain,"HTTPS")
	    
            # change the https:// to http://
            new_http_val = each_domain.replace("https://", "http://")

            # send http get request
            ez_status(new_http_val,"HTTP")


        # if it contains http already, don't alter it; scan with it; then switch to https
        elif each_domain[:7] == "http://":

            # say which domain it is testing
            print(BOLD + "[*] Testing -> %s" % (each_domain) + ENDC)

            # send http get request
            ez_status(each_domain,"HTTP")

            # change the http:// to https://
            new_https_val = each_domain.replace("http://", "https://")

            # send https get request
            ez_status(new_https_val,"HTTPS")


        # elif it doesn't contain either; add 'http://' scan it, then add 'https://' and scan with it
        elif each_domain[:7] != "http://" or each_domain[:8] != "https://":

            # say which domin tha it is testing first
            print(BOLD + "[*] Testing -> %s" % (each_domain) + ENDC)

            # add http to the front
            new_http_val = ("http://" + each_domain)

            
            # send http get request           
            ez_status(new_http_val,"HTTP")
            
            # add https to the front
            new_https_val = ("https://" + each_domain)

            # send https get request
            ez_status(new_https_val, "HTTPS")


# create a function that deals with the response codes
def response_code(name):

    try:
        response = requests.get(name, timeout=(3.05, 27))
        stat_code = response.status_code
        return stat_code

    # if the request takes too long to respond after 6.05 seconds
    except requests.Timeout:
        stat_code = 408
        return stat_code

    except requests.ConnectionError:
        # Couldn't connect
        stat_code = 999  # not a juicewrld reference, just like the number :)
        return stat_code

    except Exception as err:
        pass

    except KeyboardInterrupt as key_err:
        print("\nNext..")

    else:
        pass


try:
    if sys.argv[1] == "-h":
        help()
    elif sys.argv[1] == "-f":
        try:
            domain_file = sys.argv[2]
            subdomain_list(domain_file)
            print("[*] Done!\n")
        except FileNotFoundError as fnf:
            print ("[*] No such file known as '%s'" % (domain_file))
    elif sys.argv > sys.argv[2]:
        pass
    else:
        pass
except TypeError as typerr:
    print("[*] Please use -h for help")
except IndexError as idxerr:
    print("[*] Please use -h for help")

