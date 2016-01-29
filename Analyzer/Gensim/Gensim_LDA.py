#-*- coding: UTF-8 -*-
import logging
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.WARNING)
logging.root.level = logging.WARNING
import gensim

file=open('Sougou.txt')
allDocuments=file.readlines()
decodeTexts=[]
for document in allDocuments:

    # each document need to be converted into a list
    #split()is important for dividing document into phrase instead of single character
    decodedDocument=list(document.decode('utf-8').split())
    decodeTexts.append(decodedDocument)

wordCountDic=gensim.corpora.Dictionary(decodeTexts)

corpus=[wordCountDic.doc2bow(text) for text in decodeTexts]

tfidf=gensim.models.TfidfModel(corpus)
corpus_tfidf=tfidf[corpus]

lda=gensim.models.LdaModel(corpus_tfidf,id2word=wordCountDic,num_topics=20)

corpus_lda=lda[corpus_tfidf]

for i in range(0,20):
    print(lda.print_topic(i))+"\r\n"