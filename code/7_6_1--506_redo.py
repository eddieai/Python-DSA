"""
归并排序 n*log_2(n)
使用递归 先对二分的左右两个列表排序，然后对左右半部合并排序
"""

def mergeSort(alist):
    if len(alist) == 1:
        return None

    print("splitting", alist)
    mid_idx = len(alist) // 2
    left = alist[:mid_idx]
    right = alist[mid_idx:]
    mergeSort(left)
    mergeSort(right)
    print("merging", alist)
    i, j = 0, 0
    for k in range(len(alist)):
        if i == len(left):
            alist[k] = right[j]
            j += 1
        elif j == len(right):
            alist[k] = left[i]
            i += 1
        elif left[i] < right[j]:
            alist[k] = left[i]
            i += 1
        else:
            alist[k] = right[j]
            j += 1
    print("merged", alist)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print(alist)
