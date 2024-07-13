"""
最短路径问题
使用广度优先搜索  每个节点记录距离
每次出列距离最小的点
通过更新修改距离和父节点
"""
from pythonds.graphs import PriorityQueue, Graph, Vertex


def dijkstra(graph: Graph, start: Vertex):  # dijkstra算法
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in graph])

    while not pq.isEmpty():
        curr: Vertex = pq.delMin()
        for next_id in curr.getConnections():
            next: Vertex = graph.getVertex(next_id)
            next_dist_new = curr.getWeight(next_id) + curr.getDistance()
            if next_dist_new < next.getDistance():
                next.setDistance(next_dist_new)
                next.setPred(curr)
                pq.decreaseKey(next, next_dist_new)


import unittest

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.vertices = ["A", "B", "C", "D", "E", "F"]
        for vertex in self.vertices:
            self.graph.addVertex(vertex)

        self.graph.addEdge("A", "B", 5)
        self.graph.addEdge("A", "C", 1)
        self.graph.addEdge("B", "D", 1)
        self.graph.addEdge("B", "E", 2)
        self.graph.addEdge("C", "B", 2)
        self.graph.addEdge("C", "D", 1)
        self.graph.addEdge("C", "E", 4)
        self.graph.addEdge("D", "E", 3)
        self.graph.addEdge("D", "F", 1)
        self.graph.addEdge("E", "F", 1)

    def test_dijkstra(self):
        start_vertex = self.graph.getVertex("A")
        dijkstra(self.graph, start_vertex)

        self.assertEqual(start_vertex.getDistance(), 0)
        self.assertEqual(self.graph.getVertex("B").getDistance(), 3)
        self.assertEqual(self.graph.getVertex("C").getDistance(), 1)
        self.assertEqual(self.graph.getVertex("D").getDistance(), 2)
        self.assertEqual(self.graph.getVertex("E").getDistance(), 5)
        self.assertEqual(self.graph.getVertex("F").getDistance(), 3)

        self.assertEqual(self.graph.getVertex("B").getPred().getId(), "C")
        self.assertEqual(self.graph.getVertex("C").getPred().getId(), "A")
        self.assertEqual(self.graph.getVertex("D").getPred().getId(), "C")
        self.assertEqual(self.graph.getVertex("E").getPred().getId(), "C")
        self.assertEqual(self.graph.getVertex("F").getPred().getId(), "D")


if __name__ == "__main__":
    unittest.main()
