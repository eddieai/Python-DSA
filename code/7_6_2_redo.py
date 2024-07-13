"""
归并排序 更简洁的写法
"""

def mergeSort(alist):
    if len(alist) == 1:
        return alist

    print("splitting", alist)
    mid_idx = len(alist) // 2
    left = mergeSort(alist[:mid_idx])
    right = mergeSort(alist[mid_idx:])

    print("merging", alist)
    merged = [None for _ in range(len(alist))]
    k = len(merged) - 1
    while left and right:
        if left[-1] > right[-1]:
            merged[k] = left.pop()
        else:
            merged[k] = right.pop()
        k -= 1
    merged[:k+1] = left if left else right
    print("merged", merged)

    return merged


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
alist_sorted = mergeSort(alist)
print(alist_sorted)
