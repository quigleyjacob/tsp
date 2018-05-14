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

tsp = TSP()

v1 = Vertex()
v2 = Vertex()
edge = Edge(v1, v2, 23)
tsp.addVertex(v1)
tsp.addVertex(v2)
v1.addEdge(edge)
v2.addEdge(edge)
tsp.addEdge(edge)

with open(filename) as f:
    for num, line in enumerate(f, 1):
        numbers = line.split(" ");
        for x in range(len(numbers)):
            print(numbers[x], end=" ")
        print("");
