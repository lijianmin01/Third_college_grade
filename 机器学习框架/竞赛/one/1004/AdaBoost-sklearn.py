import numpy as np
import pandas as pd


# 获取数据
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

train=pd.read_csv("cmc_train.csv")
test=pd.read_csv("test.csv")

train['2+3']=train['2']+train['3']
test['2+3']=test['2']+test['3']

train['2+3+1']=train['2+3'].map(lambda x:'0' if x<=2 else '1' if x<=4 else '2' if x<=5 else '3' if x<=7 else '4')
test['2+3+1']=test['2+3'].map(lambda x:'0' if x<=2 else '1' if x<=4 else '2' if x<=5 else '3' if x<=7 else '4')


train['kids'] = train['3.1'].map(lambda x:'1' if x<= 3 else '2' if x<7 else '3')
test['kids'] = test['3.1'].map(lambda x:'1' if x<= 3 else '2' if x<7 else '3')


# train['husband_work']=train['2.1'].map(lambda x:'0' if x<=1 else '1' if x<=3 else '2')
# test['husband_work']=test['2.1'].map(lambda x:'0' if x<=1 else '1' if x<=3 else '2')

# train['life_is_good'] = train['3.2'].map(lambda x:'0' if x<1 else '1' if x<=2 else '2')
# test['life_is_good'] = test['3.2'].map(lambda x:'0' if x<1 else '1' if x<=2 else '2')

labels = train['1.2']
features= train.drop(['Unnamed: 0','2','3','2+3','1.2'],axis=1)

test= test.drop(['Unnamed: 0','2','3','2+3'],axis=1)

features = pd.get_dummies(features)
test = pd.get_dummies(test)

pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('pca', PCA()),
        ('randomforestclassifier', RandomForestClassifier())
])

pipeline.fit(features,labels)

prv = pipeline.predict(test)

result = np.zeros((300, 1))


id = [i for i in range(300)]

result[:, 0] = prv
# print(result)

result = pd.DataFrame(result, columns=['y'])
result.to_csv('随机森林2.csv')




