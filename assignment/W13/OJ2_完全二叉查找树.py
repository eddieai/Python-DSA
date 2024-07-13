"""
描述
给定一系列整数，请构造相应的二叉树，使其既是二叉查找树又是完全二叉树；请输出满足条件的二叉树的层次遍历。

输入
一个整数序列，以空格分隔

输出
对应完全二叉查找树的层次遍历序列，即从第1层根结点开始，逐层向下，同一层从左到右，以空格分隔，行末无多余空格

样例输入
1 2 3 4 5 6 7 8 9 0

样例输出
6 3 8 1 5 7 9 0 2 4
"""

from collections import deque


class BinaryTree:
    def __init__(self, val) -> None:
        self.root = val
        self.left = None
        self.right = None

    def setLeft(self, val):
        if isinstance(val, BinaryTree):
            self.left = val
        else:
            self.left = BinaryTree(val)

    def setRight(self, val):
        if isinstance(val, BinaryTree):
            self.right = val
        else:
            self.right = BinaryTree(val)

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def setRoot(self, val):
        self.root = val

    def getRoot(self):
        return self.root

    def __str__(self):
        res = ""
        if self.left:
            res += str(self.left)
        res += str(self.root) + " "
        if self.right:
            res += str(self.right)
        return res


def buildTree(nodes: list):
    n_node = len(nodes)
    node_queue = deque()
    tree = BinaryTree(0)
    node_queue.append(tree)
    for i in range(1, n_node // 2 + 1):
        node: BinaryTree = node_queue.popleft()
        node.setRoot(i)
        if i * 2 <= n_node:
            node.setLeft(i * 2)
            node_queue.append(node.getLeft())
        if i * 2 + 1 <= n_node:
            node.setRight(i * 2 + 1)
            node_queue.append(node.getRight())
    return tree


def fillTree(node: BinaryTree):
    if node:
        fillTree(node.getLeft())
        node.setRoot(nodes.pop())
        fillTree(node.getRight())


def levelOrderTraversal(tree):
    res = []
    node_queue = deque()
    node_queue.append(tree)
    while node_queue:
        node: BinaryTree = node_queue.popleft()
        res.append(node.getRoot())
        if node.getLeft():
            node_queue.append(node.getLeft())
        if node.getRight():
            node_queue.append(node.getRight())
    print(*res)


nodes = list(map(int, input().split()))

tree = buildTree(nodes)
# print(tree)

nodes.sort(reverse=True)
fillTree(tree)
# print(tree)

levelOrderTraversal(tree)
