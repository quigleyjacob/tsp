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
        if (self.size > 1):
            self.__decrease(self.size)

    def __decrease(self, size):
        if (size > 1):
            child = self.nodes[size]
            parent = self.nodes[size // 2]
            if (child.weight < parent.weight ):
                self.nodes[size // 2], self.nodes[size] = child, parent
                self.__decrease(size // 2)


    def removeMin(self):
        ans = self.nodes[1]
        last = self.nodes[-1]
        self.nodes[1] = last
        self.nodes[-1] = None
        self.size -= 1
        if self.size > 1:
            self.__heapify(1)

    def __heapify(self, i):
        print("Not created yet")
