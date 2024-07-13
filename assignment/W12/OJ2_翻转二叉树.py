"""
描述
给定一个二叉树，请给出它的镜面翻转。
为方便起见，本题只给出完全二叉树的层次遍历，请给出相应的翻转二叉树的中序遍历。

备注:
这个问题来自开源软件开发者Max Howell在Google面试被拒的经历 ：
谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了

输入
一行空格分隔的整数序列，表示一个完全二叉树的层次遍历

输出
一行空格分隔的整数序列，表示翻转后的二叉树的中序遍历

样例输入
4 2 7 1 3 6 9

样例输出
9 7 6 4 3 2 1
"""

def solution(lst):
    def iterate(lst, i):
        if i > len(lst) - 1:
            return []
        return iterate(lst, i * 2 + 1) + [lst[i]] + iterate(lst, i * 2)
    print(*iterate([0] + lst, 1))

lst = input().split(" ")
solution(lst)
