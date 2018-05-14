import re, sys, os
from edge import Edge
from vertex import Vertex

if len(sys.argv) < 2:
    sys.exit(f"You didn't include a filename. Use the format 'python3 tsp.py <filename>'")

filename = sys.argv[1]

if not os.path.exists(filename):
    sys.exit(f"Error: File '{sys.argv[1]}' not found")

class TSP:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def addEdge(self, edge):
        self.edges.append(edge)

    def addVertex(self, vertex):
        self.vertices.append(vertex)

    # for finding how many vertices are needed
    # in the tsp, and they are added to the TSP
    def initializeVertices(self, filename):
        with open(filename) as f:
            first_line = f.readline()
            arr = first_line.split(" ")
            i = 0;
            while i < len(arr):
                self.addVertex(Vertex(i))
                i+=1

    # go through all the edges and add them to the TSP
    # are their respective vertices
    def addEdges(self, filename):
        with open(filename) as f:
            for num, line in enumerate(f, 1):
                numbers = line.split(" ");
                i = 0;
                for x in numbers:
                    weight = int(float(x))
                    if weight is not 0:
                        v1 = self.vertices[num-1]
                        v2 = self.vertices[i]
                        edge = Edge(v1, v2, weight)
                        self.addEdge(edge)
                        v1.addEdge(edge)
                    i += 1

tsp = TSP()
tsp.initializeVertices(filename)
tsp.addEdges(filename)

print(len(tsp.edges))
for v in tsp.vertices:
    print(v.toString())
