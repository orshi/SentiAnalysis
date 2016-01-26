#encoding=utf-8
import os
import nltk
import sys
reload(sys)
sys.setdefaultencoding('utf8')
global  base
base= os.path.dirname(__file__)

def GetStopWords(filePath=base+'/../Text/StopWords.txt'):
    try:
          stopWordsContent=open(filePath).read().decode('utf8')
          stopWords=stopWordsContent.replace('\n',' ').split()
          return stopWords
    except Exception as e:
        print(e)

def WrodsFreq(fileName):
    segedFile=file

    #read key words of a file
    segedFile=open(str(fileName),'r')
    content=segedFile.read().decode('utf8')
    listed=content.split()
    freqDict=nltk.FreqDist(listed)

    # read stop words
    stopWords=GetStopWords(base+'/../Text/StopWords.txt')

    #remove stop words
    tempDic=freqDict.copy()
    for k in freqDict:
        if(unicode(k) in stopWords):
            tempDic.pop(k)
    print len(tempDic)
    sortedDic=sorted(tempDic.iteritems(),key=lambda x:x[1],reverse=True)

    #todo:if dic is less than 19

    return sortedDic

feature=WrodsFreq( base+'/../Text/text1seged.txt')

from KL_Distance import *
feature2=WrodsFreq(base+'/../Text/text1seged.txt')
KL_Distance(feature,feature2)
