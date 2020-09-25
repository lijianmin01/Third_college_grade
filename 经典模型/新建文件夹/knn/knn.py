import numpy as np


def read_file(file_name):
    dataX = []
    dataY = []
    with open(file_name, 'r') as f:
        for line in f:
            # 去空白
            line = line.strip()
            cnt = line.split('\t')
            dataX.append(cnt[:-1])
            dataY.append(cnt[-1])
    dataX = np.array(dataX)
    Y = []
    # 转换标签
    for i in dataY:
        if i == "didntLike":
            Y.append(1)
        elif i == "smallDoses":
            Y.append(2)
        else:
            Y.append(3)
    return dataX, np.array(Y)


# 最大最小规范化
# def auto_norm(dataX):
#     """规范化处理
#     参数 dataX矩阵
#
#     标准化后的数据
#     """
#
#     max_vector = dataX.max(0)
#     min_vector = dataX.min(0)
#     n = len(dataX)
#     max_mat = np.tile(max_vector, (n, 1))
#     min_mat = np.tile(min_vector, (n, 1))
#
#     normX = (dataX - min_mat) / (max_mat - min_mat)
#
#     return normX


import operator


def max_min_score(data_x):
    max = np.max(data_x,axis=0)
    min = np.min(data_x,axis=0)

    maxmin = (data_x - min) / (max - min)

    print(max,min)
    return maxmin


# 书上的
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

dataX, dataY = read_file("datingTestSet.txt")
dataX = dataX.astype('float64')
#max_min_score(dataX)

x = np.array([[0.44832535, 0.39805139, 0.56233353]],dtype='float64')
# x = max_min_score(x)
k =1
print(classify(x,dataX,dataY,k))