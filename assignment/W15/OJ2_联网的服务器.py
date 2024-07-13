"""
描述
给定一个二维列表表示的地图，其中每个位置值为 1 或 0 ；1 代表该位置存在一个服务器，0 代表该位置为空。对每个服务器来说，如果其所在的位置同一行或同一列有其它服务器，就称这个服务器是“联网”的。
请求出地图上所有联网的服务器的总数。

输入
一行，为一个以合法Python表达式给出的二维嵌套列表

输出
一行整数

样例输入
[[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]

样例输出
4
"""

def solution(map):
    row = len(map)
    col = len(map[0])
    servers = [[x, y] for x in range(row) for y in range(col) if map[x][y] == 1]

    res = 0
    for a in servers:
        xa, ya = a[0], a[1]
        for b in servers:
            xb, yb = b[0], b[1]
            if (xa == xb and ya != yb) or (xa != xb and ya == yb):
                res += 1
                break
    return res

map = eval(input())

print(solution(map))
