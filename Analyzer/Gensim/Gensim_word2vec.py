#-*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'Shulei'

from gensim.models import word2vec
import os
import jieba
import logging
from gensim.models.word2vec import LineSentence

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

model_path='SougouDic.txt'

def GetAllContent(directoryPath,encoding='gbk'):
        documents=[]
        paths=os.listdir(directoryPath)

        for path in paths:
            try:
                currentPath=directoryPath+"\\"+path
                print(directoryPath+"/"+path)
                if os.path.isdir(currentPath):
                     documents.extend(GetAllContent(currentPath,encoding))
                else:
                    fileToRead=open(currentPath,'r')
                    try:
                        fileContent=fileToRead.read().decode(encoding).strip()#.encode('utf-8')
                        documents.append(fileContent)
                    except UnicodeDecodeError as e:
                        print(e)
                    finally:
                        fileToRead.close()
            except Exception as ex:
                print(ex)

        return documents

def WordCutter(content ):
       # wordlist='abcdefghikjlmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-[]{}\|?/\"\':;>.<,`，。！？；：”“《》@#￥%…………&*、％ ＄（）【】=-+——|·★☆－１２３４５６７８９０ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＧＵＶＷＸＹＺ※●  ■＞＜'

       # word list contains english character
       wordlist='\n!@#$%^&*()_+=-[]{}\|?/\"\':;>.<,`，。！？；：”“《》@#￥%…………&*、％ ＄（）【】=-+——|·★☆－１２３４５６７８９０ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＧＵＶＷＸＹＺ※●■＞　＜ ，。、；‘’－——'
       # wordlist=['!','@','#','$','%','^','&','*','(',')','_','+','=','-','[',']','{','}','\\','|','?','/','\"',':',';','>','.','<','\'',',','`','@','#','&','*',' ',u'。',u'！',u'？',u'；',u'：',u'”',u'“',u'《',u'》',u'￥',u'…………',u'、',u'％',u'＄' ,u'（',u'）',u'【',u'】',u'=',u'-+',u'—',u'—','|',u'·',u'★',u'☆',u'－',u'※',u'●',u'‘',u'■',u'＞',u'＜',u' ']
       for word in content:
            if(word in wordlist):
                content=content.replace(word,'')
       content=content.strip()

       #todo:logic error?
       ls=jieba.cut(content)
       contentSeged=str(' '.join(ls))
       return contentSeged

def PrepareData(path,encoding,outputFile):
    # prepare for raw corpus data
    allContent= GetAllContent(path,encoding)
    cuttedContent=""
    index=0
    for content in allContent:
        cutted=WordCutter(content.strip())
        cuttedContent+=cutted+"\n"
        print "cutted :\n"+str(index)
        index+=1

    fileWriter=open(outputFile,'a+')
    fileWriter.write(cuttedContent)
    fileWriter.close()
    print(allContent.__len__())

def Train(corpusPath,savedModelName):

    # train model from text file and save to file
    sentences=LineSentence(corpusPath,max_sentence_length=200000)
    # content=open(corpusPath).read()
    model=word2vec.Word2Vec(sentences,min_count=10,size=100,workers=10,sample=1e-5)
    model.save_word2vec_format(savedModelName,binary=False)

if __name__ =="__main__":

    PrepareData('Q:\PythonProjects\SentiAnalizer\TrainSet\Reduced','gbk','Sougou.txt')
    Train('Sougou.txt',"SougouVector.txt")



