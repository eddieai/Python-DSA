"""
描述
给定一种序列化二叉树的方式：从根节点起始按层次遍历二叉树所有“可能”存在节点的位置：若该位置存在节点，则输出节点值，并在下一层相应增加两个可用位置；否则输出None，且不增加下一层的可用位置。

例如"[5, 4, 7, 3, None, 2, None, -1, None, 9]"是下面所示的二叉树序列化的结果，其中结构为【本节点，【左子树】，【右子树】】：
【5，【4，【3，【-1，【】，【】】，【】】，【】】，【7，【2，【9，【】，【】】，【】】，【】】】
现给出一个二叉树以这种形式序列化的结果，请复原该二叉树并给出它的中序遍历。

输入格式:
一行合法的Python表达式，可解析为包含整数与None的列表

输出格式：
二叉树中序遍历的整数序列，以空格分隔

输入样例：
[5, 4, 7, 3, None, 2, None, -1, None, 9]
输出样例：
-1 3 4 5 9 2 7

输入样例2：
[5,1,4,None,None,3,6]
输出样例2：
1 5 3 4 6
"""

# 方法1：
from collections import deque

class BinaryTree:
    def __init__(self, val):
        self.root = val
        self.left = None
        self.right = None

    def insertLeft(self, val):
        self.left = BinaryTree(val)

    def insertRight(self, val):
        self.right = BinaryTree(val)

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def setRootVal(self, val):
        self.root = val

    def getRootVal(self):
        return self.root

def lst2linktree(lst):
    root = BinaryTree(lst[0])
    q = deque()
    q.append(root)

    for val in lst[1:]:
        if not q[0].getLeft():
            q[0].insertLeft(val)
            q.append(q[0].getLeft())
        else:
            q[0].insertRight(val)
            q.append(q[0].getRight())
            while True:
                q.popleft()
                if q[0].getRootVal():
                    break
    return root

def in_order_iterate_linktree(root):
    if not root or not root.getRootVal():
        return []
    res = (
        in_order_iterate_linktree(root.getLeft())
        + [root.getRootVal()]
        + in_order_iterate_linktree(root.getRight())
    )
    return res


# 方法2：
def lst2arraytree(lst):
    tree = [0] + lst[:]
    i = 1
    while i < len(tree):
        if tree[i]:
            parent_idx = i // 2
            while tree[parent_idx] == None:
                parent_idx += 1
            true_i = parent_idx * 2 + i % 2
            tree = tree[:i] + [None] * (true_i - i) + tree[i:]
        i += 1
    return tree

def in_order_iterate_arraytree(tree, idx):
    if idx > len(tree) - 1 or not tree[idx]:
        return []
    res = (
        in_order_iterate_arraytree(tree, idx * 2)
        + [tree[idx]]
        + in_order_iterate_arraytree(tree, idx * 2 + 1)
    )
    return res


lst = eval(input())
print(*in_order_iterate_linktree(lst2linktree(lst)))
print(*in_order_iterate_arraytree(lst2arraytree(lst), 1))
