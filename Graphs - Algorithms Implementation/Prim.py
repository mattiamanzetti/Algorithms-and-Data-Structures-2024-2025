# Implementation of Prim's algorithm

from Graphs import PriorityQueue, Graph, Vertex
import sys


def prim(G, start):
    pq = PriorityQueue()
    start.setK(0)
    pq.buildHeap([(v.getK(), v) for v in G])

    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newCost = currentVert.getWeight(nextVert)
            if nextVert in pq and newCost < nextVert.getK():
                nextVert.setPred(currentVert)
                nextVert.setK(newCost)
                pq.decreaseKey(nextVert,newCost)


# Auxiliary method to print the edges of the MST
def printMST(graph):

    for vert in graph:
        pred = vert.getPred()
        if pred is not None:
            print(pred.getId(), "-", vert.getId())


# Test code
if __name__ == "__main__":
    myGraph = Graph(undirect=True)
    # myGraph.addEdge("A", "B", 2)
    # myGraph.addEdge("A", "C", 3)
    # myGraph.addEdge("B", "C", 1)
    # myGraph.addEdge("B", "D", 1)
    # myGraph.addEdge("D", "E", 1)
    # myGraph.addEdge("B", "E", 4)
    # myGraph.addEdge("E", "F", 1)
    # myGraph.addEdge("C", "F", 5)
    # myGraph.addEdge("F", "G", 1)

    myGraph.addEdge("A", "B", 2)
    myGraph.addEdge("A", "D", 2)
    myGraph.addEdge("B", "E", 4)
    myGraph.addEdge("B", "D", 1)
    myGraph.addEdge("E", "F", 5)
    myGraph.addEdge("E", "G", 1)
    myGraph.addEdge("G", "F", 9)
    myGraph.addEdge("C", "F", 6)
    myGraph.addEdge("G", "I", 3)
    myGraph.addEdge("C", "H", 2)
    myGraph.addEdge("I", "H", 3)

    source_vert = "A"
    prim(myGraph, myGraph.getVertex(source_vert))
    printMST(myGraph)
