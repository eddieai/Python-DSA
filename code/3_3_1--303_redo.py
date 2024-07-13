"""
通用括号匹配算法
"""

from pythonds.basic.stack import Stack


def parChecker(pars):
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


print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))