import pandas as pd

from sklearn import tree

import matplotlib.pyplot as plt


def get_date():
    train = pd.read_csv('cmc_train.csv')
    test = pd.read_csv('test.csv')

    return train,test

# 分离训练数据  特征+类别
def split_train(train):
    labels = train['1.2']
    del train['1.2']
    features = train.values[:,1:]
    features = pd.DataFrame(features)
    return features,labels

if __name__ == '__main__':
    train, test = get_date()
    Xtrain, Ytrain = split_train(train)

    # 对所有特征进行热独立编码
    Xtrain = pd.get_dummies(Xtrain)

    Xtest,Ytest = split_train(test)
    Xtest = pd.get_dummies(Xtest)

    # 用学习曲线确定最优max_depth取值

    test = []
    for i in range(20):
        clf = tree.DecisionTreeClassifier(max_depth=i + 1
                                          , criterion="entropy"
                                          , random_state=30
                                          , splitter="random"
                                          )
        clf = clf.fit(Xtrain, Ytrain)
        score = clf.score(Xtest, Ytest)
        test.append(score)
    plt.plot(range(1, 21), test, color="red", label="max_depth")
    plt.legend()
    plt.show()