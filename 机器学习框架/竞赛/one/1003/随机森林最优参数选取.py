import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import numpy as np


# 分离训练数据  特征+类别
def split_train(train):
    labels = train['1.2']
    del train['1.2']
    features = train.values[:,1:]
    features = pd.DataFrame(features)
    return features,labels

if __name__ == '__main__':
    train = pd.read_csv('cmc_train.csv')
    y = train['1.2']

    del train['1.2']
    X = train

    y = [int(i) for i in y]

    # 对所有特征进行热独立编码
    X = pd.get_dummies(X)

    test_data = pd.read_csv('test.csv')
    test_data = pd.get_dummies(test_data)


    from sklearn.model_selection import RandomizedSearchCV

    # Number of trees in random forest
    n_estimators = [int(x) for x in np.linspace(start=10, stop=400, num=5)]
    # Number of features to consider at every split
    max_features = ['auto', 'sqrt']
    # Maximum number of levels in tree
    max_depth = [int(x) for x in np.linspace(4, 30, num=1)]
    max_depth.append(None)
    # Minimum number of samples required to split a node
    min_samples_split = [2,3,5,6,7,8,10]
    # Minimum number of samples required at each leaf node
    min_samples_leaf = [1,2,3,4,5,6,7,8,9]
    # Method of selecting samples for training each tree
    bootstrap = [True, False]

    # Create the random grid
    random_grid = {'n_estimators': n_estimators,
                   'max_features': max_features,
                   'max_depth': max_depth,
                   'min_samples_split': min_samples_split,
                   'min_samples_leaf': min_samples_leaf,
                   'bootstrap': bootstrap}

    # Use the random grid to search for best hyperparameters
    # First create the base model to tune
    rf = RandomForestRegressor()
    # Random search of parameters, using 3 fold cross validation,
    # search across 100 different combinations, and use all available cores
    rf_random = RandomizedSearchCV(estimator=rf, param_distributions=random_grid,
                                   n_iter=100, scoring='neg_mean_absolute_error',
                                   cv=7, verbose=2, random_state=42, n_jobs=-1)

    # Fit the random search model
    rf_random.fit(X, y)


    print(rf_random.best_params_)



