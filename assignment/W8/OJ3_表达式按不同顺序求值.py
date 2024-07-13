"""
题目内容：
给定一个表达式字符串，求出按不同的求值顺序可能得到的所有结果

输入格式:
一行字符串，仅包含0-9与运算符+、-与*
*注：字符串保证三种运算符左右均为数字字符

输出格式：
所有不重复的可能的结果，从小到大排序并以半角逗号","分隔

输入样例：
2*3-4*5

输出样例：
-34,-14,-10,10

*注：
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

**示例代码模板：**
def findWays(expr):
    # 用于将字符串转为数字与运算符，供参考
    nums, ops = [], []
    num = 0
    for c in expr:
        if '0' <= c <= '9':
            num = num * 10 + ord(c) - 48
        else:
            ops.append(c)
            nums.append(num)
            num = 0
    else:
        nums.append(num)

    # code here

expr=input()
print(findWays(expr))
"""


def findWays(expr):
    # 用于将字符串转为数字与运算符，供参考
    nums, ops = [], []
    num = 0
    for c in expr:
        if "0" <= c <= "9":
            num = num * 10 + ord(c) - 48
        else:
            ops.append(c)
            nums.append(num)
            num = 0
    else:
        nums.append(num)

    cache = {}
    def solution(nums, ops):
        if (tuple(nums), tuple(ops)) in cache:
            return cache[tuple(nums), tuple(ops)]
        if len(nums) == 1:
            cache[tuple(nums), tuple(ops)] = {nums[0]}
            return cache[tuple(nums), tuple(ops)]

        res = set()
        for i, op in enumerate(ops):
            nums_left = nums[:i+1]
            nums_right = nums[i+1:]
            ops_left = ops[:i]
            ops_right = ops[i+1:]
            lefts = solution(nums_left, ops_left)
            rights = solution(nums_right, ops_right)
            for left in lefts:
                for right in rights:
                    res.add(eval(f"{left}{op}{right}"))
        cache[tuple(nums), tuple(ops)] = res
        return cache[tuple(nums), tuple(ops)]

    ways = solution(nums, ops)
    ways = map(str, sorted(list(ways)))
    return ",".join(ways)


# def findWays(expr):
#     cache = {}

#     def solution(expr):
#         if expr in cache:
#             return cache[expr]
#         if expr.isdigit():
#             cache[expr] = {int(expr)}
#             return cache[expr]

#         res = set()
#         for i, c in enumerate(expr):
#             if c in "+-*":
#                 op = c
#                 lefts = solution(expr[:i])
#                 rights = solution(expr[i + 1 :])
#                 for left in lefts:
#                     for right in rights:
#                         res.add(eval(f"{left}{op}{right}"))
#         cache[expr] = res
#         return cache[expr]

#     ways = solution(expr)
#     ways = map(str, sorted(list(ways)))
#     return ",".join(ways)

expr = input()
print(findWays(expr))
