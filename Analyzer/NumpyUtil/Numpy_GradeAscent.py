__author__ = 'Shulei'
import  math
from numpy import *

def loadDataSet():
    dataMat=[]
    labelMat=[]
    fr=open("Q:\PythonProjects\SentiAnalizer\NumpyData\\testSet_logistic.txt",'r')
    for line in fr.readlines():
        lineArr=line.strip().split()
        dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat


def sigmoid(inx):
    returnedValue=[]
    for value in inx:
        returnedValue.append( 1.0/(1+math.exp(-value)))

    return mat(returnedValue).transpose()

def gradeAscent(dataMatIn,labels):
    dataMatrix=mat(dataMatIn)
    labelMatrix=mat(labels).transpose()
    m,n=shape(dataMatrix)
    alpha=0.001
    maxCycle=500
    weights=ones((n,1))
    for k in range(maxCycle):
        h=sigmoid(dataMatrix*weights)
        error=(labelMatrix-h)
        weights=weights+alpha*dataMatrix.transpose()*error
        print weights
    return weights

if __name__=='__main__':
    dataMat,labelMat=loadDataSet()
    weithts=gradeAscent(dataMat,labelMat)
    print weithts