"""
描述
给定一个整数n(1<=n<=20), 输出n的阶乘(=1*2*3*...*n)。

输入
1个整数

输出
整数的阶乘值

样例输入
4

样例输出
24
"""


n = int(input())

def solution(n):
    from functools import reduce
    return reduce(lambda x, y: x * y, list(range(1, n+1)))

print(solution(n))
