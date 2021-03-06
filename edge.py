class Edge:
    def __init__(self, v1, v2, weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

    def getWeight(self):
        return self.weight

    def toString(self):
        return "(Vertices: " + str(self.v1.id) + "," + str(self.v2.id) + " Weight: " + str(self.weight) + ")"
