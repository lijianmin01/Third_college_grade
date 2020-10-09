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


# 划分数据集
def splitdataset(dataset, axis, value):
    retdataset = []  # 创建返回的数据集列表
    for featVec in dataset:  # 抽取符合划分特征的值
        if featVec[axis] == value:
            reducedfeatVec = featVec[:axis]  # 去掉axis特征
            reducedfeatVec.extend(featVec[axis + 1:])  # 将符合条件的特征添加到返回的数据集列表
            retdataset.append(reducedfeatVec)
    return retdataset


'''
选择最好的数据集划分方式
ID3算法:以信息增益为准则选择划分属性
C4.5算法：使用“增益率”来选择划分属性
'''


# ID3算法
def ID3_chooseBestFeatureToSplit(dataset):
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
    return bestFeature


# C4.5算法
def C45_chooseBestFeatureToSplit(dataset):
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
    return bestFeature


# CART算法
def CART_chooseBestFeatureToSplit(dataset):
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
    return bestFeature


def majorityCnt(classList):
    '''
    数据集已经处理了所有属性，但是类标签依然不是唯一的，
    此时我们需要决定如何定义该叶子节点，在这种情况下，我们通常会采用多数表决的方法决定该叶子节点的分类
    '''
    classCont = {}
    for vote in classList:
        if vote not in classCont.keys():
            classCont[vote] = 0
        classCont[vote] += 1
    sortedClassCont = sorted(classCont.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCont[0][0]


# 利用ID3算法创建决策树
def ID3_createTree(dataset, labels):
    classList = [example[-1] for example in dataset]
    if classList.count(classList[0]) == len(classList):
        # 类别完全相同，停止划分
        return classList[0]
    if len(dataset[0]) == 1:
        # 遍历完所有特征时返回出现次数最多的
        return majorityCnt(classList)
    bestFeat = ID3_chooseBestFeatureToSplit(dataset)
    bestFeatLabel = labels[bestFeat]
    # print(u"此时最优索引为：" + (bestFeatLabel))
    ID3Tree = {bestFeatLabel: {}}
    del (labels[bestFeat])
    # 得到列表包括节点所有的属性值
    featValues = [example[bestFeat] for example in dataset]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        ID3Tree[bestFeatLabel][value] = ID3_createTree(splitdataset(dataset, bestFeat, value), subLabels)
    return ID3Tree


def C45_createTree(dataset, labels):
    classList = [example[-1] for example in dataset]
    if classList.count(classList[0]) == len(classList):
        # 类别完全相同，停止划分
        return classList[0]
    if len(dataset[0]) == 1:
        # 遍历完所有特征时返回出现次数最多的
        return majorityCnt(classList)
    bestFeat = C45_chooseBestFeatureToSplit(dataset)
    bestFeatLabel = labels[bestFeat]
    # print(u"此时最优索引为：" + (bestFeatLabel))
    C45Tree = {bestFeatLabel: {}}
    del (labels[bestFeat])
    # 得到列表包括节点所有的属性值
    featValues = [example[bestFeat] for example in dataset]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        C45Tree[bestFeatLabel][value] = C45_createTree(splitdataset(dataset, bestFeat, value), subLabels)
    return C45Tree


def CART_createTree(dataset, labels):
    classList = [example[-1] for example in dataset]
    if classList.count(classList[0]) == len(classList):
        # 类别完全相同，停止划分
        return classList[0]
    if len(dataset[0]) == 1:
        # 遍历完所有特征时返回出现次数最多的
        return majorityCnt(classList)
    bestFeat = CART_chooseBestFeatureToSplit(dataset)
    # print(u"此时最优索引为："+str(bestFeat))
    bestFeatLabel = labels[bestFeat]
    # print(u"此时最优索引为：" + (bestFeatLabel))
    CARTTree = {bestFeatLabel: {}}
    del (labels[bestFeat])
    # 得到列表包括节点所有的属性值
    featValues = [example[bestFeat] for example in dataset]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        CARTTree[bestFeatLabel][value] = CART_createTree(splitdataset(dataset, bestFeat, value), subLabels)
    return CARTTree


def classify(inputTree, featLabels, testVec):
    """
    输入：决策树，分类标签，测试数据
    输出：决策结果
    描述：跑决策树
    """
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    classLabel = '0'
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel


def classifytest(inputTree, featLabels, testDataSet):
    """
    输入：决策树，分类标签，测试数据集
    输出：决策结果
    描述：跑决策树
    """
    classLabelAll = []
    for testVec in testDataSet:
        classLabelAll.append(classify(inputTree, featLabels, testVec))
    return classLabelAll



def create_data_set():
    # 特征标签
    labels = ['top_left_square','top_middle_square','top_right_square','middle_left_square','middle_middle_square','middle_right_square','bottom_left_square','bottom_middle_square','bottom_right_square']

    dataSets = pd.read_csv('tic_tac_toe_weka_dataset.csv').values
    # 对特征值
    dataSets[dataSets == 'o'] = 0
    dataSets[dataSets == 'x'] = 1
    dataSets[dataSets == 'b'] = 2
    # 对类别
    dataSets[dataSets == 'positive'] = '0'
    dataSets[dataSets == 'negative'] = '1'

    return dataSets.tolist(),labels

def split_data(dataSets,k):
    yy = []

    for data in dataSets:
        yy.append(data[-1])
    class_list = []
    for i in range(k):
        class_list.append([])

    # cnt_array = np.array([i for i in range(len(yy))])
    # class_0 = cnt_array[np.where(yy[cnt_array] == 0)]
    # class_1 = cnt_array[np.where(yy[cnt_array] == 1)]
    class_0 , class_1 = [],[]
    for j in range(len(yy)):
        if (yy[j])=='positive':
            class_0.append(j)
        else:
            class_1.append(j)

    # 各个类别的数量
    class_0_nums = len(class_0)
    class_1_nums = len(class_1)

    cnt = 0
    # 不放回随机抽样
    for i in range(class_0_nums):
        z = np.random.choice(class_0, 1)
        index = np.where(class_0 == z)
        class_list[cnt].append(int(z))
        class_0 = np.delete(class_0, index)
        cnt = (cnt + 1) % k

    cnt = 0
    for i in range(class_1_nums):
        z = np.random.choice(class_1, 1)
        index = np.where(class_1 == z)
        class_list[cnt].append(int(z))
        class_1 = np.delete(class_1, index)
        cnt = (cnt + 1) % k

    return class_list

# 计算正确率
def get_accuracy_rate(test_labels,test_prv):
    cnt = 0.0  # 预测正确的数量
    nums = len(test_labels) # 所有的样本数
    for i in range(nums):
        if(test_labels[i]==test_prv[i]):
            cnt+=1

    accuracy_rate = cnt/nums*1.0
    return accuracy_rate


if __name__ == '__main__':
    train = pd.read_csv('cmc_train.csv')
    train = train.drop(columns=['Unnamed: 0'])
    test = pd.read_csv('test.csv')
    test = test.drop(columns=['Unnamed: 0'])

    # 将年龄分为三段
    train['24'] = pd.qcut(train['24'], q=3, labels=['young', 'middle-aged', 'old'])
    train['24'].replace('young', 1, inplace=True)
    train['24'].replace('middle-aged', 2, inplace=True)
    train['24'].replace('old', 3, inplace=True)

    test['24'] = pd.qcut(test['24'], q=3, labels=['young', 'middle-aged', 'old'])
    test['24'].replace('young', 1, inplace=True)
    test['24'].replace('middle-aged', 2, inplace=True)
    test['24'].replace('old', 3, inplace=True)

    dataSets = train.values.tolist()
    labels = ['24','2','3','3.1','1','1.1','2.1','3.2','0']
    test_cnt = test.values.tolist()

    print(dataSets)
    print(labels)

    labels_cnt = labels[:]
    C45tree = CART_createTree(dataSets,labels_cnt)
    labels_cnt = labels[:]
    prv=classifytest(C45tree,labels_cnt,test_cnt)
    prv = [int(i) for i in prv]

    result = pd.DataFrame(prv, columns=['y'])
    result.to_csv('CART.csv')



