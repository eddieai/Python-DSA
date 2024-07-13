"""
通用的深度优先搜索
"""

from pythonds.graphs import Graph, Vertex


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0  # 增加一个time  记录当前时间

    def dfs(self):
        for vertex in self:
            vertex: Vertex
            vertex.setColor("white")
            vertex.setPred(-1)
        for vertex in self:
            if vertex.getColor() == "white":
                self.dfsvisit(vertex)

    def dfsvisit(self, startVertex: Vertex):  # 创建单棵深度优先树
        startVertex.setColor("gray")
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex_id in startVertex.getConnections():
            nextVertex: Vertex = self.getVertex(nextVertex_id)
            if nextVertex.getColor() == "white":
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor("black")
        self.time += 1
        startVertex.setFinish(self.time)


import unittest

class TestDFSGraph(unittest.TestCase):
    def setUp(self):
        self.graph = DFSGraph()
        self.vertices_id = ["A", "B", "C", "D", "E", "F", "G", "H"]
        for vertex_id in self.vertices_id:
            self.graph.addVertex(vertex_id)

        self.graph.addEdge("A", "B")
        self.graph.addEdge("A", "C")
        self.graph.addEdge("B", "D")
        self.graph.addEdge("B", "E")
        self.graph.addEdge("C", "F")
        self.graph.addEdge("C", "G")
        self.graph.addEdge("E", "H")

    def test_dfs(self):
        self.graph.dfs()

        # Check the colors of the vertices
        self.assertEqual(self.graph.getVertex(self.vertices_id[0]).getColor(), "black")  # A
        self.assertEqual(self.graph.getVertex(self.vertices_id[1]).getColor(), "black")  # B
        self.assertEqual(self.graph.getVertex(self.vertices_id[2]).getColor(), "black")  # C
        self.assertEqual(self.graph.getVertex(self.vertices_id[3]).getColor(), "black")  # D
        self.assertEqual(self.graph.getVertex(self.vertices_id[4]).getColor(), "black")  # E
        self.assertEqual(self.graph.getVertex(self.vertices_id[5]).getColor(), "black")  # F
        self.assertEqual(self.graph.getVertex(self.vertices_id[6]).getColor(), "black")  # G
        self.assertEqual(self.graph.getVertex(self.vertices_id[7]).getColor(), "black")  # H

        # Check the discovery and finish times
        [print(vertex.getDiscovery(), vertex.getFinish()) for vertex in self.graph]

        # Check the predecessor relationships
        self.assertEqual(self.graph.getVertex(self.vertices_id[1]).getPred().getId(), self.vertices_id[0])  # B's predecessor is A
        self.assertEqual(self.graph.getVertex(self.vertices_id[2]).getPred().getId(), self.vertices_id[0])  # C's predecessor is A
        self.assertEqual(self.graph.getVertex(self.vertices_id[3]).getPred().getId(), self.vertices_id[1])  # D's predecessor is B
        self.assertEqual(self.graph.getVertex(self.vertices_id[4]).getPred().getId(), self.vertices_id[1])  # E's predecessor is B
        self.assertEqual(self.graph.getVertex(self.vertices_id[5]).getPred().getId(), self.vertices_id[2])  # F's predecessor is C
        self.assertEqual(self.graph.getVertex(self.vertices_id[6]).getPred().getId(), self.vertices_id[2])  # G's predecessor is C
        self.assertEqual(self.graph.getVertex(self.vertices_id[7]).getPred().getId(), self.vertices_id[4])  # H's predecessor is E


if __name__ == "__main__":
    unittest.main()
