from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
import pandas as pd
import numpy as np

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
    y = train['1.2']
    del train['1.2']
    X = train

    y = [int(i) for i in y]


    # # 对所有特征进行热独立编码
    X = pd.get_dummies(X)


    # svc = SVC()
    # parameters = [{'C': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],'gamma': [0.00001, 0.0001, 0.001, 0.1, 1, 10, 100, 1000],
    #                'kernel': ['rbf']},{'C': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],'kernel': ['linear']}]
    #
    # clf = GridSearchCV(svc, parameters, cv=5, n_jobs=8)
    # clf.fit(X, y)
    # print(clf.best_params_)
    # best_model = clf.best_estimator_

    from sklearn.model_selection import GridSearchCV

    grid = GridSearchCV(SVC(), param_grid={"C": [0.1,0.3,0.7,1,3,5,7,10], "gamma": [100,10,1, 0.1, 0.01],'kernel': ['linear','poly','rbf', 'sigmoid', 'precomputed']}, cv=4)
    grid.fit(X, y)
    print("The best parameters are %s with a score of %0.2f" % (grid.best_params_, grid.best_score_))
