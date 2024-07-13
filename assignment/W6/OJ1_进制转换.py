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
source = input()


def solution(source, M, N):
    source_base_10 = 0
    for i, digit in enumerate(source):
        if "A" <= digit <= "Z":
            digit = 10 + (ord(digit) - ord("A"))
        else:
            digit = int(digit)
        source_base_10 += digit * M ** (len(source) - 1 - i)

    def base_convert(num):
        table = [digit for digit in string.digits] + [letter for letter in string.ascii_uppercase]
        if num < N:
            return table[num]
        return base_convert(num // N) + table[num % N]

    target = base_convert(source_base_10)
    return target

print(solution(source, M, N))
