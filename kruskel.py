from edge import Edge
from vertex import Vertex
from heap_sort import HeapSort

class Kruskel:
    def __init__(self, heap, tsp):
        self.heap = heap
        self.edgesInTree = []
        self.verticesInTree = []
        self.tsp = tsp

    def verticesAreConnected(self, v1, v2):
        if(len(self.verticesInTree) == 0):
            return True
        return not all(x in self.verticesInTree for x in [v1, v2])

    def run(self):
        while self.heap.size > 0:
            min = self.heap.removeMin()
            if self.verticesAreConnected(min.v1, min.v2):
                self.edgesInTree.append(min)
                v1 = Vertex(min.v1.id)
                v2 = Vertex(min.v2.id)
                v1.addEdgeTo(min)
                v2.addEdgeTo(min)
                self.verticesInTree.append(v1)
                self.verticesInTree.append(v2)
        return self.edgesInTree

    def toString(self):
        for v in self.verticesInTree:
            print(v.toString())
        for e in self.edgesInTree:
            print(e.toString())
