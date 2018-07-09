import os, sys
from tsp import TSP
from heap_sort import HeapSort
from kruskel import Kruskel
from vertex import Vertex

if len(sys.argv) < 2:
    sys.exit(f"You didn't include a filename. Use the format 'python3 my_imp.py <filename>'")

filename = sys.argv[1]

if not os.path.exists(filename):
    sys.exit(f"Error: File '{sys.argv[1]}' not found")

class MyImp:
    def __init__(self, filename):
        self.paths = []
        self.tsp = TSP(filename)
        # self.start = tsp.vertices[0]

myImp = MyImp(filename)

heapSort = HeapSort()

for i in myImp.tsp.edges:
    heapSort.addToTree(i)


kruskel = Kruskel(heapSort)

kruskel.run()
kruskel.toString()

# for i in heapSort.nodes:
#     if i is not None:
#         print(i.toString())

# while(heapSort.size > 0):
#     min = heapSort.removeMin()
#     print(min.weight)
# print(heapSort.size)
