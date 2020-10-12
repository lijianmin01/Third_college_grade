
import numpy as np
import operator
import pandas as pd

"""
函数说明:kNN算法,分类器
Parameters:
	inX - 用于分类的数据(测试集)
	dataSet - 用于训练的数据(训练集)
	labes - 分类标签
	k - kNN算法参数,选择距离最小的k个点
Returns:
	sortedClassCount[0][0] - 分类结果

"""


def classify0(inX, dataSet, labels, k):
    # numpy函数shape[0]返回dataSet的行数
    dataSetSize = dataSet.shape[0]
    # 在列向量方向上重复inX共1次(横向),行向量方向上重复inX共dataSetSize次(纵向)
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    # 二维特征相减后平方
    sqDiffMat = (diffMat ** 2)**(0.5)
    # sum()所有元素相加,sum(0)列相加,sum(1)行相加
    # sqDistances = sqDiffMat.sum(axis=1)
    distances = []
    for dis_cnt in sqDiffMat:
        sum=0.0
        zengyi1 = [0.09827542219198349,  0.060622044887663984, 0.04072441733137455,  0.11356575441032546, 0.009094221095042654, 0.003067720381586092, 0.028752402267523847, 0.04386051129049262, 0.019985660632640956]

        for i in range(9):
            sum+=zengyi1[i]*dis_cnt[i]
        distances.append(sum)
    distances = np.array(distances).T
    # 开方,计算出距离
    # distances = sqDistances ** 0.5
    # 返回distances中元素从小到大排序后的索引值
    sortedDistIndices = distances.argsort()
    # 定一个记录类别次数的字典
    classCount = {}
    for i in range(k):
        # 取出前k个元素的类别
        voteIlabel = labels[sortedDistIndices[i]]
        # dict.get(key,default=None),字典的get()方法,返回指定键的值,如果值不在字典中返回默认值。
        # 计算类别次数
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # python3中用items()替换python2中的iteritems()
    # key=operator.itemgetter(1)根据字典的值进行排序
    # key=operator.itemgetter(0)根据字典的键进行排序
    # reverse降序排序字典
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    # print(sortedClassCount)
    # 返回次数最多的类别,即所要分类的类别
    return sortedClassCount[0][0]


"""
函数说明:打开并解析文件，对数据进行分类：1代表不喜欢,2代表魅力一般,3代表极具魅力
Parameters:
	filename - 文件名
Returns:
	returnMat - 特征矩阵
	classLabelVector - 分类Label向量
Modify:
	2017-03-24
"""


def file2matrix(filename):
    # 打开文件,此次应指定编码，

    fr = open(filename, 'r', encoding='utf-8')
    # 读取文件所有内容
    arrayOLines = fr.readlines()
    # 针对有BOM的UTF-8文本，应该去掉BOM，否则后面会引发错误。
    arrayOLines[0] = arrayOLines[0].lstrip('\ufeff')
    # 得到文件行数
    numberOfLines = len(arrayOLines)
    # 返回的NumPy矩阵,解析完成的数据:numberOfLines行,3列
    returnMat = np.zeros((numberOfLines, 3))
    # 返回的分类标签向量
    classLabelVector = []
    # 行的索引值
    index = 0

    for line in arrayOLines:
        # s.strip(rm)，当rm空时,默认删除空白符(包括'\n','\r','\t',' ')
        line = line.strip()
        # 使用s.split(str="",num=string,cout(str))将字符串根据'\t'分隔符进行切片。
        listFromLine = line.split('\t')
        # 将数据前三列提取出来,存放到returnMat的NumPy矩阵中,也就是特征矩阵
        returnMat[index, :] = listFromLine[0:3]
        # 根据文本中标记的喜欢的程度进行分类,1代表不喜欢,2代表魅力一般,3代表极具魅力
        # 对于datingTestSet2.txt  最后的标签是已经经过处理的 标签已经改为了1, 2, 3
        if listFromLine[-1] == 'didntLike':
            classLabelVector.append(1)
        elif listFromLine[-1] == 'smallDoses':
            classLabelVector.append(2)
        elif listFromLine[-1] == 'largeDoses':
            classLabelVector.append(3)
        index += 1
    return returnMat, classLabelVector





"""
函数说明:对数据进行归一化
Parameters:
	dataSet - 特征矩阵
Returns:
	normDataSet - 归一化后的特征矩阵
	ranges - 数据范围
	minVals - 数据最小值
Modify:
	2017-03-24
"""


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


"""
函数说明:分类器测试函数
取百分之十的数据作为测试数据，检测分类器的正确性
Parameters:
	无
Returns:
	无
Modify:
	2017-03-24
"""


def datingClassTest():
    train = pd.read_csv('cmc_train.csv')
    train = train.drop(columns=['Unnamed: 0'])
    test = pd.read_csv('test.csv')
    test = test.drop(columns=['Unnamed: 0'])

    train_y = train['1.2'].values.tolist()
    train = train.drop(columns=['1.2'])

    dataSets = train.values
    labels = ['24', '2', '3', '3.1', '1', '1.1', '2.1', '3.2', '0']
    test_cnt = test.values

    dataSets, ranges_x, minVals_x = autoNorm(dataSets)
    test_cnt,ranges_y, minVals_y  = autoNorm(test_cnt)

    # 获取行数，即样本个数
    m = dataSets.shape[0]


    k_list=[42]
    for k in k_list:
        prv = []
        for i in range(len(test_cnt)):
            classifierResult = classify0(test_cnt[i],dataSets,train_y,k)
            prv.append(classifierResult)

        result = pd.DataFrame(prv, columns=['y'])
        result.to_csv('knn_{}_ID3.csv'.format(k))




if __name__ == '__main__':
    datingClassTest()
