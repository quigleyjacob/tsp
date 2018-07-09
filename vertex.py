from edge import Edge
class Vertex:
    def __init__(self, id):
        self.id = id
        self.edgesTo = []
        self.edgesFrom = []

    def addEdgeTo(self, edge):
        self.edgesTo.append(edge)

    def addEdgeFrom(self, edge):
        self.edgesFrom.append(edge)

    def toString(self):
        list = "Id: " + str(self.id) + "    Edges To: "
        for e in self.edgesTo:
            list += e.toString() + " "
        list += " Edges From: "
        for e in self.edgesFrom:
            list += e.toString() + " "
        return list

    def toShortString(self):
        return "Id: " + str(self.id) + " "

    def __eq__(self, v):
        return self.id is v.id
