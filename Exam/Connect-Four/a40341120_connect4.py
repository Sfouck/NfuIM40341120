# coding=UTF-8
import warnings
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split


def warn(*args, **kwargs):
    pass


warnings.warn = warn


def cast_data(l):
    temp = []
    for v in l[:-1]:
        temp.append({"b": 0,
                     "o": 1,
                     "x": 2,
                     }[v])
    temp.append({"win": 1,
                 "draw": 0,
                 "loss": -1,
                 }[l[-1]])
    return temp


f = open("connect-4.data", "r")
load_data = []
for line in f.read().split("\n")[:-1]:
    load_data.append(cast_data(line.split(",")))

TARGET_ATTRIBUTE = "outcome"
DATA_ATTRIBUTES = [
    "a1", "a2", "a3", "a4", "a5", "a6", "b1", "b2", "b3", "b4", "b5", "b6",
    "c1", "c2", "c3", "c4", "c5", "c6", "d1", "d2", "d3", "d4", "d5", "d6",
    "e1", "e2", "e3", "e4", "e5", "e6", "f1", "f2", "f3", "f4", "f5", "f6",
    "g1", "g2", "g3", "g4", "g5", "g6", TARGET_ATTRIBUTE
]

load_data = pd.DataFrame(load_data, columns=DATA_ATTRIBUTES)

print len(load_data)
print load_data.head(5)
print

X, y = load_data[DATA_ATTRIBUTES[:-1]], load_data[DATA_ATTRIBUTES[-1]]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=.32, random_state=1)

clf = MLPClassifier()
clf.fit(X_train, y_train)
print("Score:\n{}".format(clf.score(X_test, y_test)))

