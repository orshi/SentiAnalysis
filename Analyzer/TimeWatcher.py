__author__ = 'Shulei'
import datetime
import time
global startTime

def startWatch():
    try:
      global startTime
      startTime=datetime.datetime.now()
    except Exception as e:
        print e

def stopWatch():
    try:
        stopTime=datetime.datetime.now()
        global startTime
        timeDif=stopTime-startTime

        return timeDif
    except Exception as e:
        print e

if __name__ == '__main__':
    startWatch()
    time.sleep(0.2)
    dif=stopWatch()
    print dif