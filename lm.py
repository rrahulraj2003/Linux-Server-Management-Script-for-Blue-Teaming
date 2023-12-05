import os
import re
import time

def maluser():
    output = os.popen('w')
    ips = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', output)
    #check ips list against a stored txt file of trusted ips
    #if not ip in ips

def malkey():
    keys = os.popen('cd ~/.ssh/authorized_keys').split('\n')
    #check keys list against a stored txt file of trusted keys
    #if not key in keys


