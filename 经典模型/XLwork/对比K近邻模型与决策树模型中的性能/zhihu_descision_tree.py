import operator
import numpy as np
import pandas as pd
import time
import math


def create_dataset():
    dataset = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    features = ['no surfacing', 'flippers']
    return dataset, features

# 计算香农熵
def cal_shannon_entropy(dataset:list):
    example_num = len(dataset)
    entropy = 0.0
    label_cnt = {}
    label_list = [example[-1] for example in dataset]
    for label in label_list:
        label_cnt[label] = label_cnt.get(label, 0) + 1
    for key in label_cnt.keys():
        prob = label_cnt[key]/example_num
        entropy -= prob * math.log(prob, 2)
    return entropy

# 根据某一特征的值划分数据集的函数
def split_dataset(dataset:list, axis:int, value):
    sub_dataset = []
    for ind, example in enumerate(dataset):
        if example[axis] == value:
            # delete the feature which has been used
            reduced_vec = example[:axis] + example[axis+1:]
            sub_dataset.append(reduced_vec)
    return sub_dataset

# 当前划分数据集最好的特征
def best_feat_to_split(dataset:list):
    base_entropy = cal_shannon_entropy(dataset)
    max_info_gain = -1
    best_feat_ind = -1
    feat_len = len(dataset[0]) - 1
    for feat in range(feat_len):
        # get all kinds of value of this feature
        feat_list = [example[feat] for example in dataset]
        feat_class = set(feat_list)
        # split the dataset by all the values , and calculate entropy
        entropy = 0.0
        for feat_value in feat_class:
            sub_dataset = split_dataset(dataset, feat, feat_value)
            entropy += cal_shannon_entropy(sub_dataset)
        # calculate decrement of entropy
        info_gain = base_entropy - entropy
        if info_gain >= max_info_gain:
            best_feat_ind = feat
            max_info_gain = info_gain
    return best_feat_ind

# 取该子集中样本数量最多的类别
def major_class(class_list:list):
    class_cnt = {}
    for class_name in class_list:
        class_cnt[class_name] = class_cnt.get(class_name, 0) + 1
    sorted_class = sorted(class_cnt.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class[0][0]

# 构建决策树
def create_tree(dataset:list, labels:list):
    # ending conditions
    class_list = [example[-1] for example in dataset]
    if len(dataset[0]) == 1:
        return major_class(class_list)
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]

    feat_ind = best_feat_to_split(dataset)
    best_feat = labels[feat_ind]
    tree = {best_feat:{}}
    labels = labels[:feat_ind] + labels[feat_ind+1:]
    feat_values = set([example[feat_ind] for example in dataset])
    for feat_value in feat_values:
        sub_labels = labels[:]
        sub_dataset = split_dataset(dataset, feat_ind, feat_value)
        tree[best_feat][feat_value] = create_tree(sub_dataset, sub_labels)
    return tree

# 使用决策树预测
def classify(input_tree:dict, feat_labels:list, test_vec:list):
    # get the first feature and its index in feat_labels
    first_feat = list(input_tree.keys())[0]
    feat_ind = feat_labels.index(first_feat)
    # get the corresponding branch
    second_dict = input_tree[first_feat][test_vec[feat_ind]]
    if type(second_dict) == dict:
        ret = classify(second_dict, feat_labels, test_vec)
        return ret
    else:
        return second_dict



def main():
    dataset, labels = create_dataset()

    print(dataset)
    print(labels)
    decision_tree = create_tree(dataset, labels)
    print(decision_tree)
    print(classify(decision_tree, labels, [1, 0]))

    pass

if __name__ == '__main__':
    main()