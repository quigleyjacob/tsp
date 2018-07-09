from edge import Edge
from vertex import Vertex
from heap_sort import HeapSort

class Kruskel:
    def __init__(self, heap):
        self.heap = heap
        self.tree = []

    def vertexInTree(self, v):
        for e in self.tree:
            if e.v1.__eq__(v) or e.v2.__eq__(v):
                return True
        return False

    def run(self):
        while self.heap.size > 0:
            min = self.heap.removeMin()
        # print(min.toString())
        # print(min.v1.__eq__(min.v2))
            if not self.vertexInTree(min.v1) or not self.vertexInTree(min.v2):
            # if self.vertexInTree(min.v1) is not self.vertexInTree(min.v2):
                self.tree.append(min)
            # print(not self.vertexInTree(min.v1) or not self.vertexInTree(min.v2))
        # print(self.vertexInTree(min.v1))
        # print(min.v2.toString())
        return self.tree

    def toString(self):
        for e in self.tree:
            print(e.toString())
