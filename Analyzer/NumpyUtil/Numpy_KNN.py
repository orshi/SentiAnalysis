__author__ = 'Shulei'
from numpy import *
import operator
import matplotlib.pyplot as plt

def file2matrix(fileName):

    file=open(fileName)
    allLines=file.readlines()
    numberOfLines=len(allLines)
    returnMat=zeros((numberOfLines,3))
    classLabelVector=[]
    index =0;
    for line in allLines:
        line=line.strip()
        listFromLines=line.split('\t')
        returnMat[index,:]=listFromLines[0:3]
        classLabelVector.append(int(listFromLines[-1]))
        index+=1
    return returnMat,classLabelVector

def normData(dataSet):
    max=dataSet.max(0)
    min=dataSet.min(0)
    range=max-min
    normDataSet=zeros(shape(dataSet))
    rowDemention=dataSet.shape[0]
    normDataSet=dataSet-tile(min,(rowDemention,1))
    normDataSet=normDataSet/tile(range,(rowDemention,1))
    return normDataSet,range,min

#k-means
def classify0(inx,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]

    diffMat=tile(inx,(dataSetSize,1))-dataSet

    #inner product
    sqDiffMat=diffMat**2
    sqDistances=sqDiffMat.sum(axis=1)
    distances=sqDistances**0.5

    #calculate the distance with each point and get the nearest k point, argsort returns the index of sorted distances value
    sortedDistances=distances.argsort()

    classCount={}
    for i in range(k):
        voteLabel=labels[sortedDistances[i]]
        #print sortedDistances[i]
        classCount[voteLabel]=classCount.get(voteLabel,0)+1
    # classCount.iteritems() iterator of items , operator.itermgetter(1) user data's second dimension
    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)

    return sortedClassCount[0][0]

if __name__=='__main__':

   hoRatio=0.10
   dataMatrix,label=file2matrix('Q:\PythonProjects\SentiAnalizer\NumpyData\datingTestSet2.txt')
   normedData,rangeValue,minValues=normData(dataMatrix)
   rowDimenssion=normedData.shape[0]
   numTestVector= int(rowDimenssion*hoRatio)
   errorCount=0

   for i in range(numTestVector):
       classifyReult=classify0(normedData[i,:],normedData[numTestVector:rowDimenssion,:],label[numTestVector:rowDimenssion],3)
       print "the classifier came back with : %d the real answer is %d" % (classifyReult,label[i])
       if(classifyReult!=label[i]):
           errorCount+=1.0
   print "total error rate is %d" % (errorCount/float(numTestVector))




