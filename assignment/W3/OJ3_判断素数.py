"""
描述
输入一个正整数n, 编程判断n是否是素数。

输入
一个正整数

输出
是素数，输出"yes"，否则输出"no”。
（注意输出不包括引号）

样例输入
11

样例输出
yes

提示
1 <= n <= 2100000000
"""


n = int(input())

def solution(n):
    from math import sqrt
    if n == 1:
        return "no"
    elif n <= 3:
        return "yes"
    elif n % 2 == 0 or n % 3 == 0:
        return "no"
    for i in range(5, int(sqrt(n))+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return "no"
    return "yes"

print(solution(n))
