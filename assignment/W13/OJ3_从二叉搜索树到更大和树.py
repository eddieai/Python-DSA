"""
描述
给定一个二叉搜索树，请修改树节点，使新树中每个节点的值等于原树中大于等于该节点的值之和；请输出修改后的树的层次遍历序列。

输入
一个不重复的整数序列，以空格分隔，为构造原二叉查找树的节点插入顺序
注：题目保证输入序列无重复

输出
修改后的树的层次遍历序列，即从第1层根结点开始，逐层向下，同一层从左到右，以空格分隔，行尾无多余空格

样例输入
6 1 8 3 4 9 2 7 5 0

样例输出
30 45 17 45 42 24 9 44 39 35
"""

from collections import deque


class BST:
    def __init__(self, key, val=None) -> None:
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def setLeft(self, key, val):
        self.left = BST(key, val)

    def setRight(self, key, val):
        self.right = BST(key, val)

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def setKeyVal(self, key=None, val=None):
        self.key = key if key else self.key
        self.val = val if val else self.val

    def getKeyVal(self):
        return (self.key, self.val)

    def __str__(self):
        res = ""
        if self.left:
            res += str(self.left)
        res += f"{self.key}: {self.val}, "
        if self.right:
            res += str(self.right)
        return res

    def insertItem(self, key, val):

        def helper(node: BST, key, val):
            if node:
                if node.getKeyVal()[0] < key:
                    if node.getRight():
                        helper(node.getRight(), key, val)
                    else:
                        node.setRight(key, val)
                else:
                    if node.getLeft():
                        helper(node.getLeft(), key, val)
                    else:
                        node.setLeft(key, val)

        helper(self, key, val)


keys = list(map(int, input().split()))
keys_sort = sorted(keys)
key_val_dict = {}
for i, key in enumerate(keys_sort):
    key_val_dict[key] = sum(keys_sort[i:])

tree = BST(keys[0], key_val_dict[keys[0]])
for key in keys[1:]:
    tree.insertItem(key, key_val_dict[key])

res = []
node_queue = deque()
node_queue.append(tree)

while node_queue:
    node: BST = node_queue.popleft()
    res.append(node.getKeyVal()[1])
    if node.getLeft():
        node_queue.append(node.getLeft())
    if node.getRight():
        node_queue.append(node.getRight())

print(*res)
