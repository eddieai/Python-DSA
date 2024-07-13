"""
描述
输入两个数a,b, 计算在[a,b]范围内，有多少个素数。

输入
2行, 每行一个正整数

输出
一个数，表示素数个数

样例输入
5
10

样例输出
2

提示
约定, a和b范围不超过10,000;
输入数据保证a
"""


a, b = map(int, [input() for _ in range(2)])

def check_prime(n):
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

def solution(a, b):
    count = 0
    for num in range(a, b+1):
        if check_prime(num) == "yes":
            count += 1
    return count

print(solution(a, b))
