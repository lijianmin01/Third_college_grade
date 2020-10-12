
# 建立一颗决策树
def build_tree(train, max_depth, min_size):
    root = get_split(train)  # 1-8
    split(root, max_depth, min_size, 1)
    return root

# 计算分割数据集的基尼系数
def gini_index(groups, classes):
    # 总的样本数--count all samples at split point
    n_instances = float(sum([len(group) for group in groups]))

    # 划分后的加权GINI指数--sum weighted Gini index for each group
    gini = 0.0
    for group in groups:
        size = float(len(group))

        # 避免分母出现0的情况
        if size == 0:
            continue
        score = 0.0
        # 根据每个课程的分数为小组评分
        for class_val in classes:
            p = [row[-1] for row in group].count(class_val) / size
            score += p * p

        # 根据相对得分对小组得分进行加权
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

# 为数据集选择最佳分割点
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

# 基于到达当前节点的训练集，生成该节点的预测值
def to_terminal(group):
    outcomes = [row[-1] for row in group]
    return max(set(outcomes), key=outcomes.count)

# 为节点创建子拆分或创建叶子结点
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

    # 左孩纸
    if len(left) <= min_size:
        node['left'] = to_terminal(left)
    else:
        node['left'] = get_split(left)
        split(node['left'], max_depth, min_size, depth + 1)

    # 右孩纸
    if len(right) <= min_size:
        node['right'] = to_terminal(right)
    else:
        node['right'] = get_split(right)
        split(node['right'], max_depth, min_size, depth + 1)

# 进行预测
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

# 分类回归树算法(核心函数)
def decision_tree(train, test, max_depth, min_size):
    tree = build_tree(train, max_depth, min_size)
    predictions = list()
    for row in test:
        prediction = predict(tree, row)
        predictions.append(prediction)
    return (predictions)

