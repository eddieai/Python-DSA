"""
写一个栈的类型
"""

class Stack_Complex:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def size(self):
        return len(self.items)


class Stack(list):
    push = list.append
    peek = lambda self: self[-1]
    isEmpty = lambda self: not len(self)
    size = list.__len__


s = Stack()
print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
print(s.pop())
print(s.size())
print(s)