# coding=utf-8
from __future__ import division
from matplotlib import pyplot as plt
from matplotlib import dates
import datetime,random,time
import numpy as np

print "---第二題---"
# lambda
pi = 3.14
r = 5
getRoundArea = lambda x: x*pi**2
print("pi * r ^ 2 = {} * {} ^ 2 = {}".format(pi, r, getRoundArea(r)))

print "---第三題---"
# random不重複
q2 = []
for i in range(3):
    q2.append(np.arange(10, 20))
    np.random.shuffle(q2[i])

for i,v in enumerate(q2):
    print("[{}] = {}".format(i,v))


print "---第四題---"
# matplotlib畫圖

def string_to_date(date):
    tmp = []
    for i, d in enumerate(date):
        ts = d.split("-")
        tmp.append(datetime.date(int(ts[0]),int(ts[1]),int(ts[2])))
    return tmp
date = ['2015-1-10', '2015-1-11', '2015-1-12', '2015-1-13', '2015-1-14','2015-1-15',
        '2015-1-16', '2015-1-17', '2015-1-18', '2015-1-19', '2015-1-20']
temp = np.array([16.7,17.4,17.1,20.3,16.2,16.1,17.5,15.3,16.8,16,18.4])
plt.plot_date(string_to_date(date),temp,'r-',marker = '.')
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Taipei January Temperature\n40341120")
plt.show()
print("date = {}\ntemp = {}".format(string_to_date(date),temp))

print "---第五題---"
# 亂數矩陣相加
#random.seed(40341120)

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols
def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j) for j in range(num_cols)]for i in range(num_rows)]

def random_number(i, j):
    return random.randint(0,20)

def matrix_cal(A, B,L):
    if shape(A) != shape(B):
        raise ArithmeticError("cannot add matrices with different shapes")
    num_rows, num_cols = shape(A)
    def entry_fn(i, j):
        return L(A[i][j] , B[i][j])
    return make_matrix(num_rows, num_cols, entry_fn)
mAdd = lambda x, y: x+y
mMinus = lambda x, y : x-y
matrixA = make_matrix(2, 3, random_number)
matrixB = make_matrix(2, 3, random_number)
matrixC = make_matrix(2, 3, random_number)
print("matrixA = {}".format(matrixA))
print("matrixB = {}".format(matrixB))
print("matrixC = {}".format(matrixC))
print("matrixA - matrixB = {}".format(matrix_cal(matrixA,matrixB,mMinus)))
print("matrixA + matrixB + matrixC = {}".format(matrix_cal(matrix_cal(matrixA,matrixB,mAdd),matrixC,mAdd)))

print "---第六題---"
# 填空題
a1=0
a2=0
aboth=0
n=100000
def random_ball():
    return random.choice(["B", "Y"])
random.seed(2)
for _ in range(n):
    get1 = random_ball()
    get2 = random_ball()
    if get1 == "B":
        a1 += 1
    if get1 == "B" and get2 == "B":
        aboth += 1
    if get2 == "B":
        a2 += 1

print "P(aboth):", aboth / n
print "P(get1): ", a1 / n
print "P(get2): ", a2 / n
print "P(get1,get2): ", a1 / n * a2 / n
print "P(get1|get2) = p(aboth)/p(get2): ", (aboth / n) / (a2 / n)
print "p(get1|get2)/p(get2) = p(get1)p(get2)/p((get2) = p(get1) : ", a1 / n



