from collections import defaultdict


class Graph:
    def __init__(self):
        self.vertex = {}
        self.graph = defaultdict(list)
        self.trouble_vertices = []

    def is_visited(self, vertexId, visited=False):
        self.vertex[vertexId] = visited

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def getTroubleVertex(self, path):
        if len(path) == 1:
            self.trouble_vertices.append(path[0])
        elif len(path) > 1:
            self.trouble_vertices.append(path[-2])

    def isPathAvailable(self, u, d, path):
        self.vertex[u] = True
        path.append(u)
        if u == d:
            self.getTroubleVertex(path=path)
        else:
            for i in self.graph[u]:
                if self.vertex[i] is False:
                    self.isPathAvailable(i, d, path)
        path.pop()
        self.vertex[u] = False

    def isPathAvailableInGraph(self, s, d):
        path = []
        self.isPathAvailable(s, d,path)
        if len(self.trouble_vertices)>0:
            print(* self.trouble_vertices, sep=' ')

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
g.isPathAvailableInGraph(s, d)
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
5
2
"""