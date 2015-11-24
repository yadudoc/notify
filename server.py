#!/usr/bin/env python
# Ref: http://bottlepy.org/docs/dev/tutorial.html

import uuid
import time, datetime
import subprocess
import os
import glob
import json
from bottle import route, run, get, post, request, put
from bottle import response

def tstamp():
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

MESSAGE_QUEUE={ "yadu": [] };

#------------------------------------------------------------------------------
# Handle job submission
@post('/submit')
def put_submit():
    b = request.body.read()
    j = json.loads(b)
    print "Json :", j
    print j["username"]
    print j["message"]
    j["timestamp"] = tstamp()
    if j["username"] not in MESSAGE_QUEUE:
        MESSAGE_QUEUE["username"] = []

    MESSAGE_QUEUE[j["username"]].append(json.dumps(j))
    return { "HTTP_code": 200 , "Message" : "ACK"}


#------------------------------------------------------------------------------
# Process job retrieve requests
@get('/retrieve/<username>')
def get_retrieve(username):
    #user_id   = request.json['user']
    #return { "job_id" : job_id }
    #json     = get_job_results(job_id)
    print "Username : ", username

    if username not in MESSAGE_QUEUE:
        return "ERROR: Username not found in queue\n"

    if not MESSAGE_QUEUE[username]:
        return "No new notifications\n"

    message = MESSAGE_QUEUE[username].pop(0)
    data = json.loads(message)
    print data["message"]
    print data["timestamp"]

    #response.status = int(json["HTTP_code"])
    #return MESSAGE_QUEUE[user][0]
    return "{0}\n{1}\n".format(data["timestamp"], data["message"])

run(host='0.0.0.0', port=50011, debug=True, reloader=True)
