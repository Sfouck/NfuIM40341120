import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import linear_model
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import warnings

if __name__ == '__main__':
    def warn(*args, **kwargs):
        pass


    warnings.warn = warn


    def load_data(path):
        data = []
        with open("adult.data", "r") as data_file:
            for line in data_file:
                if line.find("?") == -1:
                    data.append(line.strip().split(","))
                else:
                    pass
        return data


    train_data = load_data("adult.data")
    adult_columns = "age,workclass,fnlwgt,education,education-num,marital-status,occupation,relationship,race,sex," \
                    "capital-gain,capital-loss,hours-per-week,native-country,over50k".split(",")
    train_data = pd.DataFrame(train_data, columns=adult_columns)

    print train_data
    train_data["over50k"] = [1 if x == " >50K" else 0 for x in train_data["over50k"]]
    continuous_col = "age,fnlwgt,education-num,capital-gain,capital-loss,hours-per-week".split(",")
    for col in continuous_col:
        print(col)
        # print(train_data[col])
        train_data[col] = [int(x) if not (x == "" or x == None)else 0 for x in train_data[col]]
        print("{:s} is done".format(col))

    print len(train_data)
    print train_data.head(15)
    select_row = "age,fnlwgt".split(",")
    print select_row
    # print train_data[select_row]

    h = .02  # step size in the mesh
    train_percent = 50

    names = ["Nearest Neighbors", "Naive Bayes", "Neural Net"]

    classifiers = [
        KNeighborsClassifier(3),
        GaussianNB(),
        MLPClassifier(alpha=1)]

    figure = plt.figure(figsize=(3, 3))

    # iterate over datasets
    # preprocess dataset, split into training and test part
    X, y = train_data[select_row], train_data["over50k"]
    X = StandardScaler().fit_transform(X)
    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, test_size=1 - train_percent / 100.0, random_state=42)

    # x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    # y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    # xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
    #                      np.arange(y_min, y_max, h))
    #
    # # just plot the dataset first
    # cm = plt.cm.RdBu
    # cm_bright = ListedColormap(['#FF0000', '#0000FF'])
    # ax = plt.subplot(1, len(classifiers), 1)
    # ax.set_title("Input data")
    # # Plot the training points
    # ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright)
    # # and testing points
    # ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright, alpha=0.6)
    # ax.set_xlim(xx.min(), xx.max())
    # ax.set_ylim(yy.min(), yy.max())
    # ax.set_xticks(())
    # ax.set_yticks(())

    # iterate over classifiers
    for name, clf in zip(names, classifiers):
        print("{}:".format(name))

        ax = plt.subplot(1, len(classifiers), 1)
        clf.fit(X_train, y_train)
        score = clf.score(X_test, y_test)

        print('Variance score: {:.2f}'.format(clf.score(X_test, y_test)))
        print

        # # Plot the decision boundary. For that, we will assign a color to each
        # # point in the mesh [x_min, x_max]x[y_min, y_max].
        # if hasattr(clf, "decision_function"):
        #     Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
        # else:
        #     Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
        #
        # # Put the result into a color plot
        # Z = Z.reshape(xx.shape)
        # ax.contourf(xx, yy, Z, cmap=cm, alpha=.8)
        #
        # # Plot also the training points
        # ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright)
        # # and testing points
        # ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright,
        #            alpha=0.6)
        #
        # ax.set_xlim(xx.min(), xx.max())
        # ax.set_ylim(yy.min(), yy.max())
        # ax.set_xticks(())
        # ax.set_yticks(())
        # ax.set_title(name)
        # ax.text(xx.max() - .3, yy.min() + .3, ('%.2f' % score).lstrip('0'),
        #         size=15, horizontalalignment='right')

        # plt.tight_layout()
        # plt.show()
