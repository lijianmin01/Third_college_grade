from random import seed
from random import randrange
import pandas as pd
import numpy as np




# 1-7 Calculate the Gini index for a split dataset
def gini_index(groups, classes):
    # 总的样本数--count all samples at split point
    n_instances = float(sum([len(group) for group in groups]))

    # 划分后的加权GINI指数--sum weighted Gini index for each group
    gini = 0.0
    for group in groups:
        size = float(len(group))

        # avoid divide by zero
        if size == 0:
            continue
        score = 0.0
        # score the group based on the score for each class
        for class_val in classes:
            p = [row[-1] for row in group].count(class_val) / size
            score += p * p

        # weight the group score by its relative size
        gini += (1.0 - score) * (size / n_instances)

    return gini

def t_split(index, value, dataset):
    left, right = list(), list()
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right

# 1-8 Select the best split point for a dataset
def get_split(dataset):

    class_values = list(set(row[-1] for row in dataset))

    # 初始化最小基尼指数对应的特征序号，切分点，基尼指数值，分组列表
    b_index, b_value, b_score, b_groups = 999, 999, 999, None

    # 针对每个备选的特征
    for index in range(len(dataset[0]) - 1):

        # 考查每个备选的切分阈值
        for row in dataset:
            groups = t_split(index, row[index], dataset)
            gini = gini_index(groups, class_values)
            if gini < b_score:
                b_index, b_value, b_score, b_groups = index, row[index], gini, groups

    # 在当前结点处，存放字典形式的信息：切分特征、切分点、划分的两个子集
    return {'index': b_index, 'value': b_value, 'groups': b_groups}


# 1-9 Create a terminal node value--基于到达当前节点的训练集，生成该节点的预测值
def to_terminal(group):
    outcomes = [row[-1] for row in group]
    return max(set(outcomes), key=outcomes.count)


# 1-10 Create child splits for a node or make terminal
# 生成当前结点的后续子节点、或直接作为叶子结点生成预测结果
# 输入参数：当前结点的字典形式的描述；最大深度；最小样本数；当前深度
def split(node, max_depth, min_size, depth):
    # (1)获取该结点的左右子集，为后续更新结点信息更新做准备
    left, right = node['groups']
    del (node['groups'])

    # (2)判断当前结点是否直接作为叶子结点--check for a no split
    # 如果是，不再分裂，直接返回
    if not left or not right:
        node['left'] = node['right'] = to_terminal(left + right)
        return

    # (2)check for max depth 若已为最大深度，后续两个子结点直接作为叶子结点
    if depth >= max_depth:
        node['left'], node['right'] = to_terminal(left), to_terminal(right)
        return

    # (3)process left child
    if len(left) <= min_size:
        node['left'] = to_terminal(left)
    else:
        node['left'] = get_split(left)
        split(node['left'], max_depth, min_size, depth + 1)

    # (4)process right child
    if len(right) <= min_size:
        node['right'] = to_terminal(right)
    else:
        node['right'] = get_split(right)
        split(node['right'], max_depth, min_size, depth + 1)


# 1-11 Build a decision tree
def build_tree(train, max_depth, min_size):
    root = get_split(train)  # 1-8
    split(root, max_depth, min_size, 1)
    return root


# 1-12 Make a prediction with a decision tree
def predict(node, row):
    if row[node['index']] < node['value']:
        if isinstance(node['left'], dict):
            return predict(node['left'], row)
        else:
            return node['left']  # 见1-10
    else:
        if isinstance(node['right'], dict):
            return predict(node['right'], row)
        else:
            return node['right']


# 1-13 Classification and Regression Tree Algorithm(核心函数)
def decision_tree(train, test, max_depth, min_size):
    tree = build_tree(train, max_depth, min_size)
    predictions = list()
    for row in test:
        prediction = predict(tree, row)
        predictions.append(prediction)
    return (predictions)


# 判断准确率
def yanzheng(prv,max_depth,min_size):
    ans = [1, 1, 1, 3, 3, 3, 3, 3, 3, 1, 1, 3, 1, 2, 3, 1, 2, 1, 1, 1, 1, 1, 3, 3, 1, 1, 3, 3, 2, 3, 1, 2, 1, 1, 1, 2, 3, 2, 3, 1, 3, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 1, 3, 3, 3, 1, 2, 2, 2, 1, 2, 3, 1, 1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 3, 3, 3, 2, 2, 3, 3, 1, 1, 1, 1, 1, 1, 2, 1, 3, 2, 2, 3, 1, 3, 1, 2, 1, 3, 2, 1, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 2, 1, 1, 3, 3, 1, 1, 1, 3, 3, 3, 1, 3, 1, 2, 2, 2, 1, 3, 1, 3, 1, 3, 2, 1, 3, 1, 3, 1, 3, 2, 2, 2, 1, 3, 2, 3, 1, 3, 3, 3, 3, 1, 2, 2, 1, 3, 1, 2, 3, 1, 3, 1, 1, 1, 3, 2, 1, 1, 1, 1, 3, 2, 1, 1, 2, 2, 2, 3, 1, 1, 1, 2, 1, 1, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 3, 3, 1, 1, 1, 3, 2, 3, 1, 2, 1, 3, 3, 3, 1, 3, 2, 1, 2, 2, 2, 3, 1, 3, 1, 1, 1, 2, 3, 2, 1, 2, 2, 3, 1, 1, 1, 1, 1, 1, 2, 2, 1, 3, 2, 1, 2, 3, 2, 3, 1, 2, 1, 1, 1, 1, 3, 1, 3, 2, 1, 1, 1, 3, 1, 1, 3, 3, 2, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 1, 1, 1, 2, 3, 3, 1, 1, 2, 1, 3, 2, 1, 1, 3]
    lens = len(prv)
    cnt = 0.0
    for i in range(lens):
        if(ans[i]==prv[i]):
            cnt+=1

    print("max_depth:{},min_size:{} is {}".format(max_depth,min_size,cnt/lens*1.0))

    result = pd.DataFrame(prv, columns=['y'])
    result.to_csv('cart_5_8.csv'.format(max_depth))

# 1-6 Split a dataset based on an attribute and an attribute value





if __name__ == '__main__':
    train = pd.read_csv('cmc_train.csv')
    train = train.drop(columns=['Unnamed: 0'])
    test = pd.read_csv('test.csv')
    test = test.drop(columns=['Unnamed: 0'])

    # train_y = train['1.2'].values.tolist()
    # train = train.drop(columns=['1.2'])

    dataSets = train.values
    test_cnt = test.values

    n_folds = 5
    max_depth = 5
    min_size = 8

    # 6 9

    # max_depth_list = [i for i in range(7,15)]
    # min_size_list = [i for i in range(4,20)]
    #
    # max_depth_list = [i for i in range(7, 15)]
    # min_size_list = [i for i in range(4, 20)]

    # for max_depth in max_depth_list:
    #     for min_size in min_size_list:

    tree = build_tree(dataSets, max_depth, min_size)
    predictions = []
    for row in test_cnt:
        prediction = predict(tree, row)
        predictions.append(prediction)

    yanzheng(predictions,max_depth,min_size)
