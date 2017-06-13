# coding=UTF-8
import warnings
# 使用 pandas 儲存資料
import pandas as pd
# import在 sklearn 中，會在這用到的 Classifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import LinearSVC, SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

if __name__ == '__main__':
    def warn(*args, **kwargs):
        pass


    # 讀取資料
    def load_data(path):
        data = []
        with open(path, "r") as data_file:
            for line in data_file:
                # 有未知值則捨棄該行資料
                if line.find("?") == -1:
                    data.append(line.strip().split(","))
                else:
                    pass
        return data


    warnings.warn = warn
    # 訓練集和測試集欄位名的list
    adult_columns = "age,workclass,fnlwgt,education,education-num,marital-status,occupation,relationship,race,sex," \
                    "capital-gain,capital-loss,hours-per-week,native-country,over50k".split(",")

    # 讀取訓練集和測試集，塞到DataFrame結構裡面
    train_data = pd.DataFrame(load_data("adult.data"), columns=adult_columns)
    test_data = pd.DataFrame(load_data("adult.test"), columns=adult_columns)

    # 處理讀進來的資料

    # over50k欄位裡，">50K"為1 "<=50K"為0
    train_data["over50k"] = [1 if x == " >50K" else 0 for x in train_data["over50k"]]
    test_data["over50k"] = [1 if x == " >50K" else 0 for x in test_data["over50k"]]

    # 數值為連續變數之欄位，空為0;反之將 string 轉為 int
    continuous_col = "age,fnlwgt,education-num,capital-gain,capital-loss,hours-per-week".split(",")
    for col in continuous_col:
        train_data[col] = [int(x) if not ((x is "") or (x is None))else 0 for x in train_data[col]]
        test_data[col] = [int(x) if not ((x is "") or (x is None))else 0 for x in test_data[col]]
        print("{:s} is done.".format(col))

    # 輸出處理過後的訓練集和測試集的資料數
    print("Train_instances number = {0}\n"
          "Test_instances number = {1}\n".format(len(train_data), len(test_data)))

    # 建立儲存classifiers本身和它名字的List
    names = ["Nearest Neighbors(1)", "Nearest Neighbors(3)", "Neural Net(MLPClassifier)", "LinearSVC", "SVC"]
    classifiers = [
        KNeighborsClassifier(1),
        KNeighborsClassifier(3),
        MLPClassifier(alpha=1),
        LinearSVC(C=1.0),
        SVC(gamma=2, C=1)]

    # 選擇作為 X 的欄位,和作為 Y 的欄位
    select_col = "age,hours-per-week".split(",")
    target = "over50k"
    print("Features:\n"
          "{0}\n"
          "Target:\n"
          "{1}\n".format(select_col, target))

    # 將訓練集和測試集中，選定欄位丟入相應變數中
    scaler = lambda x: StandardScaler().fit_transform(x)
    X_train, X_test = scaler(train_data[select_col]), scaler(test_data[select_col])
    y_train, y_test = train_data[target], test_data[target]

    # 遍歷 classifiers，丟入訓練集後，在依照測試集取得score
    for name, clf in zip(names, classifiers):
        print("{}:".format(name))
        clf.fit(X_train, y_train)
        score = clf.score(X_test, y_test)
        # 輸出 Variance score，1.0 為完美預測
        print('Variance score = {:.2f}'.format(score))

        if hasattr(clf, "coef_"):
            print("coef_ = {}".format(clf.coef_))

        print
