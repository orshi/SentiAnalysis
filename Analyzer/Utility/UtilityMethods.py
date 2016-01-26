__author__ = 'Shulei'
import os
def GetAllContent(directoryPath):
    documents=[]
    paths=os.listdir(directoryPath)
    for path in paths:
        currentPath=directoryPath+"\\"+path
        print(directoryPath+"/"+path)
        if os.path.isdir(currentPath):
             documents.extend(GetAllContent(currentPath))
        else:
            filecontent=open(currentPath,'r').read()
            documents.append(filecontent)
    return documents
