#!/usr/bin/env python

import requests
import argparse
import sys
import json

URL = "http://swift.rcc.uchicago.edu:50011/"

if __name__ == "__main__":

    parser   = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", default="yadu", help="User name to identify message queue")
    parser.add_argument("-m", "--messagefile", default=None, help="Message file")
    args   = parser.parse_args()

    content = None
    if args.messagefile == None:
        content = sys.stdin.read()
        #print "Message from stdin: \n", content
    else:
        with open(args.messagefile, 'r') as f:
            content = f.read()
            #print "Message from file : \n", content

    r = requests.post(URL+"submit", data = json.dumps({ "username" : args.user ,
                                             "message"  : content }) )
    print r.status_code,
    print r.json()["Message"]


