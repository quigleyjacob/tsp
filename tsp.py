from edge import Edge
from vertex import Vertex

class TSP:
    def __init__(self, filename):
        self.vertices = []
        self.edges = []
        # for finding how many vertices are needed
        # in the tsp, and they are added to the TSP
        with open(filename) as f:
            first_line = f.readline()
            arr = first_line.split(" ")
            i = 0;
            while i < len(arr):
                self.addVertex(Vertex(i))
                i+=1

        # go through all the edges and add them to the TSP
        # are their respective vertices
        with open(filename) as f:
            for num, line in enumerate(f, 1):
                numbers = line.split(" ");
                while len(numbers) > 0 and numbers[0] is not "0":
                    numbers.pop(0)
                for i, x in enumerate(numbers, 0):
                    weight = int(float(x))
                    if weight is not 0:
                        v1 = self.vertices[num-1]
                        v2 = self.vertices[i]
                        edge = Edge(v1, v2, weight)
                        self.addEdge(edge)
                        v1.addEdge(edge)
                        v2.addEdge(edge)

    def addEdge(self, edge):
        self.edges.append(edge)

    def addVertex(self, vertex):
        self.vertices.append(vertex)
