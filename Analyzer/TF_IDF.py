__author__ = 'Shulei'
import jieba
import jieba.analyse
import os
from TimeWatcher import  *

global  base
base= os.path.dirname(__file__)

def extract_top(k=10):
    try:
        startWatch()
        file=open(base+'/../Text/text1.txt','r')
        content=file.read()
        tags=jieba.analyse.extract_tags(content,k)
        dif=stopWatch()
        print dif
        print tags
        inputValue=input("")

    except Exception as e:
        print(e)

if __name__ =='__main__':
    extract_top()
