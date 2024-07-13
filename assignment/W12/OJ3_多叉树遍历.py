"""
描述
给定以嵌套列表形式给出的多叉树，求它的后序遍历
注：每个代表非空多叉树的列表包含至少一项；列表第一项代表节点值，其后每一项分别为子树；遍历子树时以列表下标从小到大的顺序进行。

输入
一行合法的Python表达式，可解析为嵌套列表形式的多叉树结构

输出
一行整数，以空格分隔

样例输入
[1,[2,[3,[4],[5]],[6]],[7],[8,[9],[10]]]

样例输出
4 5 3 6 2 7 9 10 8 1
"""

def iterate(tree):
    if len(tree) == 1:
        return tree
    if len(tree) == 0:
        return []

    res = []
    for i in range(1, len(tree)):
        res += iterate(tree[i])
    res += [tree[0]]
    return res

tree = eval(input())
print(*iterate(tree))
