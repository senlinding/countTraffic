import sys, os
from time import *

logFileName = ""

def getTimeStr():
    lt = localtime()
    timeStr = "%04d%02d%02d %02d:%02d:%02d" % (lt.tm_year, lt.tm_mon, lt.tm_mday, lt.tm_hour, lt.tm_min, lt.tm_sec)
    return timeStr

def initLogFile():
    global logFileName
    if logFileName == "":
        logFileName = (getTimeStr() + ".log").replace(' ', '_').replace(":", "")

    with open(logFileName, "w+") as fr:
        fr.write('log start time: ' + str(ctime(time())) + "\n")

    print "init log file[%s] ok!" % (logFileName)

def writeLog(buf, fileName=""):
    global logFileName
    if fileName != "":
        logFileName = fileName

    log = getTimeStr() + ": " + buf
    #print log
    with open(logFileName, "a") as fr:
        fr.write(log + "\n")


if __name__ == '__main__':
    initLogFile()
    writeLog("test123")

