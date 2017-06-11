# code = utf-8
from sklearn.naive_bayes import MultinomialNB
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_parem = []
data_result = []

f = open("connect-4.data","rb")

temp=[]
for line in f.read().split("\n"):
    temp = line.split(",")
    data_parem.append(temp[:-1])
    data_result.append(temp[-1])

#data_parem = np.array(data_parem)
#data_result = np.array(data_result)

print len(data_parem)
print data_parem[0],data_result[0]

clf = MultinomialNB()

clf.fit(data_parem[:10000], data_result[:10000])
result = clf.predict(data_parem[-10])
print "predict:"
print result
print "actual:"
print data_result[:-10]

print

