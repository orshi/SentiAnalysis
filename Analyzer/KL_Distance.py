__author__ = 'Shulei'
import math

def KL_Distance(a,b):

 try:
        totalA=0
        totalB=0

        probListA={}
        probListB={}

        for k,v in a:
            totalA=totalA+v

        for k,v in b:
            totalB=totalB+v

        for k,v in a:
            percentage=float(v)/totalA
            probListA[k]=percentage

        for k,v in b:
            percentage=float(v)/totalB
            probListB[k]=percentage

        relative_entropy=0.0

        print probListA

        for k in probListA.iterkeys():
            print k
            if(probListB.has_key(k)):
                singalEntropy=probListA[k]*math.log(probListA[k]/probListB[k])
                relative_entropy=relative_entropy+singalEntropy

        return relative_entropy

 except Exception as e:
      print  e
      return None