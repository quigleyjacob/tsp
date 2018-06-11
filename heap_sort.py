from edge import Edge

class HeapSort:
    def __init__(self):
        self.nodes = []
        self.size = 0;
        self.nodes.append(None)

    def printNodes(self):
        for n in self.nodes:
            print(n.toString())

    def addToTree(self, node):
        self.size += 1
        self.nodes.append(node)
        if self.size > 1:
            self.__decrease(self.size)

    def __decrease(self, size):
        if size > 1:
            child = self.nodes[size]
            parent = self.nodes[size // 2]
            if child.weight < parent.weight:
                self.nodes[size // 2], self.nodes[size] = child, parent
                self.__decrease(size // 2)


    def removeMin(self):
        ans = self.nodes[1]
        last = self.nodes[-1]
        self.nodes[1] = last
        self.nodes = self.nodes[:-1]
        self.size -= 1
        if self.size > 1:
            self.__heapify(1)
        return ans

    def __heapify(self, i):
        if i < (self.size // 2 + 1):
            parent = self.nodes[i]
            child1 = self.nodes[i*2]
            child2 = 0
            if i*2+1 <= len(self.nodes):
                child2 = self.nodes[i*2 + 1] if i*2+1 < len(self.nodes) else Edge(None, None, 100000)
            switch = child1 if child1.weight < child2.weight else child2
            next = i*2 if child1.weight < child2.weight else i*2 + 1
            if (parent.weight > switch.weight):
                self.nodes[i], self.nodes[next] = switch, parent

            self.__heapify(next)
