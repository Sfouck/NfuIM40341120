# coding=UTF-8
import warnings
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.svm import LinearSVC, SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


if __name__ == '__main__':
    def warn(*args, **kwargs):
        pass


    def load_data(path):
        data = []
        with open(path, "r") as data_file:
            for line in data_file:
                if line.find("?") == -1:
                    data.append(line.strip().split(","))
                else:
                    pass
        return data


    warnings.warn = warn
    adult_columns = "age,workclass,fnlwgt,education,education-num,marital-status,occupation,relationship,race,sex," \
                    "capital-gain,capital-loss,hours-per-week,native-country,over50k".split(",")

    train_data = pd.DataFrame(load_data("adult.data"), columns=adult_columns)
    test_data = pd.DataFrame(load_data("adult.test"), columns=adult_columns)

    continuous_col = "age,fnlwgt,education-num,capital-gain,capital-loss,hours-per-week".split(",")
    train_data["over50k"] = [1 if x == " >50K" else 0 for x in train_data["over50k"]]
    test_data["over50k"] = [1 if x == " >50K" else 0 for x in test_data["over50k"]]
    for col in continuous_col:
        train_data[col] = [int(x) if not ((x is "") or (x is None))else 0 for x in train_data[col]]
        test_data[col] = [int(x) if not ((x is "") or (x is None))else 0 for x in test_data[col]]
        print("{:s} is done.".format(col))

    print("Train_instances number = {0}\n"
          "Test_instances number = {1}\n".format(len(train_data), len(test_data)))

    names = ["Nearest Neighbors(1)", "Nearest Neighbors(3)", "Neural Net(MLPClassifier)", "LinearSVC", "SVC"]
    classifiers = [
        KNeighborsClassifier(1),
        KNeighborsClassifier(3),
        MLPClassifier(alpha=1),
        LinearSVC(C=1.0),
        SVC(gamma=2, C=1)]


    select_row = "fnlwgt,hours-per-week".split(",")
    target = "over50k"
    print("Features:\n"
          "{0}\n"
          "Target:\n"
          "{1}\n".format(select_row, target))

    scaler = lambda x: StandardScaler().fit_transform(x)
    X_train, X_test = scaler(train_data[select_row]), scaler(test_data[select_row])
    y_train, y_test = train_data[target], test_data[target]

    for name, clf in zip(names, classifiers):
        print("{}:".format(name))
        clf.fit(X_train, y_train)
        score = clf.score(X_test, y_test)
        print('Variance score = {:.2f}'.format(score))

        if hasattr(clf, "coef_"):
            print("coef_ = {}".format(clf.coef_))

        print
