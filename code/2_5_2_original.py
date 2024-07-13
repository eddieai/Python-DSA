"""
Import另一个文件中的函数，然后使用timeit
"""


from timeit import Timer

# 需要把另一个文件名改成字母才能使用
t1 = Timer("test1()", "from a import test1")
print ("concat %f seconds\n" % (t1.timeit(number=1000)))
