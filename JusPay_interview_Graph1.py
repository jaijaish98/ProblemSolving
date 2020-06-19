from collections import defaultdict


class Graph:
    def __init__(self):
        self.vertex = {}
        self.graph = defaultdict(list)

    def is_visited(self, vertexId, visited=False):
        self.vertex[vertexId] = visited

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isPathAvailable(self, u, d):
        self.vertex[u] = True
        if u == d:
            return True
        else:
            for i in self.graph[u]:
                if self.vertex[i] is False:
                    return self.isPathAvailable(i, d)
        self.vertex[u] = False
        return False

    def isPathAvailableInGraph(self, s, d):
        path = []
        return self.isPathAvailable(s, d)


n = int(input())
g = Graph()
for i in range(n):
    vertexId = int(input())
    g.is_visited(vertexId=vertexId, visited=False)
edges = int(input())
for i in range(edges):
    u,v= input().split()
    g.addEdge(int(u),int(v))
s = int(input())
d = int(input())
print(1) if g.isPathAvailableInGraph(s, d) else print(0)
"""
4
2
5
7
9
4
2 9
7 2
7 9
9 5
7
9
"""