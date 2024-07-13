"""
描述
计算每个事件发生之时，往前算10000毫秒内有多少个事件发生，包含当事件；也即对于列表中的每个元素k，算出整个列表中有多少个元素介于k-10000和k（两端均含）之间。

代码模板(建议复制粘贴使用)：

def func(mylist):
    # your code here
    return output

mylist = eval(input())
print(func(mylist))

输入
一个已排序列表mylist，所有元素为非负整数，记录各个请求的发生时间，单位为毫秒。
输出
一个与mylist等长的列表。
样例输入
[0,10,100,1000,10000,20000,100000]
样例输出
[1, 2, 3, 4, 5, 2, 1]
"""


def func(mylist):
    if mylist:
        start = 0
        end = 0
        output = []
        for k in mylist:
            while start < len(mylist) and mylist[start] < k - 10000:
                start += 1
            while end < len(mylist) and mylist[end] <= k:
                end += 1
            output.append(end - start)
    else:
        output = []
    return output


mylist = eval(input())
print(func(mylist))
