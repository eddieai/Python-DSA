"""
描述
在一个小镇里，按从 1 到 N 标记了 N 个人。传言称，这些人中有一个是小镇上的秘密法官。
如果小镇的法官真的存在，那么：
1. 小镇的法官不相信任何人。
2. 每个人（除了小镇法官外）都信任小镇的法官。
3. 只有一个人同时满足属性 1 和属性 2 。
给定列表 trust，该列表由信任对 trust[i] = [a, b] 组成，表示标记为 a 的人信任标记为 b 的人。
如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的标记。否则，返回 -1。

输入
输入包含两行，第一行为一个正整数N，第二行为信任对列表trust，以合法的Python表达式给出

输出
一个整数，表示法官的编号

样例输入
4
[[1,3],[1,4],[2,3],[2,4],[4,3]]

样例输出
3
"""


# class Vertex:
#     def __init__(self, key) -> None:
#         self.key = key
#         self.connectedTo = {}

#     def addConnection(self, vertex, weight=0):
#         assert isinstance(vertex, Vertex)
#         self.connectedTo[vertex] = weight

#     def getConnections(self):
#         return self.connectedTo.keys()

#     def getKey(self):
#         return self.key

#     def __str__(self) -> str:
#         return f"Key: {self.key},\tConnections: {[f'vertex {vertex.getKey()}: weight {weight}' for vertex, weight in self.connectedTo.items()]}"


# class Graph:
#     def __init__(self) -> None:
#         self.vertices = {}

#     def __contains__(self, key):
#         return key in self.vertices

#     def addVertex(self, key):
#         assert not isinstance(key, Vertex)
#         if key not in self:
#             new_vertex = Vertex(key)
#             self.vertices[key] = new_vertex

#     def getVertex(self, key) -> Vertex:
#         assert not isinstance(key, Vertex)
#         if key in self:
#             return self.vertices[key]
#         else:
#             return None

#     def addEdge(self, key1, key2, weight=0):
#         assert not isinstance(key1, Vertex)
#         assert not isinstance(key2, Vertex)
#         if key1 not in self:
#             self.addVertex(key1)
#         if key2 not in self:
#             self.addVertex(key2)
#         self.getVertex(key1).addConnection(self.getVertex(key2), weight)

#     def getVertices(self):
#         return self.vertices.keys()

#     def __iter__(self):
#         return iter(self.vertices.values())


# def is_trusted_by_all(g, person):
#     for vertex in g:
#         vertex: Vertex
#         if person not in vertex.getConnections():
#             if person != vertex:
#                 return False
#     return True

# def find_judge(N, trust):
#     g = Graph()
#     for i in range(1, N + 1):
#         g.addVertex(i)
#     for a, b in trust:
#         g.addEdge(a, b)

#     for person in g:
#         person: Vertex
#         if not person.getConnections() and is_trusted_by_all(g, person):
#             return person.getKey()
#     return -1


def is_trusted_by_all(g, p):
    for v in g:
        if p not in g[v]:
            if p != v:
                return False
    return True

def find_judge(N, trust):
    g = {i: [] for i in range(1, N+1)}
    for a, b in trust:
        g[a].append(b)

    for p in g:
        if not g[p] and is_trusted_by_all(g, p):
            return p
    return -1


N = int(input())
trust = eval(input())
print(find_judge(N, trust))
