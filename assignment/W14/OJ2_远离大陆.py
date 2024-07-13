"""
描述
你现在手里有一份大小为 M x N 的『地图』（网格） grid，上面的每个『区域』（单元格）都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地
对于每个海洋方格，其存在一个距离它最近的陆地方格，相应有一个到陆地的最小距离
请输出上述所有最小距离中的最大值。
我们这里说的距离是『曼哈顿距离』（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 - x1| + |y0 - y1| 。
如果地图上只有陆地或者海洋，请返回 -1。

输入
输入共1行，为一个仅包含0与1的嵌套列表，用合法的Python表达式给出

输出
一个整数，表示最短距离

样例输入
[[1,0,1],[0,0,0],[1,0,1]]

样例输出
2

提示
注：最远的海洋区域坐标为(1,1)
"""

from collections import deque

def solution(grid):
    grid = grid[:]
    M, N = len(grid), len(grid[0])
    layer = deque([[x, y, 0] for x in range(M) for y in range(N) if grid[x][y] == 1])
    res = -1
    if len(layer) == 0 or len(layer) == M*N:
        return res

    while layer:
        x, y, d = layer.popleft()
        res = max(res, d)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == 0:
                grid[nx][ny] = 2
                layer.append([nx, ny, d + 1])
    return res

grid = eval(input())
print(solution(grid))
