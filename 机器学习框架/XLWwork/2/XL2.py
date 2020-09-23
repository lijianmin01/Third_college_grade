import matplotlib.pyplot as plt
import numpy as np

# 读取数据集
x = []
y = []
with open('iris.txt','r') as f:
    for line in f:
        # 去掉空白
        line = line.strip()
        data = line.split(" ")
        x.append(float(data[0]))
        y.append(float(data[1]))

# 记录标签
labels=np.loadtxt('iris_target.txt')
x = np.array(x)
y = np.array(y)


plt.figure()
x_1 = []
x_2 = []
x_3 = []

y_1 = []
y_2 = []
y_3 = []

for i in range(len(labels)):
    if(labels[i]==0):
        x_1.append(x[i])
        y_1.append(y[i])
    elif(labels[i]==1):
        x_2.append(x[i])
        y_2.append(y[i])
    else:
        x_3.append(x[i])
        y_3.append(y[i])

plt.scatter(x_1,y_1,color='b')
plt.scatter(x_2,y_2,color='r')
plt.scatter(x_3,y_3,color='g')
plt.xticks(np.arange(4.5,8.5,0.5))
plt.yticks(np.arange(2.0,4.5,0.5))
plt.xlabel("sepal length(cm)")
plt.ylabel("sepal width(cm)")

class_labels =['setosa','versicolor','virginica']
plt.legend(class_labels, loc=2)

plt.show()



