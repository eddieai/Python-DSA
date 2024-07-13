"""
描述
洗碗工小明碰上了一位强迫症老板老王，餐厅一共就10只盘子，老板给仔细编上了0～9等10个号码，并要求小明按照从0到9的编号来洗盘子，当然，每洗好一只盘子，就必须得整齐叠放起来。
小明洗盘子期间，经常就有顾客来取盘子，当然每位顾客只能从盘子堆最上面取1只盘子离开。
老王在收银台仔细地记录了顾客依次取到盘子的编号，比如“1043257689”，对于某些记录，他能断定小明没有遵照命令按照0123456789的次序来洗盘子。
你也能像老王一样作出准确的判断吗？

输入
长度为10的字符串，其中只包含0～9的数字，且不重复，代表顾客依次取到的盘子编号。

输出
字符串：Yes或者No，表示可能遵照次序洗盘子，或者肯定没有遵照次序洗盘子。

输入样例
1043257689

输出样例
Yes
"""


index = input()


class Stack(list):
    push = list.append
    peek = lambda self: self[-1]
    isEmpty = lambda self: not len(self)
    size = list.__len__


def solution_(index):
    index = [int(ind) for ind in index]
    index_stack = Stack()
    for ind in index:
        if index_stack.isEmpty():
            index_stack.push(ind)
        elif ind < index_stack.peek():
            index_stack.push(ind)
        else:
            last1 = index_stack.pop()
            while not index_stack.isEmpty():
                last2 = index_stack.peek()
                if last2 != last1 + 1:
                    return "No"
                last1 = index_stack.pop()
    return "Yes"


def solution(takens):
    takens = [int(taken) for taken in takens]
    washed = Stack()
    washing = 0
    i = 0
    while i < 10 and washing < 10:
        # 客人拿到盘子N，即代表N之前的盘子都洗完了，把这些洗好的盘子堆起来
        taken = takens[i]
        if washing <= taken:
            for disk in range(washing, taken+1):
                washed.push(disk)
            washing = taken + 1
        else:
            return "No"

        # 在洗好的盘子堆上，模拟客人拿走的那些盘子
        while not washed.isEmpty() and washed.peek() == takens[i]:
            washed.pop()
            i += 1

    if washed.isEmpty():
        return "Yes"
    return "No"


print(solution(index))