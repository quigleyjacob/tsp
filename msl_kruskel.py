from edge import Edge
from vertex import Vertex
from heap_sort import HeapSort

class MSLKruskel:
    def __init__(self, heap, tsp):
        self.heap = heap
        self.edgesInTree = []
        self.verticesInTree = []
        self.tsp = tsp
        self.nodes = [0]*len(tsp.vertices)

    def verticesAreConnected(self, v1, v2):
        if(len(self.verticesInTree) == 0):
            return True
        # print(len(self.verticesInTree))
        # for v in self.verticesInTree:
        #     print(v.toString())
        # print(" ")
        # connected = []
        # tempV = [x for x in self.edgesInTree if x.edgesFrom.]
        # queue = []
        # if(len(tempV)):
        #     print(v1.toString())
        #     for e in tempV:
        #         print(e.toString())
        #     print(" ")
        return not all(x in self.verticesInTree for x in [v1, v2])

    def run(self):
        while self.heap.size > 0:
            min = self.heap.removeMin()
            # checks if the vertices of the removed edge have already been put into the tree
            try1 = [x for x in self.verticesInTree if x.id is min.v1.id]
            try2 = [x for x in self.verticesInTree if x.id is min.v2.id]
            v1 = Vertex(min.v1.id) if len(try1) is 0 else try1[0]
            v2 = Vertex(min.v2.id) if len(try2) is 0 else try2[0]
            edge = Edge(v1, v2, min.weight)
            edge2 = Edge(v2, v1, min.weight)
            # check to see if the two vertices are connected in the graph
            # if they are, then we do not add this edge
            if self.verticesAreConnected(v1, v2) and self.nodes[v1.id] < 2 and self.nodes[v2.id] < 2:
                self.edgesInTree.append(edge)
                self.edgesInTree.append(edge2)
                v1.addEdgeFrom(edge)
                v1.addEdgeTo(edge2)
                v2.addEdgeFrom(edge2)
                v2.addEdgeTo(edge)
                if len(try1) is 0:
                    self.verticesInTree.append(v1)
                if len(try2) is 0:
                    self.verticesInTree.append(v2)
                self.nodes[v1.id] += 1
                self.nodes[v2.id] += 1
        return self.edgesInTree

    def toString(self):
        for v in self.verticesInTree:
            print(v.toString())
        for e in self.edgesInTree:
            print(e.toString())
