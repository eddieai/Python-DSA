"""
使用双端队列判断回文词
两端同时移除字符判断是否相同，知道deque中剩下0或1个字符
"""

from pythonds.basic.deque import Deque

def palchecker(aString):
    charDeque = Deque()  # 创建双端队列

    for c in aString:
        charDeque.addFront(c)

    while charDeque.size() > 1:
        charFront = charDeque.removeFront()
        charRear = charDeque.removeRear()
        if charFront != charRear:
            return False

    return True

print(palchecker("radar"))
print(palchecker("lsdkjfskf"))
