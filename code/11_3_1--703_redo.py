"""
词梯问题
一个单词演变成另一个单词，每一步只能变一个字母
先建立单词图 只相差一个字母的单词有边相连
    创建大量的桶，每个桶可以存放若干单词，桶的标记是去掉一个字母，使用_占空
    所有匹配标记的单词都放在一个桶
    所有单词变成顶点后，对同一个桶中的单词建立边
然后使用广度优先搜索寻找最短路径
"""

from pythonds.graphs.adjGraph import Graph, Vertex
from pythonds.basic.queue import Queue

word_file = r"code\fourletterwords.txt"


def build_graph(word_file):
    d = {}
    g = Graph()
    with open(word_file, "r") as f:
        words = [line.strip() for line in f]
    for word in words:
        for i in range(len(word)):
            bucket = f"{word[:i]}_{word[i+1:]}"
            d.setdefault(bucket, []).append(word)

    for words_in_a_bucket in d.values():
        for word1 in words_in_a_bucket:
            for word2 in words_in_a_bucket:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g

# #  广度优先搜索
def bfs(g: Graph, start: str):
    start: Vertex = g.getVertex(start)
    start.setDistance(0)
    start.setPred(None)
    vertqueue = Queue()
    vertqueue.enqueue(start)
    while vertqueue.size() > 0:
        curr = vertqueue.dequeue()
        curr: Vertex
        for neighbor in curr.getConnections():
            neighbor: Vertex = g.getVertex(neighbor)
            if neighbor.getColor() == "white":
                neighbor.setColor("gray")
                neighbor.setDistance(curr.getDistance() + 1)
                neighbor.setPred(curr)
                vertqueue.enqueue(neighbor)
        curr.setColor("black")

# # 回溯节点  找到最短词梯
def traverse(g: Graph, target: str):
    res = []
    y: Vertex = g.getVertex(target)
    while True:
        res.append(y.getId())
        y = y.getPred()
        if y == None:
            break
    print(res[::-1])


word_graph = build_graph(word_file)  # 生成单词图
print("Number of vertices = ", len(word_graph.getVertices()))
num_edges = 0
for vertex in word_graph.getVertices():
    num_edges += len(word_graph.getVertex(vertex).getConnections())
print("Number of edges = ", num_edges)


print(word_graph.getVertex('FOOL'))
bfs(word_graph, "FOOL")  # 广度搜索
print(word_graph.getVertex("SAGE"))
traverse(word_graph, "SAGE")  # 打印词梯
