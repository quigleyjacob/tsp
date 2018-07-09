import os, sys
from tsp import TSP

if len(sys.argv) < 2:
    sys.exit(f"You didn't include a filename. Use the format 'python3 brute_force.py <filename>'")

filename = sys.argv[1]

if not os.path.exists(filename):
    sys.exit(f"Error: File '{sys.argv[1]}' not found")

class BruteForce:
    def __init__(self, filename):
        self.paths = []
        self.tsp = TSP(filename)


    def calculateTSP(self):
        for v in self.tsp.vertices:
            self.pathHelper([v], self.tsp.vertices)

    def pathHelper(self, path, vertices):
        last = len(path)-1;
        if(len(path) == len(path[0].edgesFrom)+1):
            self.paths.append(path)
            return path
        else:
            for e in path[last].edgesFrom:
                if e.v2 not in path:
                    newPath = list(path)
                    newPath.append(e.v2)
                    self.pathHelper(newPath, vertices)

    def shortestPath(self):
        min = 1000000
        route = []
        for p in self.paths:
            path = 0
            i = 0
            while i < len(p):
                vertex = p[i]
                if i == len(p)-1:
                    firstId = p[0].id
                    for e in vertex.edgesFrom:
                        if e.v2.id == firstId:
                            path += e.weight
                else:
                    nextId = p[i+1].id
                    for e in vertex.edgesFrom:
                        if e.v2.id == nextId:
                            path += e.weight
                i+=1
            if min > path:
                min = path
                route = list(p)
        # print(route)
        for r in route:
            print(r.toShortString(), end=" ")
        print()
        return min



bf = BruteForce(filename)
bf.calculateTSP()
shortest = bf.shortestPath()

print(shortest)
