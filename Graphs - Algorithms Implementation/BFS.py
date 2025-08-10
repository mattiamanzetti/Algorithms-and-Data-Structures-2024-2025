import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Graphs import Graph, Vertex
from LinearStructures import Queue


def bfs(graph, start_vert_key):
    startVert = graph.getVertex(start_vert_key)
    startVert.setDistance(0)
    startVert.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(startVert)
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == 'white':
                nbr.setColor('gray')
                nbr.setPred(currentVert)
                nbr.setDistance(currentVert.getDistance() + 1)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')


def traverse(graph, vert_name):
    currentVertex = graph.getVertex(vert_name)
    while currentVertex.getPred():
        print(currentVertex.getId() + " - Distance: ", currentVertex.getDistance())
        currentVertex = currentVertex.getPred()
    print(currentVertex.getId() + " - Distance: ", currentVertex.getDistance(), "\n")


# Test code
if __name__ == "__main__":

    myGraph = Graph(True)  # Create an indirect graph
    myGraph.addEdge("r", "s")
    myGraph.addEdge("r", "v")
    myGraph.addEdge("w", "s")
    myGraph.addEdge("w", "t")
    myGraph.addEdge("w", "x")
    myGraph.addEdge("t", "x")
    myGraph.addEdge("t", "u")
    myGraph.addEdge("u", "x")
    myGraph.addEdge("u", "y")
    myGraph.addEdge("x", "y")

    # for vert in myGraph:
    #     print(vert)

    bfs(myGraph, "s")

    for vert in myGraph:
        print("Path from s to", vert.getId())
        traverse(myGraph, vert.getId())

    myGraph2 = Graph(True)  # Create an indirect graph
    myGraph2.addEdge("A", "B")
    myGraph2.addEdge("B", "C")
    myGraph2.addEdge("C", "D")
    myGraph2.addEdge("B", "E")
    myGraph2.addEdge("D", "F")
    myGraph2.addEdge("E", "G")
    myGraph2.addEdge("F", "H")
    myGraph2.addEdge("G", "H")

    # for vert in myGraph2:
    #     print(vert)

    bfs(myGraph2, "E")

    for vert in myGraph2:
        print("Path from E to", vert.getId())
        traverse(myGraph2, vert.getId())


