#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Python 2.7
import sys, os, getopt, socket, struct, json
from log import *
from time import *

sysConfig = ""

def usage():
    print "countTraffic.py usage:"
    print "countTraffic.py [--show]"

def osSystem(cmd):
    result = ""
    r = os.popen(cmd)
    result = r.read().strip()
    r.close()

    return result

def getPortTraffic(buf, portName):
    start = buf.find("Chain INPUT")
    end = buf.find("\n", start)

    while end > 0:
        start = end + 1
        end = buf.find("\n", start)
        line = buf[start:end].strip()
        if line.find(portName) > 0:
            valStart = line.find(" ")
            while line[valStart] == ' ':
                valStart += 1

            valEnd = line.find(" ", valStart)
            return line[valStart:valEnd].strip()

    return ""

def getCurrTraffic():
    global sysConfig
    str = ""

    result = osSystem("ifconfig eth0|grep -E 'RX packets|TX packets'")
    start = result.find("(")
    end = result.find(")", start)
    str = "%s%-8s" % (str, result[start + 1: end])

    start = result.find("(", end)
    end = result.find(")", start)
    str = "%s%-8s" % (str, result[start + 1: end])

    result = osSystem("iptables -n -v -L -t filter")
    for port in sysConfig["portList"]:
        val = getPortTraffic(result, port["portStr"])
        str = "%s%-8s" % (str, val)
        #print str

    return str

def initConfig():
    global sysConfig
    with open(r"config.json") as configFile:
        sysConfig = json.load(configFile)
        #print sysConfig.keys()

        for i in sysConfig["portList"]:
            print "portStr[%s] name[%s]" % (i["portStr"], i["name"])

def showTraffic():
    initConfig()
    fileName = osSystem("ls -t|grep '.log$'|head -n1")
    print "log fileName:" + fileName
    writeLog(getCurrTraffic(), fileName)

    with open(fileName) as file:
        print file.read()

def countTraffic():
    global sysConfig
    initConfig()
    initLogFile()

    str = "%-8s%-8s" % ("RX", "TX")
    for port in sysConfig["portList"]:
        str = "%s%-8s" % (str, port["name"])
    writeLog(str)

    while True:
        try:
            writeLog(getCurrTraffic())
        except:
            writeLog("getCurrTraffic except")

        sleep(3600)

if __name__ == '__main__':
    try:	
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help", "show"])
    except:
        usage()
        sys.exit(1)
        
    for key, val in opts:
        if key == "--show":
            showTraffic()
            sys.exit(1)
        elif key == "h" or key == "--help":
            usage()
            sys.exit(1)

    countTraffic()