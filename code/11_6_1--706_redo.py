"""
骑士周游问题
按照走日字的方法，不重复的走完国际象棋的64个格子 每个格子走一次
先将合法走棋次序变成一个图
使用深度优先搜索算法找到长度为 row*col-1 长度的路径，路径上每个顶点出现一次
"""

from pythonds.graphs.adjGraph import Graph, Vertex


#  合法走棋的走法
def gen_legal_move(x, y, bdsize):  # x列，y行，bdsize是棋盘宽度
    newMoves = []
    move_offsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                    (1, -2), (1, 2), (2, -1), (2, 1)]
    for offset in move_offsets:
        x_new = x + offset[0]
        y_new = y + offset[1]
        if legal_cood(x_new, bdsize) and legal_cood(y_new, bdsize):
            newMoves.append((x_new, y_new))
    return newMoves

#  检查走棋是否在棋盘内
def legal_cood(x, bdsize):
    if 0 <= x < bdsize:
        return True
    else:
        return False

# 构建走棋关系图
def knight_graph(bdsize):
    ktGraph = Graph()
    for row in range(bdsize):
        for col in range(bdsize):
            nodeId = pos2node_id(row, col, bdsize)
            newMoves = gen_legal_move(row, col, bdsize)
            for x_new, y_new in newMoves:
                nodeId_new = pos2node_id(x_new, y_new, bdsize)
                ktGraph.addEdge(nodeId, nodeId_new)
    return ktGraph

# 将行列转换为唯一的id
def pos2node_id(row, col, bdsize):
    return row * bdsize + col

# Warnsdorff algorithm, 优先选择二级相邻节点（相邻节点的相邻节点）数量少的相邻节点
def ConnectionOderWarnsdorff(curr: Vertex, g: Graph):
    connection_id_list = []
    for connection_id in curr.getConnections():
        connection: Vertex = g.getVertex(connection_id)
        n_second_connection = len(connection.getConnections())
        connection_id_list.append((connection_id, n_second_connection))
    connection_id_list.sort(key=lambda x: x[1])
    return connection_id_list

# 深度优先搜索算法 n为当前深度，curr为当前顶点，path为已经走过的路径，limit为搜索总深度(棋盘格子数)
def knight_tour(n: int, g: Graph, curr_id: str, path: list, limit: int):
    curr: Vertex = g.getVertex(curr_id)
    curr.setColor("gray")
    path.append(curr_id)
    print(path)

    if n == limit:
        return True

    connection_id_list = ConnectionOderWarnsdorff(curr, g)
    for connection_id, _ in connection_id_list:
        connection: Vertex = g.getVertex(connection_id)
        if connection.getColor() == "white":
            if knight_tour(n + 1, g, connection_id, path, limit):
                return True

    curr.setColor("white")
    path.pop()

    return False


BDSIZE = 8
START_ID = 2

kt_graph = knight_graph(BDSIZE)
path = []
knight_tour(1, kt_graph, START_ID, path, BDSIZE * BDSIZE)
print(len(path))
