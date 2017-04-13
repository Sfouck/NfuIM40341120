# coding=UTF-8

## 範例1
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier ##將鄰近的點相連，去模擬出預測值
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

iris = datasets.load_iris() ## 從資料庫裡載入iris的資料
iris_X = iris.data ## iris的屬性，例如花瓣的長寬、花萼的長寬
iris_y = iris.target ## iris的分類


print(iris_X[:2]) ## 顯示前2筆
print(iris_y)
print(np.unique(iris.target)) ## 重複的值不顯示

X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3)
## 將iris_X和iris_y這2個數據集分成訓練集和測試集，其中測試集佔數據集的30%

print(X_train[:2]) ## 顯示屬性的訓練集(前2筆)
print(X_test[:2]) ## 顯示屬性的測試集(前2筆)
print(y_train) ## 顯示分類的訓練集
print(y_test) ## 顯示分類的測試集

knn = KNeighborsClassifier()
print(knn.get_params()) ## 取出之前定義的參數
knn.fit(X_train, y_train) ## 訓練模型

print(knn.predict(X_test)) ## 預測測試集的數據
print(y_test) ## 真實值

## 2D圖
x_min, x_max = iris_X[:, 0].min() - .5, iris_X[:, 0].max() + .5
y_min, y_max = iris_X[:, 1].min() - .5, iris_X[:, 1].max() + .5
plt.figure(2, figsize=(10, 8))

# plt.clf()
# Plot the training points

plt.scatter(iris_X[:, 0], iris_X[:, 1], c=iris_y, cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.show()

## 3D圖
fig = plt.figure()
ax = Axes3D(fig, elev=-150, azim=110)
ax.scatter(iris_X[:, 0], iris_X[:, 1], iris_X[:, 2], c=iris_y,
cmap=plt.cm.Paired)
ax.set_title("First three PCA directions")
ax.set_xlabel("1st eigenvector")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.w_zaxis.set_ticklabels([])

plt.show()

## 範例2
from sklearn import preprocessing ## 標準化數據模型
import numpy as np
from sklearn.model_selection import train_test_split ## train與將資料分割與test的模型
from sklearn.datasets.samples_generator import make_classification ## 生成適合做classification資料的模型
from sklearn.svm import SVC # Support Vector Machine中的Support Vector Classifier
import matplotlib.pyplot as plt

## 數據標準化的範例
# 建立Array，第一個屬性範圍為-100 ~120；第二個屬性範圍為2.7 ~ 20；第三個屬性範圍為-2 ~ 40
a = np.array([[10, 2.7, 3.6],
[-100, 5, -2],
[120, 20, 40]], dtype=np.float64)

print(a)
#將normalized後的a印出
print(preprocessing.scale(a))

## 數據標準化對機器學習成效的影響
# 建立具有2種屬性(n_features=2)的300筆數據(n_samples=300)，其中有2個相關的屬性(n_informative=2)，
# random_state是隨機數的種子，n_clusters_per_class每個分類的集群數
X, y = make_classification(n_samples=300, n_features=2,
                           n_redundant=0, n_informative=2,
                           random_state=22, n_clusters_per_class=1,
                           scale=100)

print(X[:5])
print(y)

plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()

# 數據標準化前
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
## 將X和y這2個數據集分成訓練集和測試集，其中測試集佔數據集的30%

clf = SVC() ## 使用SVC()這個模型
clf.fit(X_train, y_train) ## 訓練模型

print(clf.score(X_test, y_test)) ## 顯示測試及的精確度



# 數據標準化後
X = preprocessing.scale(X)

plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()

## 將X和y這2個數據集分成訓練集和測試集，其中測試集佔數據集的30%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

clf = SVC() ## 使用SVC()這個模型
clf.fit(X_train, y_train) ## 訓練模型

print(clf.score(X_test, y_test)) ## 顯示測試及的精確度