import pandas as pd
import numpy as np


from sklearn.tree import DecisionTreeRegressor


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
    features, labels = split_train(train)
    features = pd.get_dummies(features)

    X=features
    y=labels

    # 测试数据
    test = test.values[:, 1:]
    test = pd.DataFrame(test)
    test = pd.get_dummies(test)

    cls = DecisionTreeRegressor(max_depth=8)
    cls.fit(X,y)
    prv = cls.predict(test)


    result = np.zeros((300, 1))


    id = [i for i in range(300)]

    result[:, 0] = prv
    # print(result)

    result = pd.DataFrame(result, columns=['y'])
    result.to_csv('5.csv')