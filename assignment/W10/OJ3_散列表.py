"""
题目内容：
给定一个指定大小N的散列表，并输入一系列数字：若找到空槽，则插入该数字，并返回槽位置；若该数字在散列表中存在，则直接输出其位置。
注：使用下标增加的二次探测法解决散列冲突
注2：散列表实际大小应确定为不小于用户输入N的最小质数

输入格式:
两行
第一行为用户指定散列表大小N
第二行为一系列数字，以空格分隔

输出格式：
逐个输出对应数字在散列表中位置，以空格分隔
若该数字无法插入，则输出“-”

输入样例：
4
10 6 4 10 15

输出样例：
0 1 4 0 -

参考代码模板：
def createHashTable(n):
    # code here
    pass
def insertNumbers(table, nums):
    # code here
    pass
n = int(input())
nums = list(map(int, input().split()))
table = createHashTable(n)
insertNumbers(table, nums)
"""

def createHashTable(n):
    # code here
    def next_prime(x):
        if x <= 1:
            return 2
        n = x
        while True:
            if all(n % i != 0 for i in range(2, int(n ** 0.5) + 1)):
                return n
            n += 1

    table_size = next_prime(n)
    return [None] * table_size


def insertNumbers(table, nums):
    # code here
    table_size = len(table)

    def hash_func(key):
        return key % table_size

    def rehash_func(key, i):
        return (hash_func(key) + i * i) % table_size

    res = []
    for num in nums:
        hash = hash_func(num)

        i = 1
        while table[hash] != None and table[hash] != num:
            hash = rehash_func(num, i)
            if hash == hash_func(num):
                break
            i += 1

        if table[hash] == None:
            table[hash] = num
            res.append(hash)
        elif table[hash] == num:
            res.append(hash)
        else:
            res.append("-")

    print(*res)


n = int(input())
nums = list(map(int, input().split()))
table = createHashTable(n)
insertNumbers(table, nums)
