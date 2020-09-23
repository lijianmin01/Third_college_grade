import matplotlib.pyplot as plt
import numpy as np

# 创建距离（计算质心和样本点距离）
def euclDistance(v1,v2):
    return np.sqrt(np.sum(np.power(v2-v1,2)))


def kMeans(dataSet, k):
    n = dataSet.shape[1]
    numSamples = len(dataSet)
    clusterAssment = np.zeros((numSamples, n))
    centroids = np.empty((k, n))
    for i in range(n):
        centroids[:, i] = dataSet[:, i].min() + dataSet[:, i].ptp() * np.random.rand(k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False

        for i in range(numSamples):
            minIndex = 0
            minDist = 99999
            for j in range(k):
                distance = euclDistance(dataSet[i], centroids[j])
                if distance < minDist:
                    minDist = distance
                    minIndex = j
            if clusterAssment[i, 0] != minIndex:
                clusterAssment[i] = minIndex, minDist
                clusterChanged = True

    # 计算出每个样本的类别
    y_labels = []
    for i in range(numSamples):
        y_labels.append(int(clusterAssment[i][0]))

    # 对每一个簇，计算簇中所有的均值，并将均值作为质心
    sum_np = np.zeros((k, 2))
    count_np = np.zeros(k)
    avg_np = np.zeros((k, 2))
    # print(numSamples)
    for i in range(numSamples):
        cnt_i = int(clusterAssment[i, 0])
        # print(cnt_i)
        sum_np[cnt_i] += dataSet[i]
        count_np[cnt_i] += 1

    # 求每个簇的均值
    for i in range(k):
        avg_np[i] = sum_np[i] / count_np[i]
        # print(sum_np[i]/count_np[i])

    return y_labels, avg_np



def main():
    data = np.loadtxt('testSet.txt')
    y_labels,avg_np = kMeans(data,4)
    print(y_labels)
    print(avg_np)

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

    plt.figure()
    for i in range(4):
        plt.scatter(class_x[i],class_y[i])

    plt.show()


if __name__ == '__main__':
    main()