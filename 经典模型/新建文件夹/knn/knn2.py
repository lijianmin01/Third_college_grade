import operator

import numpy as np

#   将文本记录到转换Numpy
def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    number_of_lines = len(arrayOLines)
    returnMat = np.zeros((number_of_lines,3))
    classLabelVector = []
    index =0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:]=listFromLine[:-1]
        classLabelVector.append(listFromLine[-1])
        index += 1

    return returnMat,classLabelVector

# 归一化特征
def autoNorm(dataSet):
    min = dataSet.min(0)
    max = dataSet.max(0)
    ranges = max - min

    # normDataSet = np.zeros(dataSet.shape())

    m = dataSet.shape[0]
    normDataSet =dataSet - np.tile(min,(m,1))
    
    normDataSet = normDataSet/(ranges)

    # return normDataSet,ranges,min
    return normDataSet

def classify(intX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(intX,(dataSetSize,1))-dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    sqDistances = sqDistances**(0.5)
    sortedDistIndicies = sqDistances.argsort()
    classCount = {}
    for i in range(k):
        voteiLabel = labels[sortedDistIndicies[i]]
        classCount[voteiLabel]=classCount.get(voteiLabel,0)+1
    sortedClassCount = sorted(classCount.items(),
                             key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

data_x,data_y=file2matrix("datingTestSet.txt")
data_x = autoNorm(data_x)

x = np.array([[40920,8.326976,0.953952]],dtype='float64')
x=autoNorm(x)
k =1
print(classify(x,data_x,data_y,k))
