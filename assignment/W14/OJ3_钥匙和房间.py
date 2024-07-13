"""
描述
有 N 个房间，开始时你位于 0 号房间。每个房间有不同的号码：0，1，2，...，N-1，并且房间里可能有一些钥匙能使你进入下一个房间。
在形式上，对于每个房间 i 都有一个钥匙列表 rooms[i]，每个钥匙 rooms[i][j] 由 [0,1，...，N-1] 中的一个整数表示，其中 N = rooms.length。 钥匙 rooms[i][j] = v 可以打开编号为 v 的房间。
最初，除 0 号房间外的其余所有房间都被锁住。
你可以自由地在房间之间来回走动。
请判断是否可以最终打开所有房间。

输入
一行嵌套列表，列表长度为N，以合法的Python表达式格式给出

输出
True或False，代表是否可以进入所有房间

样例输入
[[1],[2],[3],[]]

样例输出
True
"""

def solution(key_list):
    N = len(key_list)
    rooms = [-1 for _ in range(N)]

    def dfs(room):
        if rooms[room] == -1:
            rooms[room] = 1
            for next_room in key_list[room]:
                dfs(next_room)

    dfs(0)
    if -1 in rooms:
        return False
    else:
        return True

key_list = eval(input())
print(solution(key_list))
