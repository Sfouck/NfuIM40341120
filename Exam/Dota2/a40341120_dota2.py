# coding=UTF-8
# import 需要的套件
import warnings
import pandas as pd
import time
from sklearn.neural_network import MLPClassifier
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier

if __name__ == '__main__':
    def warn(*args, **kwargs):
        pass


    # 把警告訊息忽略掉
    warnings.warn = warn

    # 讀取訓練集和測試集
    train_data = pd.read_csv("dota2Train.csv")
    test_data = pd.read_csv("dota2Test.csv")

    # 取得欄位名稱和設定target欄位
    TARGET_ATTRIBUTE = "TeamWon"
    DATA_ATTRIBUTE = train_data.columns.values.tolist()
    select_col = DATA_ATTRIBUTE[1:]

    # print DATA_ATTRIBUTE
    # print select_col

    # 建立演算法物件和名字的List
    names = ["Nearest Neighbors(3)", "Neural Net(MLPClassifier)", "LinearSVC"]
    classifiers = [
        KNeighborsClassifier(3, n_jobs=-1),
        MLPClassifier(alpha=1),
        LinearSVC(C=1.)]

    # 將訓練集和測試集丟入X和y
    X_train, X_test = train_data[select_col], test_data[select_col]
    y_train, y_test = train_data[TARGET_ATTRIBUTE], test_data[TARGET_ATTRIBUTE]

    # 依序遍歷 classifiers，fit 訓練集後，在給測試集取得score
    for name, clf in zip(names, classifiers):
        print("{}:".format(name))
        start_time = time.time()
        clf.fit(X_train, y_train)
        score = clf.score(X_test, y_test)
        # 輸出 Variance score，1.0 為完美預測
        print('Variance score = {:.2f}'.format(score))

        won = lambda x: " 1" if x == 1 else "-1"
        result_list = {"predict": [won(y) for y in clf.predict(X_test.head(5))],
                       "actual": [won(y) for y in y_test.head(5)]}
        print("Predict:\n{}\nActual:\n{}".format(result_list["predict"], result_list["actual"]))

        print("cost time = {} sec".format(time.time() - start_time))
        print
