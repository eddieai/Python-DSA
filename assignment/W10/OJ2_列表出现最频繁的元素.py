"""
题目内容：
给定一个列表与数字K，按出现次数倒序输出列表中前K个出现最频繁的元素；若少于K个元素则返回所有元素。若有两个或以上的元素出现次数相等，按元素的值进行顺序输出，小的在前。

输入格式:
输入为两行
第一行为给定列表，以合法的Python表达式给出
第二行为数字K

输出格式：
不多于K个数字，以空格分隔

输入样例：
[2,1,1,1,2,2,3]
2

输出样例：
1 2

参考代码模板：
def topKFrequent(nums, k):
    # code here
    pass

lst = eval(input())
k = int(input())
topKFrequent(lst, k)
"""

from collections import Counter

def topKFrequent(nums, k):
    # code here
    nums_counter = Counter(nums)
    nums_counter_sort = sorted(nums_counter.items(), key=lambda x: (-x[1], x[0]))
    res = [item[0] for item in nums_counter_sort[:k]]
    print(*res)

lst = eval(input())
k = int(input())
topKFrequent(lst, k)
