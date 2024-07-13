"""
描述
开心消消乐我们都熟悉，我们可以用刚学过的栈来做一个“一维”的开心消消乐游戏，这个游戏输入一串字符，逐个消去相邻的相同字符对。
如果字符全部被消完，则输出不带引号的“None”

输入
一个字符串，可能带有相邻的相同字符，如“aabbbc”

输出格式
一个字符串，消去了相邻的成对字符，如“bc”

输入样例1
beepooxxxyz

输出样例1
bpxyz

输入样例2
kxkx

输出样例2
kxkx

输入样例3
（这里bb被消了以后，第二个a挨上来了，所以两个a也相邻，同样消去）
abbacddccc00

输出样例3
None
"""


chars = input()


class Stack(list):
    push = list.append
    peek = lambda self: self[-1]
    isEmpty = lambda self: not len(self)
    size = list.__len__


def solution(chars):
    char_stack = Stack()
    for char in chars:
        if char_stack.isEmpty():
            char_stack.push(char)
        elif char != char_stack.peek():
            char_stack.push(char)
        else:
            char_stack.pop()

    if char_stack.isEmpty():
        return None

    return "".join(char_stack)


print(solution(chars))
