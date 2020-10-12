from math import log
import operator
import pandas as pd
import numpy as np
import time


# 计算信息熵
def jisuanEnt(dataset):
    numEntries = len(dataset)
    labelCounts = {}
    # 给所有可能分类创建字典
    for featVec in dataset:
        currentlabel = featVec[-1]
        if currentlabel not in labelCounts.keys():
            labelCounts[currentlabel] = 0
        labelCounts[currentlabel] += 1
    Ent = 0.0
    for key in labelCounts:
        p = float(labelCounts[key]) / numEntries
        Ent = Ent - p * log(p, 2)  # 以2为底求对数
    return Ent


# ID3算法
def ID3_chooseBestFeatureToSplit(dataset):
    zengyi = []

    numFeatures = len(dataset[0]) - 1
    baseEnt = jisuanEnt(dataset)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):  # 遍历所有特征
        # for example in dataset:
        # featList=example[i]
        featList = [example[i] for example in dataset]
        uniqueVals = set(featList)  # 将特征列表创建成为set集合，元素不可重复。创建唯一的分类标签列表
        newEnt = 0.0
        for value in uniqueVals:  # 计算每种划分方式的信息熵
            subdataset = splitdataset(dataset, i, value)
            p = len(subdataset) / float(len(dataset))
            newEnt += p * jisuanEnt(subdataset)
        infoGain = baseEnt - newEnt
        # print(u"ID3中第%d个特征的信息增益为：%.3f" % (i, infoGain))
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain  # 计算最好的信息增益
            bestFeature = i
        zengyi.append(infoGain)
    return zengyi


# C4.5算法
def C45_chooseBestFeatureToSplit(dataset):
    zengyi = []

    numFeatures = len(dataset[0]) - 1
    baseEnt = jisuanEnt(dataset)
    bestInfoGain_ratio = 0.0
    bestFeature = -1
    for i in range(numFeatures):  # 遍历所有特征
        featList = [example[i] for example in dataset]
        uniqueVals = set(featList)  # 将特征列表创建成为set集合，元素不可重复。创建唯一的分类标签列表
        newEnt = 0.0
        IV = 0.0
        for value in uniqueVals:  # 计算每种划分方式的信息熵
            subdataset = splitdataset(dataset, i, value)
            p = len(subdataset) / float(len(dataset))
            newEnt += p * jisuanEnt(subdataset)
            IV = IV - p * log(p, 2)
        infoGain = baseEnt - newEnt
        if (IV == 0):  # fix the overflow bug
            continue
        infoGain_ratio = infoGain / IV  # 这个feature的infoGain_ratio
        # print(u"C4.5中第%d个特征的信息增益率为：%.3f" % (i, infoGain_ratio))
        if (infoGain_ratio > bestInfoGain_ratio):  # 选择最大的gain ratio
            bestInfoGain_ratio = infoGain_ratio
            bestFeature = i  # 选择最大的gain ratio对应的feature
        zengyi.append(infoGain_ratio)
    return zengyi


# CART算法
def CART_chooseBestFeatureToSplit(dataset):
    zengyi = []

    numFeatures = len(dataset[0]) - 1
    bestGini = 999999.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataset]
        uniqueVals = set(featList)
        gini = 0.0
        for value in uniqueVals:
            subdataset = splitdataset(dataset, i, value)
            p = len(subdataset) / float(len(dataset))
            subp = len(splitdataset(subdataset, -1, '0')) / float(len(subdataset))
        gini += p * (1.0 - pow(subp, 2) - pow(1 - subp, 2))
        # print(u"CART中第%d个特征的基尼值为：%.3f" % (i, gini))
        if (gini < bestGini):
            bestGini = gini
            bestFeature = i

        zengyi.append(gini)

    return zengyi


# 划分数据集
def splitdataset(dataset, axis, value):
    retdataset = []  # 创建返回的数据集列表
    for featVec in dataset:  # 抽取符合划分特征的值
        if featVec[axis] == value:
            reducedfeatVec = featVec[:axis]  # 去掉axis特征
            reducedfeatVec.extend(featVec[axis + 1:])  # 将符合条件的特征添加到返回的数据集列表
            retdataset.append(reducedfeatVec)
    return retdataset

def autoNorm(dataSet):
    # 获得数据的最小值
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    # 最大值和最小值的范围
    ranges = maxVals - minVals
    # shape(dataSet)返回dataSet的矩阵行列数
    normDataSet = np.zeros(np.shape(dataSet))
    # 返回dataSet的行数
    m = dataSet.shape[0]
    # 原始值减去最小值
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    # 除以最大和最小值的差,得到归一化数据
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    # 返回归一化数据结果,数据范围,最小值
    return normDataSet, ranges, minVals


if __name__ == '__main__':
    train = pd.read_csv('cmc_train.csv')
    train = train.drop(columns=['Unnamed: 0'])
    test = pd.read_csv('test.csv')
    test = test.drop(columns=['Unnamed: 0'])

    train_y = train['1.2'].values.tolist()
    train = train.drop(columns=['1.2'])

    # 标签
    labels = ['24', '2', '3', '3.1', '1', '1.1', '2.1', '3.2', '0']

    dataSets = train.values
    dataSets, ranges_x, minVals_x = autoNorm(dataSets)
    dataSets=pd.DataFrame(dataSets,columns=labels)
    dataSets['1.2']=train_y

    # print(dataSets)
    # test_cnt = test.values


    # test_cnt, ranges_y, minVals_y = autoNorm(test_cnt)

    print(ID3_chooseBestFeatureToSplit(dataSets.values.tolist()))
    print(C45_chooseBestFeatureToSplit(dataSets.values.tolist()))
    print(CART_chooseBestFeatureToSplit(dataSets.values.tolist()))

    """
    [0.09827542219198349,
     0.060622044887663984, 
     0.04072441733137455, 
     0.11356575441032546, 
     0.009094221095042654, 
     0.003067720381586092, 
     0.028752402267523847, 
     0.04386051129049262, 
     0.019985660632640956]
    [0.019923978615616223, 0.032413147256928114, 0.027661892714145386, 0.03660197389131727, 0.014857152521957103, 0.003858572277571845, 0.01705840503558662, 0.024723874045163005, 0.050501986695184]
    """





