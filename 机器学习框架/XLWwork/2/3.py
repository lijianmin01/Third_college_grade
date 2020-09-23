import matplotlib.pyplot as plt
import numpy as np

# 创建距离（计算质心和样本点距离）
import seaborn


def euclDistance(v1,v2):
    return np.sqrt(np.sum(np.power(v2-v1,2)))


def KMeans(dataSet, k):
    # 创建k个点作为初始的质心点
    # 生成一个矩阵，矩阵为k个点，范围在最大值和最小值之间，生成的点为质心点
    numSamples = dataSet.shape[0]
    # 保留样本点的最近的质心和距离
    clusterAssment = np.zeros((numSamples, 2))
    n = data.shape[1]
    centroids = np.empty((k, n))
    for i in range(n):
        centroids[:, i] = dataSet[:, i].min() + dataSet[:, i].ptp() * np.random.rand(k)

    # 当任意一个点的簇分配结果发生改变时
    flag = True
    while flag:
        flag = False
        minIndex = 0
        # 对数据集中的每一个数据点
        for i in range(numSamples):
            minDistance = 0x3f3f3f3f
            # 对每一个质心
            for j in range(k):
                # 计算质心与数据点的距离
                distance = euclDistance(centroids[j, :], dataSet[i, :])
                # 判断该质心与样本的距离是不是所有质心中最近的
                if distance < minDistance:
                    minDistance = distance
                    minIndex = j
            # 将数据点分配到最近的簇里面去
            if clusterAssment[i, 0] != minIndex:
                clusterAssment[i, :] = minIndex, minDistance
                flag = True
        # 对每一个簇，计算簇中所有点的均值，并将均值作为质心
        for j in range(k):
            centroids[j, :] = np.mean(dataSet[np.where(clusterAssment[:, 0] == j)], axis=0)

    return centroids, clusterAssment

data = np.loadtxt('testSet.txt')
avg_np,y_labels = KMeans(data,4)


y_labels = y_labels[:,0]

y_labels = [int(i) for i in y_labels]

class_x = [[],[],[],[]]

class_y = [[],[],[],[]]



for i in range(len(data)):
    if y_labels[i]==0:
        class_x[0].append(data[i][0])
        class_y[0].append(data[i][1])
    elif y_labels[i]==1:
        class_x[1].append(data[i][0])
        class_y[1].append(data[i][1])
    elif y_labels[i]==2:
        class_x[2].append(data[i][0])
        class_y[2].append(data[i][1])
    else:
        class_x[3].append(data[i][0])
        class_y[3].append(data[i][1])

# 质心
z_x = []
z_y = []

for i in avg_np:
    z_x.append(i[0])
    z_y.append(i[1])

plt.figure()

plt.scatter(z_x,z_y,marker='+',color='k',alpha='0.8',s=100)
plt.scatter(class_x[0],class_y[0],marker='*',color='b')
plt.scatter(class_x[1],class_y[1],marker='o',alpha=0.4,color='k')
plt.scatter(class_x[2],class_y[2],marker='D',color='r',alpha=0.5)
plt.scatter(class_x[3],class_y[3],marker='<',alpha=0.8,color='xkcd:sky blue')
plt.xlabel('x')

plt.title('DataSet')
plt.show()

