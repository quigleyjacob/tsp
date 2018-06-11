import os, sys
from tsp import TSP
from heap_sort import HeapSort

if len(sys.argv) < 2:
    sys.exit(f"You didn't include a filename. Use the format 'python3 my_imp.py <filename>'")

filename = sys.argv[1]

if not os.path.exists(filename):
    sys.exit(f"Error: File '{sys.argv[1]}' not found")

class MyImp:
    def __init__(self, filename):
        self.paths = []
        self.tsp = TSP(filename)

myImp = MyImp(filename)

heapSort = HeapSort()

for i in myImp.tsp.edges:
    heapSort.addToTree(i)

# for i in heapSort.nodes:
#     if i is not None:
#         print(i.toString())
print(heapSort.size)
heapSort.removeMin()
print(heapSort.size)
