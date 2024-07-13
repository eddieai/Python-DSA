"""
最小生成树
解决广播问题  所有节点都要收到一次信息
选择具有最小权重的生成树
使用贪心算法 Prim  每次添加一条权重最小的可以添加的边（一端在树里，一端连外面的点）
"""

from pythonds.graphs import PriorityQueue, Graph, Vertex
import sys


def prim(graph: Graph, start: Vertex):
    pq = PriorityQueue()  # 建立优先队列
    for v in graph:
        v: Vertex
        v.setDistance(sys.maxsize)
        v.setPred(None)
        pq.add((v.getDistance(), v))
    start.setDistance(0)

    while not pq.isEmpty():
        curr: Vertex = pq.delMin()
        for next_id in curr.getConnections():
            next: Vertex = graph.getVertex(next_id)
            next_dist_new = curr.getWeight(next_id)
            if next in pq and next_dist_new < next.getDistance():
                next.setDistance(next_dist_new)
                next.setPred(curr)
                pq.decreaseKey(next, next_dist_new)
