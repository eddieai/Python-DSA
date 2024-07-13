"""
题目内容：
给定一个字符串s与待查找字符串p，请给出使得s[i:i+len(p)]是p的一个字母重排的所有下标i
题目保证字符串p非空，且各字符串仅由小写字母构成

输入格式:
两行字符串，第一行为s，第二行为p

输出格式：
所有满足条件的下标从小到大排列，以空格分隔输出
若无对应下标，则输出字符串"none"

输入样例：
abababa
ab

输出样例：
0 1 2 3 4 5

输入样例2：
a
b

输出样例2：
none

参考代码模板：
def findAnagrams(s, p):
    # code here
    pass
s = input()
p = input()
findAnagrams(s, p)
"""

from collections import Counter


def findAnagrams(s, p):
    # code here
    p_counter = Counter(p)

    idx = []
    for i in range(len(s)-len(p)+1):
        p_counter_ = p_counter.copy()

        s_ = s[i:i+len(p)]
        check = True
        for c in s_:
            if c not in p_counter_:
                check = False
                break
            p_counter_[c] -= 1
            if p_counter_[c] < 0:
                check = False
                break
        if check:
            idx.append(i)

    if idx:
        print(*idx)
    else:
        print("none")


s = input()
p = input()
findAnagrams(s, p)
