# flock conf
# v0.0 11-11-18 master@owlh.net

configfile = "/etc/owlh/conf/owlh_conf.json" 

import json

conf = ""

def loadconf():
    with open(configfile) as conf_data:
        global conf 
        conf = json.load(conf_data)

def get_item(item):
    global conf
    return conf[item]

def printconf():
    global conf
    for item in conf: 
        print item + " -> " + conf[item]

loadconf()
