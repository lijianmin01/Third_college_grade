import pandas as pd
import numpy as np


# 获取数据
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


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
    # print(features)
    # print(labels)
    # 对所有特征进行热独立编码
    features = pd.get_dummies(features)

    X=features
    y=labels

    # 测试数据
    test = test.values[:, 1:]
    test = pd.DataFrame(test)
    test = pd.get_dummies(test)

    #pipe = Pipeline([('select', SelectKBest(k=20)),('classify', RandomForestClassifier(random_state=10, max_features='sqrt'))])

    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('pca', PCA()),
        ('randomforestclassifier', RandomForestClassifier())
    ])

    pipeline.fit(X,y)

    prv = pipeline.predict(test)

    result = np.zeros((300, 1))


    id = [i for i in range(300)]

    result[:, 0] = prv
    # print(result)

    result = pd.DataFrame(result, columns=['y'])
    result.to_csv('2.csv')