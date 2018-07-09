from edge import Edge
class Vertex:
    def __init__(self, id):
        self.id = id
        self.edges = []

    def addEdge(self, edge):
        self.edges.append(edge)

    def toString(self):
        list = "Id: " + str(self.id) + "    Edges: "
        for e in self.edges:
            list += e.toString() + " "
        return list

    def toShortString(self):
        return "Id: " + str(self.id) + " "

    def __eq__(self, v):
        return self.id is v.id
