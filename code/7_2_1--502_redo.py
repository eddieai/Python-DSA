"""
二分查找算法
针对有序表
每次将item和中间的元素进行比对
item更小则找左边 大则找右边
"""

def binarySearch(alist, item):
    left = 0
    right = len(alist) - 1
    while right >= left:
        mid_idx = left + (right - left) // 2
        if item == alist[mid_idx]:
            return True
        if item < alist[mid_idx]:
            right = mid_idx - 1
        if item > alist[mid_idx]:
            left = mid_idx + 1
    return False

# 使用递归解法
def RecursiveBinarySearch(alist, item):
    if not alist:
        return False

    mid_idx = len(alist) // 2
    if item == alist[mid_idx]:
        return True
    elif item < alist[mid_idx]:
        return RecursiveBinarySearch(alist[:mid_idx-1], item)
    elif item > alist[mid_idx]:
        return RecursiveBinarySearch(alist[mid_idx+1:], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(testlist, 17))
print(RecursiveBinarySearch(testlist, 17))
