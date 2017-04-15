import sys, os
from time import *

logFileName = ""
def initLogFile():
    global logFileName
    if logFileName == "":
        logFileName = (str(ctime(time())) + ".log").replace(' ', '_').replace(":", "")
        start = logFileName.find("_")
        logFileName = logFileName[start + 1:]

    with open(logFileName, "w+") as fr:
        fr.write('log start time: ' + str(ctime(time())) + "\n")

    print "init log file[%s] ok!" % (logFileName)

def writeLog(buf, fileName=""):
    global logFileName
    if fileName != "":
        logFileName = fileName

    log = str(ctime(time())) + ": " + buf
    print log
    with open(logFileName, "a") as fr:
        fr.write(log + "\n")

'''
if __name__ == '__main__':
    initLogFile()
    writeLog("test123")
'''
