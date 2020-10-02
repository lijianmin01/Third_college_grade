import pandas as pd
import numpy as np
r1 = pd.read_csv("随机森林2_1.csv").values

r2 = pd.read_csv("res_tan_2.csv").values

r3 = pd.read_csv("res_tan_4.csv").values

r4 = pd.read_csv("res_tan_1.csv").values

r5 = pd.read_csv("XGBClassifier1_1.csv").values
def count(zero,one,cnt):
    if cnt==1 :
        one+=1
    else :
        zero+=1

    return zero,one

result=[]
for i in range(len(r1)):
    zeros = 0
    ones = 0
    zeros, ones = count(zeros, ones, r1[i][1])
    zeros, ones = count(zeros, ones, r2[i][1])
    zeros, ones = count(zeros, ones, r3[i][1])
    zeros, ones = count(zeros, ones, r4[i][1])
    zeros, ones = count(zeros, ones, r5[i][1])
    if (ones>zeros):
        result.append(1)
    else:
        result.append(0)

result = pd.DataFrame({'PassengerId':pd.read_csv("res_tan_1.csv")['PassengerId'].values, 'Survived':np.array(result)})
result.to_csv("reslut_2_11.csv", index=False)