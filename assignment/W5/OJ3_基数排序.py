"""
描述
实现一个基数排序算法，用于10进制的正整数从小到大的排序。

思路是保持10个队列(队列0、队列1......队列9、队列main)，开始，所有的数都在main队列，没有排序。

第一趟将所有的数根据其10进制个位(0~9)，放入相应的队列0~9，全放好后，按照FIFO的顺序，将每个队列的数合并排到main队列。

第二趟再从main队列队首取数，根据其十位的数值，放入相应队列0~9，全放好后，仍然按照FIFO的顺序，将每个队列的数合并排到main队列。

第三趟放百位，再合并；第四趟放千位，再合并。

直到最多的位数放完，合并完，这样main队列里就是排好序的数列了。

代码模板(建议复制粘贴使用)：

def func(mylist):
    # your code here
    return output

mylist = eval(input())
print(func(mylist))

输入
一个列表mylist，其中mylist包含一些需要排序的正整数，正整数互不相同且均不超过100000，且个数在1至1000之间。
输出
一个与mylist等长的列表。
样例输入
[8, 91, 34, 22, 65, 30, 4, 55, 18]
样例输出
[4, 8, 18, 22, 30, 34, 55, 65, 91]
"""


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return f"{self.items[::-1]}"


def func(mylist) -> list:
    # 请在此编写你的代码（可删除pass语句）
    radix_queues = [Queue() for _ in range(10)]
    main_queue = Queue()
    max_digit = len(str(max(mylist)))
    for num in mylist:
        main_queue.enqueue(num)
    for digit in range(max_digit):
        while not main_queue.isEmpty():
            num = main_queue.dequeue()
            radix = num // 10**digit % 10
            radix_queues[radix].enqueue(num)
        for i in range(10):
            while not radix_queues[i].isEmpty():
                main_queue.enqueue(radix_queues[i].dequeue())
    return main_queue


mylist = eval(input())
print(func(mylist))
