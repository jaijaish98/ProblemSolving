from collections import defaultdict


class Graph:
    def __init__(self):
        self.vertex = {}
        self.graph = defaultdict(list)
        self.pathList = []
        self.minDist = float("inf")
        self.distDict = {}

    def is_visited(self, vertexId, visited=False):
        self.vertex[vertexId] = visited

    def addEdge(self, u, v, d):
        self.graph[u].append(v)
        s =(u,v)
        self.distDict[s] = d

    def calculateDistance(self, path):
        dist = 0
        if len(path)==1:
            s = (path[0],path[1])
            if s in self.distDict:
                dist += self.distDict[s]
        else:
            for i in range(1,len(path)):
                s= (path[i-1],path[i])
                if s in self.distDict:
                    dist += self.distDict[s]
        return dist

    def isPathAvailable(self, u, d, path):
        self.vertex[u] = True
        path.append(u)
        if u == d:
            d = self.calculateDistance(path)
            if d<self.minDist:
                self.minDist = d
        else:
            for i in self.graph[u]:
                if self.vertex[i] is False:
                    self.isPathAvailable(i, d, path)
        path.pop()
        self.vertex[u] = False

    def getMinDistance(self, s, d):
        path = []
        self.isPathAvailable(s, d, path)
        if self.minDist < float("inf"):
            print(self.minDist)
        else:
            print(-1)

n = int(input())
g = Graph()
for i in range(n):
    vertexId = int(input())
    g.is_visited(vertexId=vertexId, visited=False)
edges = int(input())
for i in range(edges):
    u, v, d = input().split()
    g.addEdge(int(u),int(v), int(d))
s = int(input())
d = int(input())
g.getMinDistance(s, d)
"""
4
2
5
7
9
4
2 9 2
7 2 3
7 9 7
9 5 1
5
7
"""