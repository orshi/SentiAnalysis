__author__ = 'Shulei'
from gensim  import models,corpora,similarities
import os

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

documents = ["Human machine interface for lab abc computer applications",
              "A survey of user opinion of computer system response time",
              "The EPS user interface management system",
              "System and human system engineering testing of EPS",
              "Relation of user perceived response time to error measurement",
              "The generation of random binary unordered trees",
              "The intersection graph of paths in trees",
              "Graph minors IV Widths of trees and well quasi ordering",
              "Graph minors A survey"]

stoplist=set("for a the of an and end to in".split())

# remove stop words
texts=[[word for word in document.lower().split() if word not in stoplist] for document in documents]

from collections import defaultdict

frequency=defaultdict(int)
for text in texts:
    for token in text:
        frequency[token]+=1

# remove words that frequency lower then 1
texts=[[word for word in text if frequency[token]>1] for text in texts]
from pprint import pprint
pprint(texts)

dictionary=corpora.Dictionary(texts)
#dictionary.save('Q:\PythonProjects\SentiAnalizer\Text\storeedDic.dic')
print(dictionary.token2id)

doc_new="human computer interation"
new_vec=dictionary.doc2bow(doc_new.lower().split())
