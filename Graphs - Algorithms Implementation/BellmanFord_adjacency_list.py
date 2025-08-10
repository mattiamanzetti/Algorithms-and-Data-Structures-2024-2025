# Bellman Ford Algorithm in Python

from Graphs import Graph
import sys


def bellman_ford(graph, src):

    # Step 1: reset the vertex
    for aVertex in graph:
        aVertex.setDistance(sys.maxsize)
        aVertex.setPred(None)

    # Set distance 0 for the source vertex
    src.setDistance(0)

    # Step 2: Relax the edges
    for _ in range(graph.numVertices - 1):
        for vert in graph:
            for neighbour in vert.getConnections():
                newDist = vert.getDistance() + vert.getWeight(neighbour)
                if newDist < neighbour.getDistance():
                    neighbour.setDistance(newDist)
                    neighbour.setPred(vert)

    # Step 3: Check for negative weight cycles
    for vert in graph:
        for neighbour in vert.getConnections():
            if neighbour.getDistance() > vert.getDistance() + vert.getWeight(neighbour):
                print("Negative cycle detected!")
                return False

    # Solution found
    return True


# Auxiliary method to print all the paths from the source
def printPaths(graph, source):
    path = []
    source_id = source.getId()
    for vert in graph:
        if vert.getId() != source_id:
            if vert.getDistance() != sys.maxsize:
                print("Vertex", vert.getId(), "is at distance", vert.getDistance(), "from the source vertex", source_id)
            else:
                print("Vertex", vert.getId(), "is not reachable from the source vertex", source_id)
            # get the path
            path.clear()
            currentVertex = vert
            while currentVertex.getPred():
                path.insert(0, currentVertex.getId())
                currentVertex = currentVertex.getPred()
            print("\tPath:", source_id, *path)


# Test code
if __name__ == "__main__":

    myGraph = Graph()
    myGraph.addEdge("A", "B", 6)
    myGraph.addEdge("A", "C", 7)
    myGraph.addEdge("B", "C", 8)
    myGraph.addEdge("C", "D", -3)
    myGraph.addEdge("D", "B", -2)
    myGraph.addEdge("B", "E", -4)
    myGraph.addEdge("C", "E", 9)
    myGraph.addEdge("E", "D", 7)

    source_vert = myGraph.getVertex("A")
    if bellman_ford(myGraph, source_vert):
        printPaths(myGraph, source_vert)