"""
描述
题目内容：

给定一个M进制的数，请将其转换为N进制并输出

输入
两行，第一行为空格分隔的两个数字，分别为10进制表示的M与N；其中M, N均满足2 ≤ M、N ≤ 36
第二行为待转换的M进制数字，其中每位超过9的部分从10至36分别用大写字母A-Z表示；输入数据保证数据的每一位不超过M

输出
一行字符串，表示转换后的N进制数

样例输入
8 16
471

样例输出
139
"""

import string


M, N = map(int, input().split(" "))
k = input()


def solution(k, M, N):
    table = [digit for digit in string.digits] + [
        letter for letter in string.ascii_uppercase
    ]

    def nbase2int(k):
        if len(k) == 1:
            return table.index(k)
        return nbase2int(k[:-1]) * M + table.index(k[-1])

    def int2nbase(k):
        if k < N:
            return table[k]
        return int2nbase(k // N) + table[k % N]

    return int2nbase(nbase2int(k))

print(solution(k, M, N))
