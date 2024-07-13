"""
创建无向图，使用邻接列表的方式
所有的顶点组成一个列表，每个顶点的边组成一个单独的列表
ADT graph
顶点类
图类
"""


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr_id, weight):
        self.connectedTo[nbr_id] = weight

    def __str__(self):  # 这样可以使用print打印
        return str(self.id)+ ' connectedTo ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return list(self.connectedTo.keys())

    def getId(self):
        return self.id

    def getWeight(self, nbr):  # 返回与某顶点之间的边值
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, key):  # 取顶点类
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vertList

    def addEdge(self, f, t, cost=0):  # 添加有向边，f -> t
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(t, cost)

    def getVertices(self):  # 取所有顶点
        return list(self.vertList.keys())

    def __iter__(self):
        return iter(self.vertList.values())


import unittest


class TestVertex(unittest.TestCase):
    def test_vertex_creation(self):
        v = Vertex(1)
        self.assertEqual(v.getId(), 1)
        self.assertEqual(str(v), "1 connectedTo []")

    def test_add_neighbor(self):
        v = Vertex(1)
        v.addNeighbor(2, 10)
        self.assertEqual(v.getConnections(), [2])
        self.assertEqual(v.getWeight(2), 10)


class TestGraph(unittest.TestCase):
    def test_add_vertex(self):
        g = Graph()
        v1 = g.addVertex(1)
        self.assertEqual(g.getVertex(1), v1)
        self.assertEqual(g.numVertices, 1)

    def test_add_edge(self):
        g = Graph()
        g.addEdge(1, 2, 10)
        self.assertIn(1, g)
        self.assertIn(2, g)
        v1 = g.getVertex(1)
        self.assertEqual(v1.getConnections(), [2])
        self.assertEqual(v1.getWeight(2), 10)

    def test_get_vertices(self):
        g = Graph()
        g.addVertex(1)
        g.addVertex(2)
        g.addVertex(3)
        self.assertListEqual(g.getVertices(), [1, 2, 3])

    def test_iterate_graph(self):
        g = Graph()
        g.addVertex(1)
        g.addVertex(2)
        g.addVertex(3)
        vertices = [v.getId() for v in g]
        self.assertListEqual(vertices, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
