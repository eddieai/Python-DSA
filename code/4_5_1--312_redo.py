"""
建立双端队列 首尾都可以移除和添加
列表末是队首
"""

class Deque:
    def __init__(self) -> None:
        self.items = []

    def addRear(self, item):
        self.items.insert(0, item)

    def addFront(self, item):
        self.items.append(item)

    def removeRear(self):
        return self.items.pop(0)

    def removeFront(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)