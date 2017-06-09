from sklearn import datasets,svm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

load_date = np.array(pd.read_table("ColorHistogram.asc.gz"))

print len(load_date[0][0].split()[1:])
test = load_date[0][0].split()[1:]
print test

test = [[load_date[0][0].split()[1:][i*j+j] for j in range(1,8)] for i in range(4)]
for g in test:
    print g