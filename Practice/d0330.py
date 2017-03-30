print "d0330,Hello world!"

from functools import partial

class Set:
    def __init__(self, values=None):
        self.dict = {}
        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        return "Set: " + str(self.dict.keys())

    def add(self, value):
        self.dict[value] = True

    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]


a = Set([1,1,2,3,4])
a.add(10)
print a

def exp(n,p):
    return n ** p

square_of = partial( exp, p=2)

print square_of(3)

def double(n): return 2 * n
def multiply(x,y): return x * y
def is_even(n): return n % 2 == 0

xss = [1,2,3,4,5]
print("xss = {}".format(xss))
print("map double xss = {}".format(map(double, xss)))
print("filter is_even xss = {}".format(filter(is_even,xss)))
print("reduce multiply xss = {}".format(reduce(multiply,xss)))

for i, document in enumerate(xss):
    print("i = {},e = {}".format(i, document))

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
print(zip(list1, list2))

pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
print(letters,numbers)

def magic(*args, **kwargs):
    print "unnamed args:", args
    print "keyword args:", kwargs
magic(1, 2, key="word", key2="word2")
