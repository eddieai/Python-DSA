"""
python 数据类型的各种操作的大O
"""
from timeit import Timer

def test1():    # concat
    l = []
    for i in range(1000):
        l = l + [i]
def test2():    # self-concat
    l = []
    for i in range(1000):
        l += [i]
def test3():    # extend
    l = []
    for i in range(1000):
        l.extend([i])
def test4():    # append
    l = []
    for i in range(1000):
        l.append(i)
def test5():    # assign
    l = [0] * 1000
    for i in range(1000):
        l[i] = i
def test6():    # comprehension
    l = [i for i in range(1000)]
def test7():    # list range
    l = list(range(1000))


for i in range(1, 8):
    t = Timer(f"test{i}()", f"from __main__ import test{i}")
    print (f"t{i} %f seconds\n" % (t.timeit(number=10000)))
