"""
描述
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
你需要按照以下要求，帮助老师给这些孩子分发糖果：
每个孩子至少分配到 1 个糖果。
相邻的孩子中，评分高的孩子必须获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？

示例代码模板：
def candy(ratings):
    # code here
    pass
lst = eval(input())
print(candy(lst))

输入
一个列表，以文本格式的有效Python表达式给出

输出
一行数字，表示满足分配条件所需的最少糖果数

样例输入
[1,2,2]

样例输出
4

提示
注：可行的分配方案为1、2、1 颗糖果；第三个孩子只得到1颗糖果也满足题目条件
"""


# def candy(ratings):
#     candies = [1] * len(ratings)
#     for i in range(len(ratings) - 1):
#         if ratings[i + 1] > ratings[i]:
#             candies[i + 1] = candies[i] + 1
#         elif ratings[i + 1] < ratings[i]:
#             if candies[i] == 1:
#                 for j in range(i, -1, -1):
#                     if ratings[j] <= ratings[j + 1]:
#                         break
#                     if candies[j] > candies[j + 1]:
#                         break
#                     candies[j] += 1

#     return sum(candies)


def candy(ratings):
    candies = [1] * len(ratings)
    for i in range(0, len(ratings) - 1):
        if ratings[i + 1] > ratings[i]:
            candies[i + 1] = candies[i] + 1

    for i in range(len(ratings) - 1, 0, -1):
        if ratings[i - 1] > ratings[i]:
            candies[i - 1] = max(candies[i] + 1, candies[i - 1])

    return sum(candies)

lst = eval(input())
print(candy(lst))
