"""
使用二叉树对全括号表达式建立表达式解析树
使用表达式解析树求值
"""
from pythonds.trees.binaryTree import BinaryTree
from pythonds.basic.stack import Stack
import operator


# 建立表达式解析树
def buildParseTree(fpexp: str):
    current = BinaryTree("")
    father_stack = Stack()
    for token in fpexp:
        if token == "(":
            current.insertLeft("")
            father_stack.push(current)
            current = current.getLeftChild()
        elif token in "+-*/":
            current = father_stack.pop()
            current.setRootVal(token)
            current.insertRight("")
            father_stack.push(current)
            current = current.getRightChild()
        elif token == ")":
            current = father_stack.pop()
        else:
            current.setRootVal(int(token))
    return current

# 使用递归的方法
# 基本结束条件：没有左右子节点
# 缩小规模： 将表达式分为左右子树
# 调用自身
opers = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

def evaluate(parseTree: BinaryTree):
    if not parseTree.getLeftChild() and not parseTree.getRightChild():
        return parseTree.getRootVal()

    left = evaluate(parseTree.getLeftChild())
    right = evaluate(parseTree.getRightChild())
    op = parseTree.getRootVal()
    return opers[op](left, right)


# # 9_7_1的方法 后序方法计算树
def post_order_eval(parseTree: BinaryTree):
    if parseTree:
        left = post_order_eval(parseTree.getLeftChild())
        right = post_order_eval(parseTree.getRightChild())
        root = parseTree.getRootVal()
        print("post order", root)
        if left and right:
            return opers[root](left, right)
        else:
            return root


# # 9_7_1的方法 前序方法计算树
def pre_order_eval(parseTree: BinaryTree):
    if parseTree:
        root = parseTree.getRootVal()
        print("pre order", root)
        left = pre_order_eval(parseTree.getLeftChild())
        right = pre_order_eval(parseTree.getRightChild())
        if left and right:
            return opers[root](left, right)
        else:
            return root


# # 9_7_1的方法 由树恢复回全括号表达式
def print_exp(parseTree: BinaryTree):
    res = ""
    if parseTree:
        res += (
            "(" + print_exp(parseTree.getLeftChild())
            if parseTree.getLeftChild()
            else ""
        )
        res += str(parseTree.getRootVal())
        print("in order", parseTree.getRootVal())
        res += (
            print_exp(parseTree.getRightChild()) + ")"
            if parseTree.getRightChild()
            else ""
        )
    return res

a = "((6-(5+(3*4)))/2)"
# a = "(3+(4*5))"
h = buildParseTree(a)
print(evaluate(h))
print(post_order_eval(h))
print(pre_order_eval(h))
print(print_exp(h))
