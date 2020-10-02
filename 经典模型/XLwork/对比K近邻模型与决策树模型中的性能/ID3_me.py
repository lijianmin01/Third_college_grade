import operator
import numpy as np
import pandas as pd
from math import log
import time

# 计算出数据集的经验熵
def calcShannonEnt(dataSet):
    numEntires = len(dataSet)  # 返回数据集的行数
    labelCounts = {}  # 保存每个标签(Label)出现次数的字典
    for featVec in dataSet:  # 对每组特征向量进行统计
        currentLabel = featVec[-1]  # 提取标签(Label)信息
        if currentLabel not in labelCounts.keys():  # 如果标签(Label)没有放入统计次数的字典,添加进去
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1  # Label计数
    shannonEnt = 0.0  # 经验熵(香农熵)
    for key in labelCounts:  # 计算香农熵
        prob = float(labelCounts[key]) / numEntires  # 选择该标签(Label)的概率
        shannonEnt -= prob * log(prob, 2)  # 利用公式计算
    return shannonEnt  # 返回经验熵(香农熵)

def createDataSet():
    # 特征标签
    labels = ['top_left_square','top_middle_square','top_right_square','middle_left_square','middle_middle_square',
              'middle_right_square','bottom_left_square','bottom_middle_square','bottom_right_square']

    dataSets = pd.read_csv('tic_tac_toe_weka_dataset.csv').values

    return dataSets,labels

"""函数说明：分层划分数据集
Parameters:
    dataSet - 带划分的数据集
    k       - 将数据集划分为几份
return：
    划分完数据的下标
"""
def split_data(dataSets,k):
    dataSets[dataSets == 'positive'] = 0
    dataSets[dataSets == 'negative'] = 1
    yy=[]

    for data in dataSets:
        yy.append(int(data[-1]))
    class_list = []
    for i in range(k):
        class_list.append([])

    # cnt_array = np.array([i for i in range(len(yy))])
    # class_0 = cnt_array[np.where(yy[cnt_array] == 0)]
    # class_1 = cnt_array[np.where(yy[cnt_array] == 1)]
    class_0 , class_1 = [],[]
    for j in range(len(yy)):
        if (yy[j]-0)==0:
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


"""函数说明:按照给定特征划分数据集
Parameters:
	dataSet - 待划分的数据集
	axis - 划分数据集的特征
	value - 需要返回的特征的值
"""
def splitDataSet(dataSet, axis, value):
    retDataSet = []  # 创建返回的数据集列表
    for featVec in dataSet:  # 遍历数据集
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]  # 去掉axis特征
            reducedFeatVec.extend(featVec[axis + 1:])  # 将符合条件的添加到返回的数据集
            retDataSet.append(reducedFeatVec)
    return retDataSet  # 返回划分后的数据集

"""
函数说明:选择最优特征
Parameters:
	dataSet - 数据集
Returns:
	bestFeature - 信息增益最大的(最优)特征的索引值
"""
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1  # 特征数量
    baseEntropy = calcShannonEnt(dataSet)  # 计算数据集的香农熵
    bestInfoGain = 0.0  # 信息增益
    bestFeature = -1  # 最优特征的索引值
    for i in range(numFeatures):  # 遍历所有特征
        # 获取dataSet的第i个所有特征
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)  # 创建set集合{},元素不可重复
        newEntropy = 0.0  # 经验条件熵
        for value in uniqueVals:  # 计算信息增益
            subDataSet = splitDataSet(dataSet, i, value)  # subDataSet划分后的子集
            prob = len(subDataSet) / float(len(dataSet))  # 计算子集的概率
            newEntropy += prob * calcShannonEnt(subDataSet)  # 根据公式计算经验条件熵
        infoGain = baseEntropy - newEntropy  # 信息增益
        # print("第%d个特征的增益为%.3f" % (i, infoGain))			#打印每个特征的信息增益
        if (infoGain > bestInfoGain):  # 计算信息增益
            bestInfoGain = infoGain  # 更新信息增益，找到最大的信息增益
            bestFeature = i  # 记录信息增益最大的特征的索引值
    return bestFeature  # 返回信息增益最大的特征的索引值

"""
函数说明:统计classList中出现此处最多的元素(类标签)
Parameters:
	classList - 类标签列表
Returns:
	sortedClassCount[0][0] - 出现此处最多的元素(类标签)
"""
def majorityCnt(classList):
    classCount = {}
    for vote in classList:  # 统计classList中每个元素出现的次数
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)  # 根据字典的值降序排序
    return sortedClassCount[0][0]  # 返回classList中出现次数最多的元素

"""
函数说明:创建决策树
Parameters:
	dataSet - 训练数据集
	labels - 分类属性标签
	featLabels - 存储选择的最优特征标签
Returns:
	myTree - 决策树
"""
def createTree(dataSet, labels, featLabels):
    classList = [example[-1] for example in dataSet]  # 取分类标签(是否放贷:yes or no)
    if classList.count(classList[0]) == len(classList):  # 如果类别完全相同则停止继续划分
        return classList[0]
    if len(dataSet[0]) == 1 or len(labels) == 0:  # 遍历完所有特征时返回出现次数最多的类标签
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)  # 选择最优特征
    bestFeatLabel = labels[bestFeat]  # 最优特征的标签
    featLabels.append(bestFeatLabel)
    myTree = {bestFeatLabel: {}}  # 根据最优特征的标签生成树
    del (labels[bestFeat])  # 删除已经使用特征标签
    featValues = [example[bestFeat] for example in dataSet]  # 得到训练集中所有最优特征的属性值
    uniqueVals = set(featValues)  # 去掉重复的属性值
    for value in uniqueVals:  # 遍历特征，创建决策树。
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels, featLabels)

    return myTree

"""
函数说明:使用决策树分类
Parameters:
	inputTree - 已经生成的决策树
	featLabels - 存储选择的最优特征标签
	testVec - 测试数据列表，顺序对应最优特征标签
Returns:
	classLabel - 分类结果
"""


def classify(input_tree:dict, feat_labels:list, test_vec:list):
    # get the first feature and its index in feat_labels
    first_feat = list(input_tree.keys())[0]
    feat_ind = feat_labels.index(first_feat)
    # get the corresponding branch
    second_dict = input_tree[first_feat][test_vec[feat_ind]]
    if type(second_dict) == dict:
        ret = classify(second_dict, feat_labels, test_vec)
        return ret
    else:
        return second_dict


"""函数说明:根据k进行5折交叉验证
Parameters:
	dataSet - 待划分的数据集
	labels - 特征标签
"""


def main():
    dataSets , labels = createDataSet()
    k = 5
    class_list = split_data(dataSets,k)
    # 对于每个k   开始交叉验证数据 5 折交叉验证
    # 建立矩阵，用来保存每个ID3树的正确率,以及预测所需的时间
    accuracy_rate_list = np.zeros((k, 2))
    for i in range(1):
        train = []
        featLabels = []
        test = dataSets[class_list[i]]
        for j in range(k):
            if i!=j:
                train.extend(dataSets[class_list[j]].tolist())

        # print(train)
        myTree = createTree(train,labels,featLabels)
        print(myTree)
        # 预测数据
        test_data = test[:,:-1]
        for one_test in test_data:
            result = classify(myTree, featLabels, one_test)
            print(result)



if __name__ == '__main__':
    main()





