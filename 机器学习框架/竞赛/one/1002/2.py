# 导入相关的库
#首先引入需要的库和函数
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer
from sklearn.metrics import accuracy_score,roc_auc_score
from time import time
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier

import pandas as pd
import numpy as np


# 定义通用函数框架(通过训练数据，得到模型)
def fit_model(alg,parameters,features,labels):
    x = features.values.tolist()
    y = labels.values.tolist() # 由于数据较少，使用全部数据进行网格搜索
    scorer=make_scorer(roc_auc_score)  #使用roc_auc_score作为评分标准
    grid = GridSearchCV(alg,parameters,scoring=scorer,cv=5)##使用网格搜索，出入参数

    x = np.array(x)
    y = np.array(y)
    start = time() # 计时
    grid = grid.fit(x,y) # 模型训练
    end = time()
    t = round(end-start,3)
    print (grid.best_params_)  #输出最佳参数
    #print ('searching time for {} is {} s'.format(alg.__class__.__name__,t)) #输出搜索时间
    print("time"+str(t))
    return grid #返回训练好的模型

# 获取数据
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
    # 列出需要使用的算法
    alg1 = DecisionTreeClassifier(random_state=29)
    alg2 = SVC(probability=True, random_state=29)  # 由于使用roc_auc_score作为评分标准，需将SVC中的probability参数设置为True
    alg3 = RandomForestClassifier(random_state=29)
    alg4 = AdaBoostClassifier(random_state=29)
    alg5 = KNeighborsClassifier(n_jobs=-1)

    # 列出需要调整的参数范围
    parameters1 = {'max_depth': range(1, 10), 'min_samples_split': range(2, 10)}
    parameters2 = {"C": range(1, 20), "gamma": [0.05, 0.1, 0.15, 0.2, 0.25]}
    parameters3_1 = {'n_estimators': range(10, 200, 10)}
    parameters3_2 = {'max_depth': range(1, 10), 'min_samples_split': range(2, 10)}  # 搜索空间太大，分两次调整参数
    parameters4 = {'n_estimators': range(10, 200, 10), 'learning_rate': [i / 10.0 for i in range(5, 15)]}
    parameters5 = {'n_neighbors': range(2, 10), 'leaf_size': range(10, 80, 20)}
    parameters6_1 = {'n_estimators': range(10, 200, 10)}
    parameters6_2 = {'max_depth': range(1, 10), 'min_child_weight': range(1, 10)}
    parameters6_3 = {'subsample': [i / 10.0 for i in range(1, 10)],
                     'colsample_bytree': [i / 10.0 for i in range(1, 10)]}  # 搜索空间太大，分三次调整参数

    # 获取数据
    train, test = get_date()
    features, labels = split_train(train)
    # print(features)
    # print(labels)
    # 对所有特征进行热独立编码
    features = pd.get_dummies(features)

    # 测试数据
    test = test.values[:, 1:]
    test = pd.DataFrame(test)
    test = pd.get_dummies(test)
    encoded = list(test.columns)

    clf = RandomForestClassifier(n_estimators=15)
    clf.fit(features,labels)
    prv = clf.predict(test)
    # print(prv)

    result = np.zeros((300,1))
    id = [i for i in range(300)]

    result[:,0]=prv
    # print(result)

    result=pd.DataFrame(result,columns=['y'])
    result.to_csv('1.csv')

