"""
描述
一开始给出了一个由小写字母组成的字符串 S。我们规定每次移动中，选择最左侧的字母，将其从原位置移除，并加到字符串的末尾。这样的移动可以执行任意多次

返回我们移动之后可以拥有的最小字符串（注：在Python3中，字符串的大小可用不等号比较）。

代码模板(建议复制粘贴使用)：

def func(S):
    # your code here
    return output

S = eval(input())
print(func(S))

输入
S。S为仅含有小写字母的字符串，长度不超过100000。
输出
一个与S等长的字符串。
样例输入
"cba"
样例输出
acb
"""


# class Queue(list):
#     def enqueue(self, item):
#         self.append(item)
#     def dequeue(self):
#         return self.pop(0)
#     def isEmpty(self):
#         return self == []
#     def size(self):
#         return len(self)


# def func(S):
#     q = Queue()
#     for c in S:
#         q.enqueue(c)
#     output = "z" * len(S)
#     curr = ""
#     while curr != S:
#         q.enqueue((q.dequeue()))
#         curr = "".join(q)
#         if curr < output:
#             output = curr
#     return output


def func(S):
    output = "z" * len(S)
    for _ in range(len(S)):
        newS = S[1:] + S[0]
        if newS < output:
            output = newS
        S = newS
    return output


S = eval(input())
print(func(S))
