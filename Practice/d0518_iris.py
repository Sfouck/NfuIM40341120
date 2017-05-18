from sklearn import datasets,svm
import matplotlib.pyplot as plt
import numpy as np
iris = datasets.load_iris()
#print iris.data

clf = svm.SVC(gamma=0.001, C=100.)
iris = datasets.load_iris()
clf.fit(iris.data[:-10], iris.target[:-10])
result = clf.predict(iris.data[-10])
print "predict:"
print result
print "actual:"
print iris.data[:-10]

digits = datasets.load_digits()
testData = "0 1 7 8 13 16 8 1 0 1 7 7 9 11 6 0 0 0 0 0 8 13 6 0 0 4 6 6 10 15 6 0 0 2 7 15 10 4 0 0 0 0 0 16 5 0 0 0 0 0 9 10 9 0 0 0 0 0 13 5 0 0 0 0"
testData = np.array(testData.strip().split(" "), dtype=float)
testImage = np.array([testData[i*8:i*8+8] for i in range(8)])

print testImage

print "Test begin"
clf = svm.SVC(gamma=0.001, C=100.)
digits = datasets.load_digits()
clf.fit(digits.data[:-1], digits.target[:-1])
result = clf.predict(testData)
print "predict:"
print result
print "actual:"
print 7

plt.figure(1,figsize=(3,3))
plt.imshow(testImage, cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
print "Test end"
