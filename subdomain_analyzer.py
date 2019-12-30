#!/usr/bin/python3

# create a tool that takes a list of subdomains and sends a get request to each one

# will go over the same subdomain TWICE, the first one for http (port 80) and the second for https (port 443)


# make 200 green
# make 403 red
# make 404 blue

import requests
from requests.exceptions import HTTPError
import sys
import time
import os

# print(sys.argv)

# for when the user needs help on how to use the tool


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


def help():

    print("""

    subdomain_analyzer is a tool used to output the status codes of a list of domains

    {Checks both http & https status codes}

    -h displays help information

    -f to specify subdomain file

    Ex. 'python3 subdomain_analyzer.py -f list_of_domains.txt'

    That's about it

    """)


# create a function that takes the usersfile and outputs the details on the screen
def subdomain_list(list):

    os.system("clear")

    title()
    print("[*] Sit back.. this may take some time...")

    time.sleep(2)
    print("[*] Starting scan...\n\n")
    time.sleep(1)

    li = [i.strip().split() for i in open(list).readlines()]

    for domain in li[:-1]:
        # turns each item from the list into a string
        each_domain = ''.join(domain)

        # if it contains https already, don't alter it, and scan with it, then scan using http
        if each_domain[:8] == "https://":

            # say which domain it is testing
            print("[*] Testing -> %s" % (each_domain))

            # send https get request
            # send back status code
            code = response_code(each_domain)
            if code == 200:
                ncode = "200 -> OK"
            elif code == 401:
                ncode = "401 -> Unauthorized"
            elif code == 403:
                ncode = "403 -> Forbidden @_@"
            elif code == 404:
                ncode = "404 -> Not found | Possible Subdomain Takeover?"
            elif code == 408:
                ncode = "408 ->  Request Timed out"
            elif code == 500:
                ncode = "500 -> Internal Server Error"
            elif code == 502:
                ncode = "502 -> Bad Gateway"
            elif code == 503:
                ncode = "503 -> Service Unavailable"
            elif code == 504:
                ncode = "504 -> Gateway Timeout"
            elif code == 999:
                ncode = "Can't Connect..."
            else:
                ncode = "Error"

            print("[*] HTTPS -> %s -> " % (each_domain) + "%s" % (ncode))

            # change the https:// to http://
            new_http_val = each_domain.replace("https://", "http://")
            # send http get request
            # send back status code
            code = response_code(new_http_val)

            if code == 200:
                ncode = "200 -> OK"
            elif code == 401:
                ncode = "401 -> Unauthorized"
            elif code == 403:
                ncode = "403 -> Forbidden @_@"
            elif code == 404:
                ncode = "404 -> Not found | Possible Subdomain Takeover?"
            elif code == 408:
                ncode = "408 ->  Request Timed out"
            elif code == 500:
                ncode = "500 -> Internal Server Error"
            elif code == 502:
                ncode = "502 -> Bad Gateway"
            elif code == 503:
                ncode = "503 -> Service Unavailable"
            elif code == 504:
                ncode = "504 -> Gateway Timeout"
            elif code == 999:
                ncode = "Can't Connect..."
            else:
                ncode = "Error"

            print("[*] HTTP -> %s -> " % (new_http_val) + "%s\n\n" % (ncode))

        # if it contains http already, don't alter it, and scan with it, then scan using https
        elif each_domain[:7] == "http://":

            # say which domain it is testing
            print("[*] Testing -> %s" % (each_domain))

            # send http get request
            # send back status code
            code = response_code(each_domain)
            if code == 200:
                ncode = "200 -> OK"
            elif code == 401:
                ncode = "401 -> Unauthorized"
            elif code == 403:
                ncode = "403 -> Forbidden @_@"
            elif code == 404:
                ncode = "404 -> Not found | Possible Subdomain Takeover?"
            elif code == 408:
                ncode = "408 ->  Request Timed out"
            elif code == 500:
                ncode = "500 -> Internal Server Error"
            elif code == 502:
                ncode = "502 -> Bad Gateway"
            elif code == 503:
                ncode = "503 -> Service Unavailable"
            elif code == 504:
                ncode = "504 -> Gateway Timeout"
            elif code == 999:
                ncode = "Can't Connect..."
            else:
                ncode = "Error"

            print("[*] HTTP -> %s -> " % (each_domain) + "%s" % (ncode))

            # change the http:// to https://
            new_https_val = each_domain.replace("http://", "https://")
            # send https get request
            # send back status code
            code = response_code(new_https_val)

            if code == 200:
                ncode = "200 -> OK"
            elif code == 401:
                ncode = "401 -> Unauthorized"
            elif code == 403:
                ncode = "403 -> Forbidden @_@"
            elif code == 404:
                ncode = "404 -> Not found | Possible Subdomain Takeover?"
            elif code == 408:
                ncode = "408 ->  Request Timed out"
            elif code == 500:
                ncode = "500 -> Internal Server Error"
            elif code == 502:
                ncode = "502 -> Bad Gateway"
            elif code == 503:
                ncode = "503 -> Service Unavailable"
            elif code == 504:
                ncode = "504 -> Gateway Timeout"
            elif code == 999:
                ncode = "Can't Connect..."
            else:
                ncode = "Error"

            print("[*] HTTPS -> %s -> " % (new_https_val) + "%s\n\n" % (ncode))

        # elif it doesn't contain either, add 'http://' scan it, then add 'https://' and scan with it
        elif each_domain[:7] != "http://" or each_domain[:8] != "https://":

            # say which domin tha it is testing first
            print("[*] Testing -> %s" % (each_domain))

            # add http in the front
            new_http_val = ("http://" + each_domain)
            # send http get request
            # send back status code
            code = response_code(new_http_val)
            if code == 200:
                ncode = "200 -> OK"
            elif code == 401:
                ncode = "401 -> Unauthorized"
            elif code == 403:
                ncode = "403 -> Forbidden @_@"
            elif code == 404:
                ncode = "404 -> Not found | Possible Subdomain Takeover?"
            elif code == 408:
                ncode = "408 ->  Request Timed out"
            elif code == 500:
                ncode = "500 -> Internal Server Error"
            elif code == 502:
                ncode = "502 -> Bad Gateway"
            elif code == 503:
                ncode = "503 -> Service Unavailable"
            elif code == 504:
                ncode = "504 -> Gateway Timeout"
            elif code == 999:
                ncode = "Can't Connect..."
            else:
                ncode = "Error"

            print("[*] HTTP -> %s -> " % (new_http_val) + "%s" % (ncode))

            # add https in the front
            new_https_val = ("https://" + each_domain)
            # send https get request
            # send back status code
            code = response_code(new_https_val)
            
            if code == 200:
                ncode = "200 -> OK"
            elif code == 401:
                ncode = "401 -> Unauthorized"
            elif code == 403:
                ncode = "403 -> Forbidden @_@"
            elif code == 404:
                ncode = "404 -> Not found | Possible Subdomain Takeover?"
            elif code == 408:
                ncode = "408 ->  Request Timed out"
            elif code == 500:
                ncode = "500 -> Internal Server Error"
            elif code == 502:
                ncode = "502 -> Bad Gateway"
            elif code == 503:
                ncode = "503 -> Service Unavailable"
            elif code == 504:
                ncode = "504 -> Gateway Timeout"
            elif code == 999:
                ncode = "Can't Connect..."
            else:
                ncode = "Error"

            print("[*] HTTPS -> %s -> " % (new_https_val) + "%s\n\n" % (ncode))

        else:

            # error message
            print("[*] Oops :(")


# create a function that deals with the response codes
def response_code(name):

    try:
        response = requests.get(name, timeout=(3.05, 27))
        # response.raise_for_status()
        # If the response was successful, no Exception will be raised
        stat_code = response.status_code
        return stat_code

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')

    # if the request takes too long to respond after 6.05 seconds
    except requests.Timeout:
        # print("[*] request timed out")
        stat_code = 408
        return stat_code

    except requests.ConnectionError:
        # print("[*] Couldn't connect")
        stat_code = 999  # not a juicewrld refrence, just like the number :)
        return stat_code

    except Exception as err:
        print(f'Other error occurred: {err}')

    except KeyboardInterrupt as key_err:
        print("Next..")

    else:
        print("DONE!")


if len(sys.argv) == 1:
    print("[*] Please use -h for help")
else:
    for i in sys.argv:
        if i == "-h":
            help()
            break
        elif i == "-f":
            subdomain_list(sys.argv[2])
            print("[*] Done! :) ")
        else:
            continue
