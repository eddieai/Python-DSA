"""
表达式转换 转为后缀表达式
操作数直接输出，操作符需要对比栈内操作符再做决定
"""

from pythonds.basic.stack import Stack


def infixTopostfix(infixpr): # 中缀转后缀
    priority = {
        "(": 0,
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
    }

    infixpr = infixpr.split(" ")
    postfixpr = []
    ops_stack = Stack()

    for c in infixpr:
        if ord(c) in range(ord("A"), ord("Z")) or ord(c) in range(ord("0"), ord("9")):
            postfixpr.append(c)
        elif c == "(":
            ops_stack.push(c)
        elif c == ")":
            while ops_stack.peek() != "(":
                postfixpr.append(ops_stack.pop())
            ops_stack.pop()
        else:
            while not ops_stack.isEmpty() and priority[c] <= priority[ops_stack.peek()]:
                postfixpr.append(ops_stack.pop())
            ops_stack.push(c)

    while not ops_stack.isEmpty():
        postfixpr.append(ops_stack.pop())

    return "".join(postfixpr)


print(infixTopostfix('A * B + C * D'))