#encoding=utf-8

# from nltk.book import *
# import nltk.probability
# import numpy
# import matplotlib
# # text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
# # fdist1= nltk.probability.FreqDist(text1)
# # fdist1.plot(50,cumulative=True)

from urllib import *
import os
import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def Tokenizer(originalPath,tokenizeredFilePath):

    #file read ,tokenize and write
    base= os.path.dirname(__file__)
    file=file
    fileWrite=file;

    try:
        file=open(base+'/../Text/text1.txt','r')
        content=file.read();

        #remove all alphabet characters and punctuation
        wordlist='abcdefghikjlmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-[]{}\|?/\"\':;>.<,`'
        for word in content:
            if(word in wordlist):
                content=content.replace(word,'')
        #remove break line character
        content=content.replace('\n','')

        #word segmentation
        ls=jieba.cut(content,cut_all=True)
        contentStr=str(' '.join(ls))
        contentSeged=' '.join(contentStr.split())
        fileWrite=open(base+'/../Text/text1seged.txt','a+')
        # fileWrite.write(contentSeged)

        print('finished')
    except Exception as e:
        print e
    finally:
        print 'close file'
        fileWrite.close()
        file.close()


