#!/usr/bin/python3

# subzer0
# created by ~ 0xApt_

# subzer0 takes a list of subdomains, and sends a get request to each one, returning the status code
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

    print( OKBLUE + """  
  ______             __                                       ______  
 /      \           /  |                                     /      \ 
/$$$$$$  | __    __ $$ |____   ________   ______    ______  /$$$$$$  |
$$ \__$$/ /  |  /  |$$      \ /        | /      \  /      \ $$$  \$$ |
$$      \ $$ |  $$ |$$$$$$$  |$$$$$$$$/ /$$$$$$  |/$$$$$$  |$$$$  $$ |
 $$$$$$  |$$ |  $$ |$$ |  $$ |  /  $$/  $$    $$ |$$ |  $$/ $$ $$ $$ |
/  \__$$ |$$ \__$$ |$$ |__$$ | /$$$$/__ $$$$$$$$/ $$ |      $$ \$$$$ |
$$    $$/ $$    $$/ $$    $$/ /$$      |$$       |$$ |      $$   $$$/ 
 $$$$$$/   $$$$$$/  $$$$$$$/  $$$$$$$$/  $$$$$$$/ $$/        $$$$$$/  1.0
   
          """ + ENDC)
    
    print(BOLD + """                       Created by 0xApt_
          
          
          """ + ENDC)

# for when the user needs help on how to use the tool
def help():

    print("""

    SubZer0 is a tool used to output the status codes of a list of domains

    {Checks both http & https status codes}

    -h  -Display help information

    -f  - Specify subdomain file

    Ex. 'python3 subzer0.py -f <file_containing_list_of_domains.txt>'
    
    
    To save the output, you can do so using following command 
    
    'python3 subzer0.py -f list_of_domains.txt > filetosaveoutput.txt'
    
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
    print("[*] Starting scan...\n")
   
    
    li = [i.strip().split() for i in open(list).readlines()]

    for domain in li[:-1]:
        
        each_domain = ''.join(domain)

        # if it contains https already, don't alter it, and scan with it, then scan using http
        if each_domain[:8] == "https://":

            print(BOLD + "[*] Testing -> %s" % (each_domain) + ENDC)

            ez_status(each_domain,"HTTPS")
	    
            new_http_val = each_domain.replace("https://", "http://")

            ez_status(new_http_val,"HTTP")


        # if it contains http already, don't alter it; scan with it; then switch to https
        elif each_domain[:7] == "http://":
            
            print(BOLD + "[*] Testing -> %s" % (each_domain) + ENDC)
            
            ez_status(each_domain,"HTTP")
            
            new_https_val = each_domain.replace("http://", "https://")   
              
            ez_status(new_https_val,"HTTPS")


        # elif it doesn't contain either; add 'http://' scan it, then add 'https://' and scan with it
        elif each_domain[:7] != "http://" or each_domain[:8] != "https://":
            
            print(BOLD + "[*] Testing -> %s" % (each_domain) + ENDC)
            
            new_http_val = ("http://" + each_domain)
                   
            ez_status(new_http_val,"HTTP")
            
            new_https_val = ("https://" + each_domain)

            ez_status(new_https_val, "HTTPS")


# create a function that deals with the response codes
def response_code(name):

    try:
        response = requests.get(name, timeout=(3.05, 27))
        stat_code = response.status_code
        return stat_code

    except requests.Timeout:
        stat_code = 408
        return stat_code

    except requests.ConnectionError:
        stat_code = 999 
        return stat_code

    except Exception as err:
        pass

    except KeyboardInterrupt as key_err:
        print("\n[*] Stopping..")
        exit()

try:
    if sys.argv[1] == "-h":
        help()
    elif sys.argv[1] == "-f":
        try:
            domain_file = sys.argv[2]
            subdomain_list(domain_file)
            print("[*] Done!\n")
        except FileNotFoundError as fnf:
            print("[*] No such file known as {}".format(domain_file))   
    elif sys.argv > sys.argv[2]:
        pass
    else:
        pass
except TypeError as typerr:
    sys.stderr.write("[*] Please use -h for help \n")
    sys.stout.flush()
except IndexError as idxerr:
    sys.stderr.write("[*] Please use -h for help \n")
    sys.stout.flush()
