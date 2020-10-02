import operator
import numpy as np
import pandas as pd
import math
import time


# 获取数据
def get_data():
    dataSets = pd.read_csv('tic_tac_toe_weka_dataset.csv')
    # 观察数据特征
    # print(dataSets.info())
    # print(dataSets.describe())
    # print(dataSets)
    # 将数据转成np.array形式
    dataSets = dataSets.values
    # 将数据集中的数据进行替换  o->0   x->1   b->2
    # positive 0   negative  1
    # 对特征值
    dataSets[dataSets == 'o'] = 0
    dataSets[dataSets == 'x'] = 1
    dataSets[dataSets == 'b'] = 2
    # 对类别
    dataSets[dataSets == 'positive'] = 0
    dataSets[dataSets == 'negative'] = 1

    # 保存每个样本特征的值
    xx = []
    # 保存每个样本的类别
    yy = []

    for data in dataSets:
        xx.append(list(data[:-1]))
        yy.append(data[-1])

    # print(xx)
    # print(yy)

    return np.array(xx),np.array(yy)

# 分层随机划分数据
"""
    xx  --  特征集
    yy  --  样本集
    k   --  将数据划分成k份
    这里采用k折交叉验证 将数据分层划分成k份
    return k份数据的list
"""
def split_data(xx,yy,k):
    class_list = []
    for i in range(k):
        class_list.append([])

    cnt_array = np.array([i for i in range(len(yy))])
    # 算了，不想复杂了，直接当成两类别来随机划分吧
    class_0 = cnt_array[np.where(yy[cnt_array] == 0)]
    class_1 = cnt_array[np.where(yy[cnt_array] == 1)]

    # 各个类别的数量
    class_0_nums = len(class_0)
    class_1_nums = len(class_1)

    cnt = 0
    # 不放回随机抽样
    for i in range(class_0_nums):
        z = np.random.choice(class_0,1)
        index = np.where(class_0 == z)
        class_list[cnt].append(int(z))
        class_0 = np.delete(class_0,index)
        cnt = (cnt+1)%k

    cnt = 0
    for i in range(class_1_nums):
        z = np.random.choice(class_1, 1)
        index = np.where(class_1 == z)
        class_list[cnt].append(int(z))
        class_1 = np.delete(class_1, index)
        cnt = (cnt + 1) % k

    return class_list


# knn模型
# xx 代表各个样本的特征值  yy 代表各个样本的特征   k 不同的K值
# 默认使用绝对值距离  否则使用欧式距离
"""
knn算法，分类器
    intX --     用于分类的数据（测试集）
    xx   --     用于训练的数据（训练接）
    yy   --     分类标签（训练集）
    k    --     选择距离最小的k个点
    is_abs--    不同的距离度量（如绝对值距离、欧氏距离）
"""
# KNN预测模型
def my_knn(featers,labels,class_list,k,is_abs=True):
    sum_accuracy_rate=0.0
    start_time = time.time()
    for i in range(k):
        intX = featers[class_list[i]]
        intY_true = labels[class_list[i]]
        # print(intX)
        xx,yy = [],[]
        for j in range(k):
            if i != j:
                xx.extend(featers[class_list[j]].tolist())
                yy.extend(labels[class_list[j]])

        # xx = np.array(xx)
        # yy = np.array(yy)
        # # 训练集中一共有多少个训练样本
        # dataSetSize = xx.shape[0]
        # # 测试集中一共有多少个样本
        # testSetSize = intX.shape[0]
        # 记录每个测试样本的类别
        intY = []
        print(xx)
        xx = np.array(xx)
        # 对数据进行归一化处理
        xx = auto_norm(xx)
        intX = auto_norm(intX)

        # 下面开始对每个样本进行预测
        for test_data in intX:
            # distances 记录样本与训练集每个样本之间的距离
            distances = None
            if (is_abs):
                distances = abs_distance(xx, test_data)
            else:
                distances = euclidean_distance(xx, test_data)

            # 返回distances中元素从小到大排序后的索引值
            sorted_dist_indices = distances.argsort()
            # 记录在前k个样本中出现的各个类别的次数
            class_count = {}
            for i in range(k):
                # 取出前k个元素的类别
                voteIlabel = yy[sorted_dist_indices[i]]
                # dict.get(key,default=None),字典的get()方法,返回指定键的值,如果值不在字典中返回默认值。
                # 计算类别次数
                class_count[voteIlabel] = class_count.get(voteIlabel, 0) + 1

            """
            python3中用items()替换python2中的iteritems()
            #key=operator.itemgetter(1)根据字典的值进行排序
            #key=operator.itemgetter(0)根据字典的键进行排序
            #reverse降序排序字典
            """
            sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
            # 记录出现次数最多的类别，及预测的类别
            intY.append(sorted_class_count[0][0])

        sum_accuracy_rate+=get_accuracy_rate(intY_true,intY)

    mean_accuracy_rate = sum_accuracy_rate/k
    end_time = time.time()

    # 返回平均预测正确率，程序预测需要的时间
    return mean_accuracy_rate,(end_time-start_time)



# 对样本数据进行归一化处理
def auto_norm(xx):
    print(xx)
    # 获取数据的最大、最小值
    min_vals = xx.min()
    max_vals = xx.max()
    # 最大~最小的范围
    ranges = max_vals-min_vals
    # 初始化用来记录处理之后的数据
    norm_data = np.zeros(np.shape(xx))
    # xx中有多少个样本
    m = xx.shape[0]
    """
    np.tile(a,(2,1))第一个参数为Y轴扩大倍数，第二个为X轴扩大倍数。
    这里其实用不着tile函数了，因为矩阵具有广播性质
    为了避免出错,so接着用吧 
    """
    # 分子（原始值减去最小值）
    norm_data = xx-np.tile(min_vals,(m,1))
    norm_data = norm_data/np.tile(ranges,(m,1))
    # 返回归一化数据结果
    return norm_data

# 绝对值距离
def abs_distance(dataSet,one_test_data):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(one_test_data,(dataSetSize,1))-dataSet
    # 特征相减后取绝对值
    sqDiffMat = abs(diffMat)
    # sum()所有元素相加,sum(0)列相加,sum(1)行相加
    sqDistances = sqDiffMat.sum(axis=1)
    return sqDistances
# 欧氏距离
def euclidean_distance(dataSet,one_test_data):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(one_test_data, (dataSetSize, 1)) - dataSet
    # 特征相减后平方
    sqDiffMat = diffMat**2
    # sum()所有元素相加,sum(0)列相加,sum(1)行相加
    sqDistances = sqDiffMat.sum(axis=1)
    # 开方
    sqDistances = np.sqrt(sqDistances)
    return sqDistances

# 计算正确率
def get_accuracy_rate(test_labels,test_prv):
    cnt = 0.0  # 预测正确的数量
    nums = len(test_labels) # 所有的样本数
    for i in range(nums):
        if(test_labels[i]==test_prv[i]):
            cnt+=1

    accuracy_rate = cnt/nums*1.0
    return accuracy_rate

def main():
    # 获得数据
    xx,yy = get_data()
    # 分层随机划分数据 将数据划分成5份
    class_list = split_data(xx,yy,5)

    k = 1
    accuracy_rate, time = my_knn(xx, yy, class_list, k)
    print(accuracy_rate, time)

    # # K值取值范围
    # k_list = [1, 3, 5, 7, 10, 15]
    # # 建立矩阵，用来保存正确率,以及预测所需的时间
    # accuracy_rate_list = np.zeros((6, 4))
    # for i in range(len(k_list)):
    #     k = k_list[i]
    #     accuracy_rate, time = my_knn(xx, yy, class_list, k)
    #     accuracy_rate_list[i][0] = accuracy_rate
    #     accuracy_rate_list[i][1] = time
    #
    #     accuracy_rate, time = my_knn(xx, yy, class_list, k,is_abs=False)
    #     accuracy_rate_list[i][2] = accuracy_rate
    #     accuracy_rate_list[i][3] = time
    #
    # result = pd.DataFrame(accuracy_rate_list, index=k_list, columns=['绝对值距离', '绝对值距离所需的时间', '欧式距离', '欧式距离所需的时间'])
    # print(result)


if __name__ == '__main__':
    main()

