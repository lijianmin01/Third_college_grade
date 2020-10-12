import pandas as pd
import Cart


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
    max_depth = 8
    min_size = 10

    tree = Cart.build_tree(dataSets, max_depth, min_size)
    predictions = []
    for row in test_cnt:
        prediction = Cart.predict(tree, row)
        predictions.append(prediction)

    # 将预测结果保存为csv文件
    result = pd.DataFrame(predictions, columns=['y'])
    result.to_csv('prv_result.csv')
