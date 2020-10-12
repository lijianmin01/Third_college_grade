import pandas as pd
import Cart
import numpy as np

def yanzheng(t_true,prv,max_depth,min_size):
    ans = t_true
    lens = len(prv)
    cnt = 0.0
    for i in range(lens):
        if(ans[i]==prv[i]):
            cnt+=1

    print("max_depth:{},min_size:{} is {}".format(max_depth,min_size,cnt/lens*1.0))


# 分层划分数据
def split_data(xx,yy):
    k = 10
    class_list = []
    for i in range(k):
        class_list.append([])

    cnt_array = np.array([i for i in range(len(yy))])
    # 算了，不想复杂了，直接当成两类别来随机划分吧
    class_0 = cnt_array[np.where(yy[cnt_array] == 0)]
    class_1 = cnt_array[np.where(yy[cnt_array] == 1)]
    class_2 = cnt_array[np.where(yy[cnt_array] == 2)]

    # 各个类别的数量
    class_0_nums = len(class_0)
    class_1_nums = len(class_1)
    class_2_nums = len(class_2)

    cnt = 0
    # 不放回随机抽样
    for i in range(class_0_nums):
        z = np.random.choice(class_0,1)
        index = np.where(class_0 == z)
        class_list[cnt].append(int(z))
        class_0 = np.delete(class_0,index)
        cnt = (cnt+1)%k

    cnt = 0
    for i in range(class_1_nums):
        z = np.random.choice(class_1, 1)
        index = np.where(class_1 == z)
        class_list[cnt].append(int(z))
        class_1 = np.delete(class_1, index)
        cnt = (cnt + 1) % k

    cnt = 0
    for i in range(class_2_nums):
        z = np.random.choice(class_2, 1)
        index = np.where(class_2 == z)
        class_list[cnt].append(int(z))
        class_1 = np.delete(class_2, index)
        cnt = (cnt + 1) % k

    test_cnt = xx[class_list[1]][:,:-1]
    test_true = xx[class_list[1]][:,-1]


    train = []
    for i in range(0,k):
        if i != 1:
            train.extend(xx[class_list[i]])


    train = [list(i) for i in train]

    return train,test_cnt,test_true

if __name__ == '__main__':
    # 从训练集中选出100份作为测试集，找出最佳 max_depth,min_size
    train = pd.read_csv('cmc_train.csv')
    train = train.drop(columns=['Unnamed: 0'])

    labels = train.values[:,-1]
    datasets = train.values

    dataSets,test_cnt,test_true = split_data(datasets,labels)

    # print(dataSets)
    # print(test_cnt)
    # print(test_true)


    n_folds = 5
    # max_depth = 8
    # min_size = 10

    max_depth_list = [5]
    min_size_list = [i for i in range(2,16,2)]

    for max_depth in max_depth_list:
        for min_size in min_size_list:
            tree = Cart.build_tree(dataSets, max_depth, min_size)
            predictions = []
            for row in test_cnt:
                prediction = Cart.predict(tree, row)
                predictions.append(prediction)

            yanzheng(test_true,predictions, max_depth, min_size)

    pass