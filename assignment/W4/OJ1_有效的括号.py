"""
描述
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
输入
一行字符串

输出
True或False，表示该输入是否为合法括号串

输入样例1
([])

输出样例1
True

输入样例2
{{)]}

输出样例2
False
"""


pars = input()


class Stack(list):
    push = list.append
    peek = lambda self: self[-1]
    isEmpty = lambda self: not len(self)
    size = list.__len__


def solution(pars):
    open_close = {
        "(": ")",
        "[": "]",
        "{": "}",
    }

    stack = Stack()
    for par in pars:
        if par in ["(", "[", "{"]:
            stack.push(par)
        if par in [")", "]", "}"]:
            if stack.isEmpty():
                return False
            if par != open_close[stack.peek()]:
                return False
            stack.pop()

    if not stack.isEmpty():
        return False
    return True

print(solution(pars))
