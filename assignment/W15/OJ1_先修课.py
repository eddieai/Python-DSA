"""
描述
有 n 门课程要选，其编号分别由 0 至 n-1
每个课程都有一些需要提前学完的先修课程：例如，假设在学习课程 0 前需要先学习课程 1 ，我们用一个先修关系对[0, 1]来表示这种 “后学习课程，先修课程” 的关系
现给定一系列课程与若干先修关系，请判断是否存在一个方案可以学完所有课程

参考代码模板：
def canFinish(self, n, pre):
    # code here
    pass

n = int(input())
pre = eval(input())
print(canFinish(n, pre))

输入
输入分为两行，第一行为一个整数，表示课程的总数
第二行为一个嵌套列表的Python表达式，包含若干先修关系对

输出
True或False，表示是否存在一个按照先修关系学完所有课程的顺序

样例输入
2
[[1,0],[0,1]]

样例输出
False
"""


def canFinish(n, pre):
    # code here
    pre_courses = [[] for _ in range(n)]
    for a, b in pre:
        pre_courses[a].append(b)

    colors = ["white" for _ in range(n)]

    def is_DAG(id):
        if colors[id] == "black":
            return True
        elif colors[id] == "gray":
            return False
        elif colors[id] == "white":
            colors[id] = "gray"
            for pre_id in pre_courses[id]:
                if not is_DAG(pre_id):
                    return False
            colors[id] = "black"
            return True

    for id in range(n):
        if not is_DAG(id):
            return False
    return True


n = int(input())
pre = eval(input())
print(canFinish(n, pre))
