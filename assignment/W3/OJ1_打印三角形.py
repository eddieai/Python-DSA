"""
描述
给定一个整数n(1<=n<=40), 输出一个边长为n的"*"字符构成的直角三角形图案。

输入
1个整数

输出
一个"*"字符构成的直角三角形图案。

样例输入
4

样例输出
*
**
***
****

提示
两重循环
"""


n = int(input())

def solution(n):
    return "\n".join(["*" * i for i in range(1, n+1)])

print(solution(n))
