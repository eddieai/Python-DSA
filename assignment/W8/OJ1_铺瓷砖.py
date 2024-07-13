"""
描述
题目内容：
给定一个长度为N的区域，及4种不同长度的瓷砖：灰瓷砖（长为1格）、红瓷砖（长为2格）、绿瓷砖（长为3格）与蓝瓷砖（长为4格），求所有不同的铺满整个区域的方法数。

输入
一个非负整数N

输出
一行数字，表示不同的方法总数

样例输入
5
0

样例输出
15
1
"""

N = int(input())

def solution(N, cache):
    if N in cache:
        return cache[N]
    if N==0:
        cache[N] = 1
        return 1

    count = 0
    for L in range(1, 5):
        if L <= N:
            count += solution(N-L, cache)
    cache[N] = count
    return count

print(solution(N, cache={}))
