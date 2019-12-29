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

# print(sys.argv)

# for when the user needs help on how to use the tool


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

    li = [i.strip().split() for i in open(list).readlines()]

    for domain in li:
        each_domain = ''.join(domain)

        # if it contains https already, don't alter it, and scan with it, then scan using http
        if each_domain[:8] == "https://":

            # send https get request
            # send back status code
            code = response_code(each_domain)
            print("[*] HTTPS -> %s -> %d " % (each_domain, code))

            # change the https:// to http://
            new_http_val = each_domain.replace("https://", "http://")
            # send http get request
            # send back status code
            code = response_code(new_http_val)
            print("[*] HTTP -> %s -> %d" % (new_http_val, code))

        # if it contains http already, don't alter it, and scan with it, then scan using https
        elif each_domain[:7] == "http://":

            # send http get request
            # send back status code
            code = response_code(each_domain)
            print("[*] HTTP -> %s -> %d" % (each_domain, code))

            # change the http:// to https://
            new_https_val = each_domain.replace("http://", "https://")
            # send https get request
            # send back status code
            code = response_code(new_https_val)
            print("[*] HTTPS -> %s -> %d" % (new_https_val, code))

        # if it doesn't contain either, add 'http://' scan it, then add 'https://' and scan with it
        elif each_domain[:7] != "http://" or each_domain[:8] != "https://":

            # add http in the front
            new_http_val = ("http://" + each_domain)
            # send http get request
            # send back status code
            code = response_code(new_http_val)
            if code == 404:
                ncode = 404
            elif code == 200:
                ncode = 200
            elif code == 403:
                ncode = 403
            else:
                print(code)
                ncode = "Might want to check manually.."
            print("[*] HTTP -> %s -> " % (new_http_val) + "%s" % (ncode))

            # add https in the front
            new_https_val = ("https://" + each_domain)
            # send https get request
            # send back status code
            code = response_code(new_https_val)
            if code == 200:
                print(code)
                ncode = 200
            elif code == 403:
                ncode = 403
            elif code == 404:
                ncode = 404
            else:
                print(code)
                ncode = "Might want to check manually.."
            print("[*] HTTPS -> %s -> " % (new_https_val) + "%s" % (ncode))

        else:

            # error message
            print("[*] Oops :(")


# create a function that deals with the response codes
def response_code(name):

    try:
        response = requests.get(name)
        # response.raise_for_status()
        # If the response was successful, no Exception will be raised
        stat_code = response.status_code
        return stat_code

    except HTTPError as http_err:
        pass

    except Exception as err:
        pass

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
            print("\n[*] Done! :) ")
        else:
            continue
