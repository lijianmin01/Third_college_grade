from math import log

# 计算给定数据集的熵

def calc_shannon_ent(data_set):
    num_entries = len(data_set)  # 样本总个数
    label_counts = {}    # 标签的数量
    for feat_vec in data_set:
        current_label = feat_vec[-1]  # 该样本所属的类别
        if current_label not in label_counts.keys():
            label_counts[current_label]=0
        label_counts[current_label]+=1
        shannon_ent = 0.0 # 记录数据集的经验熵yan
        for key in label_counts:
            # 每个类别 |Ck/D|log2 |Ck/D|
            prob = float(label_counts[key])/num_entries
            shannon_ent -= prob*log(prob,2)
    return shannon_ent


# 按照给定的特征划分数据集

# axis 代表特征所在的行  value 代表特征的值
def split_dataSet(dataset,axis,value):
    ret_dataSet = []
    for feat_vec in dataset:
        if feat_vec[axis]==value:
            # 删去给定的特征
            reduced_feat_vec = feat_vec[:axis]
            reduced_feat_vec.extend(feat_vec[axis+1:])
            ret_dataSet.append(reduced_feat_vec)
    return ret_dataSet

# 选择出信息增益最大的特征，来进行数据集的划分

def choose_best_feature_to_split(dataSet):
    # 一个样本特征的数量
    numFeatures = len(dataset[0])-1
    # 计算出数据的经验熵
    base_entropy = calc_shannon_ent(dataset)
    # 初始化两个变量用来记录 信息增益最大值 和  表现最好的特征
    best_info_gain = 0.0
    best_feature = -1
    
    for i in range(numFeatures):
        # 记录该特征的所有值
        feat_list = [example[i] for example in dataSet]
        # 将该特征值划分类别
        unique_vals = set(feat_list)
        # 
        new_entropy = 0.0
        # 依次求出信息增益
        for value in unique_vals:
            sub_data_set = split_dataSet(dataset,i,value)
            prob = len(sub_data_set)/float(len(dataSet))
            new_entropy += prob*calc_shannon_ent(sub_data_set)
        info_gain = base_entropy-new_entropy
        if (info_gain>best_info_gain):
            best_info_gain = info_gain
            best_feature = i
    return best_feature




    