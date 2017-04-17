import sys, os
from time import *

logFileName = ""

class timeMode:
    (showAll, notYear) = range(1, 3)
def getTimeStr(mode=timeMode.showAll):
    lt = localtime()

    if mode == timeMode.notYear:
        timeStr = "%02d%02d %02d:%02d:%02d" % (lt.tm_mon, lt.tm_mday, lt.tm_hour, lt.tm_min, lt.tm_sec)
    else:
        timeStr = "%04d%02d%02d %02d:%02d:%02d" % (lt.tm_year, lt.tm_mon, lt.tm_mday, lt.tm_hour, lt.tm_min, lt.tm_sec)

    return timeStr

def initLogFile():
    global logFileName
    if logFileName == "":
        logFileName = (getTimeStr() + ".log").replace(' ', '_').replace(":", "")

    with open(logFileName, "w+") as fr:
        fr.write('log start time: ' + getTimeStr() + "\n")

    print "init log file[%s] ok!" % (logFileName)

def writeLog(buf, fileName="", mode=timeMode.notYear):
    global logFileName
    if fileName != "":
        logFileName = fileName

    log = getTimeStr(mode) + ": " + buf
    #print log
    with open(logFileName, "a") as fr:
        fr.write(log + "\n")

if __name__ == '__main__':
    initLogFile()
    writeLog("test123")

