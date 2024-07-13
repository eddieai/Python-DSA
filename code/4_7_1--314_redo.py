"""
无序表的链表实现
"""

class Node:
    def __init__(self, initdata):
        self.data = initdata  # 初始赋值
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:  # 无序表
    def __init__(self):
        self.head = None  # 表头

    def isEmpty(self):
        return self.head == None

    def size(self):
        n = 0
        curr = self.head
        while curr != None:
            n += 1
            curr = curr.getNext()
        return n

    def add(self, item):
        tmp = Node(item)
        tmp.setNext(self.head)
        self.head = tmp

    def search(self, item):
        curr = self.head
        while curr != None:
            if curr.getData() == item:
                return True
            curr = curr.getNext()
        return False

    def remove(self, item):
        found = False
        prev = None
        curr = self.head

        while curr != None:
            if curr.getData() == item:
                found = True
                break
            prev = curr
            curr = curr.getNext()

        if found:
            if prev == None:
                self.head = curr.getNext()
            else:
                prev.setNext(curr.getNext())

        return found

    def __str__(self):
        res = ""
        curr = self.head
        while curr != None:
            res += f", {curr.getData()}"
            curr = curr.getNext()
        return res[2:]


mylist = UnorderedList()
mylist.add(2)
print(mylist)
mylist.add(3)
print(mylist)
mylist.add(7)
print(mylist)
mylist.add(8)
print(mylist)
print(mylist.size(), '\n')
print(mylist.search(3), '\n')
print(mylist.remove(7), '\n')
print(mylist)
print(mylist.size(), '\n')
print(mylist.remove(10), "\n")
print(mylist)
print(mylist.remove(2), "\n")
print(mylist)
print(mylist.size(), "\n")
