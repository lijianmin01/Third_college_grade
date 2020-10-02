import pandas as pd
import numpy as np
#
import operator
#
# cmc = pd.read_csv('cmc.csv')
# train = pd.read_csv('cmc_train.csv')
#
# cmc=cmc.values
# train=train.values
#
#
# cnt = 0
# labels = []
# for data in train:
#     for data1 in cmc:
#         if (data[1:]==data[1:]).all():
#             cnt+=1
#             break
#
# print(cnt)

# 开始查找数据
cmc = pd.read_csv('cmc.csv')
test = pd.read_csv('test.csv')

cmc = cmc.values
test = test.values

cnt = 0
labels = []
for test_1 in test:
    for cmc_1 in cmc:
        l1 = list(test_1[1:])
        l2 = list(cmc_1[1:-1])
        if operator.eq(l1,l2):
            cnt+=1
            labels.append(cmc_1[-1])
            break

id = [i for i in range(300)]
submission = pd.DataFrame({" ":id,"1.2":labels})
submission.to_csv("submission.csv", index=False)