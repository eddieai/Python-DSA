"""
描述
给定一个二叉树结构，与一个整数列表，请将整数填充至二叉树对应节点内，使其成为一个二叉查找树；请输出该二叉查找树的层次遍历。下图展示了给定样例对应的二叉树结构：

输入
每个测试样例第一行包含一个整数，为二叉树的节点总数N。随后N行分别给定了编号由0至(N-1)的节点的左右子树编号，以空格分隔；若编号-1则代表对应子树为空。最后一行给出了以空格分隔的N个整数

输出
对填空后的二叉查找树进行层次遍历，按顺序输出整数序列，即从第1层根结点开始，逐层向下，同一层从左到右，以空格分隔，行尾无多余空格

样例输入
9
1 6
2 3
-1 -1
-1 4
5 -1
-1 -1
7 -1
-1 8
-1 -1
73 45 11 58 82 25 67 38 42

样例输出
58 25 82 11 38 67 45 73 42
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


def buildTree(node: BinaryTree, node_children):
    left, right = node_children
    if left != -1:
        node.setLeft(left)
        buildTree(node.getLeft(), nodes_children[left])
    if right != -1:
        node.setRight(right)
        buildTree(node.getRight(), nodes_children[right])


def fillTree(node: BinaryTree):
    if node:
        fillTree(node.getLeft())
        node.setRoot(nodes_val.pop())
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


N = int(input())
nodes_children = [list(map(int, input().split())) for _ in range(N)]
nodes_val = list(map(int, input().split()))

tree = BinaryTree(0)
buildTree(tree, nodes_children[0])
# print(tree)

nodes_val.sort(reverse=True)
fillTree(tree)
# print(tree)

levelOrderTraversal(tree)
