"""
后缀表达式计算  先把中缀改成后缀 然后再运行后缀计算
"""

from pythonds.basic.stack import Stack


operator_priority = {
    "(": 0,
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "**": 3,
}


def infixTopostfix(infixpr): # 中缀转后缀
    infixpr = infixpr.split(" ")
    postfixpr = []
    ops_stack = Stack()

    for token in infixpr:
        if not token in operator_priority:
            postfixpr.append(token)
        elif token == "(":
            ops_stack.push(token)
        elif token == ")":
            while ops_stack.peek() != "(":
                postfixpr.append(ops_stack.pop())
            ops_stack.pop()
        else:
            while not ops_stack.isEmpty() and operator_priority[token] <= operator_priority[ops_stack.peek()]:
                postfixpr.append(ops_stack.pop())
            ops_stack.push(token)

    while not ops_stack.isEmpty():
        postfixpr.append(ops_stack.pop())

    return "".join(postfixpr), " ".join(postfixpr)


def posfixEval(posfixExpr): # 计算后缀
    posfixExpr = posfixExpr.split(" ")
    operand_stack = Stack()

    for token in posfixExpr:
        if token not in operator_priority:
            operand_stack.push(token)
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            res = eval(operand1+token+operand2)
            operand_stack.push(f"{res:.10f}")
    return operand_stack.pop()


_, posfixList = infixTopostfix('1 + 5 ** 2 - 6 / 3')
result = float(posfixEval(posfixList))
print(f"{posfixList}\n{result}")
