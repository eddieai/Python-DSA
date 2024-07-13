"""
创建无序表的节点  使用链表的方式
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def getData(self):
        return self.val

    def getNext(self):
        return self.next

    def setData(self, val):
        self.val = val

    def setNext(self, next):
        self.next = next


class UnorderedList:  # 无序表
    def __init__(self):
        self.head = None  # 表头


mylist = UnorderedList()
print(mylist.head)

mylist.head = Node(1)
print(mylist.head)
print(mylist.head.getData())
