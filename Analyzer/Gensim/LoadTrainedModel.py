#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'Shulei'
from gensim.models import word2vec
import logging,sys
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#load saved model
model_path="SougouVector.txt"
model=word2vec.Word2Vec.load_word2vec_format(model_path,binary=False)
result= model.most_similar(U'男人')
for word in result:
    print'%s -- %f'%(word[0],word[1])

print('finished!')