"""
二插堆实现
使用一个列表来保存堆数据，可以发现节点p的父节点索引为p//2，左节点为2p，右节点为2p+1
插入节点：插在尾部，然后上浮到合适的位置（与父节点比较大小并交换）
移去最小节点：return根结点的值并移走，然后将其赋值为最后一个节点，然后对该节点进行下沉
    （与子节点比较大小并交换位置） 如果比子节点大，选择较小的一个下沉，如果比两个子节点都小，则停止
建立二叉堆
"""


class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def float_up(self, i):  # 上浮函数
        while i // 2 > 0:
            parent_idx = i // 2
            if self.heapList[i] < self.heapList[parent_idx]:
                self.heapList[i], self.heapList[parent_idx] = self.heapList[parent_idx], self.heapList[i]
            i //= 2

    def insert(self, k):  # 向二叉堆插入k
        self.heapList.append(k)
        self.currentSize += 1
        self.float_up(self.currentSize)

    def min_child(self, i):  # 返回最小的子节点
        left_child_idx = i * 2
        right_child_idx = i * 2 + 1
        if right_child_idx > self.currentSize:
            return left_child_idx
        else:
            return left_child_idx if self.heapList[left_child_idx] < self.heapList[right_child_idx] else right_child_idx

    def sink_down(self, i):  # 下沉函数
        while i * 2 <= self.currentSize:
            min_child_idx = self.min_child(i)
            if self.heapList[i] > self.heapList[min_child_idx]:
                self.heapList[i], self.heapList[min_child_idx] = self.heapList[min_child_idx], self.heapList[i]
            i = min_child_idx

    def del_min(self):  # 删除二叉堆中最小的数（根节点）
        min = self.heapList[1]
        self.heapList[1] = self.heapList.pop()
        self.currentSize -= 1
        self.sink_down(1)
        return min

    def buildHeap(self, lst):   # 从无序表生成堆，O(n)
        self.heapList = [0] + lst[:]
        self.currentSize = len(lst)
        i = self.currentSize // 2
        while i > 0:
            print(self.heapList, i)
            self.sink_down(i)
            i -= 1
        print(self.heapList, i)


# Test case 1: Inserting elements in a random order
print("Test case 1:")
bin_heap = BinHeap()
for num in [5, 3, 8, 4, 6]:
    bin_heap.insert(num)
    print(bin_heap.heapList)

# Test case 2: Inserting elements in an ascending order
print("\nTest case 2:")
bin_heap = BinHeap()
for num in [1, 2, 3, 4, 5]:
    bin_heap.insert(num)
    print(bin_heap.heapList)

# Test case 3: Inserting elements in a descending order
print("\nTest case 3:")
bin_heap = BinHeap()
for num in [5, 4, 3, 2, 1]:
    bin_heap.insert(num)
    print(bin_heap.heapList)

# Test case 4: Building a heap from an unordered list
print("\nTest case 4:")
bin_heap = BinHeap()
bin_heap.buildHeap([10, 5, 8, 2, 11])

# Test case 5: Deleting the minimum element from a heap
print("\nTest case 5:")
bin_heap = BinHeap()
for num in [5, 3, 8, 4, 6]:
    bin_heap.insert(num)
print("Before deleting the minimum element:", bin_heap.heapList)
bin_heap.del_min()
print("After deleting the minimum element:", bin_heap.heapList)
