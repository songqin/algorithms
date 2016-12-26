
V=3
g = [[0 for _ in range(V)] for _ in range(V)]
print g


# print [1 for a in range(3)]
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

dgn = DirectedGraphNode(1)
print dgn.label
print dgn.neighbors