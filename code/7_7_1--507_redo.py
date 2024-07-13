"""
快速排序
随意取一个中值  中值后一位为左标，列表末尾是右标
     左标右移，遇到大于中值的停止
     右标左移，遇到小于中值的停止
     交换左右标的数据
继续移动，直到左标移到右标右侧
交换中值和右标的位置
此时中值左半部比中值小 右半部比中值大
"""

def quickSort(alist):

    def quickSortHelper(alist, first, last):
        print(first, last, alist)

        if last <= first:
            return None

        left_mark, right_mark = first + 1, last
        while True:
            while left_mark <= right_mark and alist[left_mark] <= alist[first]:
                left_mark += 1
            while left_mark <= right_mark and alist[right_mark] >= alist[first]:
                right_mark -= 1

            if left_mark > right_mark:
                break
            else:
                alist[left_mark], alist[right_mark] = alist[right_mark], alist[left_mark]

        alist[first], alist[right_mark] = alist[right_mark], alist[first]

        quickSortHelper(alist, first, right_mark - 1)
        quickSortHelper(alist, right_mark + 1, last)

    quickSortHelper(alist, 0, len(alist) - 1)

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print(alist)
