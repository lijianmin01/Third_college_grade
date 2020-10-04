import pandas as pd
import numpy as np


# 引入相关的机器学习库
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

# 定义通用函数框架(通过训练数据，得到模型)
def fit_model(alg,parameters):
    x = features
    y = labels # 由于数据较少，使用全部数据进行网格搜索
    scorer=make_scorer(roc_auc_score)  #使用roc_auc_score作为评分标准
    grid = GridSearchCV(alg,parameters,scoring=scorer,cv=5)##使用网格搜索，出入参数
    start = time() # 计时
    grid = grid.fit(x,y) # 模型训练
    end = time()
    t = round(end-start,3)
    print (grid.best_params_)  #输出最佳参数
    print ('searching time for {} is {} s'.format(alg.__class__.__name__,t)) #输出搜索时间
    return grid #返回训练好的模型


#首先我们先定义一个保存函数，将预测的结果保存为可以提交的格式：
def save(clf,i):
    pred=clf.predict(test)
    Id = [i for i in range(300)]
    sub=pd.DataFrame({ 'id': Id, 'y': pred })
    sub.to_csv("res_tan_{}.csv".format(i), index=False)

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

#对所有特征实现独热编码
def data_hot(features):
    features = pd.get_dummies(features)
    return features



if __name__ == '__main__':
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

    # 定义初始化函数
    ## 列出需要使用的算法
    # 列出需要使用的算法
    alg1 = DecisionTreeClassifier(random_state=29)
    alg2 = SVC(probability=True, random_state=29)  # 由于使用roc_auc_score作为评分标准，需将SVC中的probability参数设置为True
    alg3 = RandomForestClassifier(random_state=29)
    alg4 = AdaBoostClassifier(random_state=29)
    alg5 = KNeighborsClassifier(n_jobs=-1)
    # alg6=XGBClassifier(random_state=29,n_jobs=-1)

    # 然后列出我们需要调整的参数及取值范围，这是一个很繁琐的工作，需要大量的尝试和优化。（以下参数范围并非最优，大家可以继续探索）
    # 列出需要调整的参数范围
    parameters1 = {'max_depth': range(1, 10), 'min_samples_split': range(2, 10)}
    parameters2 = {"C": range(1, 20), "gamma": [0.05, 0.1, 0.15, 0.2, 0.25]}
    parameters3_1 = {'n_estimators': range(10, 200, 10)}
    parameters3_2 = {'max_depth': range(1, 10), 'min_samples_split': range(2, 10)}  # 搜索空间太大，分两次调整参数
    parameters4 = {'n_estimators': range(10, 200, 10), 'learning_rate': [i / 10.0 for i in range(5, 15)]}
    parameters5 = {'n_neighbors': range(2, 10), 'leaf_size': range(10, 80, 20)}
    parameters6_1 = {'n_estimators': range(10, 200, 10)}
    parameters6_2 = {'max_depth': range(1, 10), 'min_child_weight': range(1, 10)}
    parameters6_3 = {'subsample': [i / 10.0 for i in range(1, 10)],'colsample_bytree': [i / 10.0 for i in range(1, 10)]}  # 搜索空间太大，分三次调整参数

    # 1、DecisonTreeClassifier
    clf1 = fit_model(alg1, parameters1)

    # 2、SVM
    clf2 = fit_model(alg2, parameters2)

    # 3.RandomForest
    clf3_m1 = fit_model(alg3, parameters3_1)

    # 3.1第二次调参
    alg3 = RandomForestClassifier(random_state=29, n_estimators=180)
    clf3 = fit_model(alg3, parameters3_2)

    clf4 = fit_model(alg4, parameters4)

    # 5、KNN
    clf5 = fit_model(alg5, parameters5)

    # 调用这个函数，完成6个模型的预测：
    i = 1
    for clf in [clf1, clf2, clf3, clf4, clf5]:
        save(clf, i)
        i = i + 1
