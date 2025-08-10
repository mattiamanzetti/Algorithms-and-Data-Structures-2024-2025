# Implementation of Dijkstra's Algorithm

from Graphs import Graph, PriorityQueue
import sys


# Dijkstra's algorithm from a start vertex to all the other ones
def _dijkstra(aGraph, start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in aGraph])

    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert, newDist)


# Dijkstra's algorithm from a start vertex to a destination vertex
def _dijkstra_se(aGraph, start, end):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in aGraph])

    end_reached = False
    while not pq.isEmpty():
        currentVert = pq.delMin()

        if currentVert is end and currentVert.getDistance() < sys.maxsize:
            end_reached = True
            break

        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert, newDist)

    if end_reached:
        printPath(start, end)
    else:
        print("Node", end.getId(), "is not reachable")


# Auxiliary method to print the path from the source vertex to the destination vertex
def printPath(source, dest):
    path = []

    print("Vertex", dest.getId(), "is at distance", dest.getDistance(), "from the source vertex", source.getId())
    # get the path
    currentVertex = dest
    while currentVertex.getPred():
        path.insert(0, currentVertex.getId())
        currentVertex = currentVertex.getPred()
    print("\tPath", source.getId(), *path)


# Auxiliary method to print all the paths from the source
def printPaths(graph, source):
    path = []
    source_id = source.getId()
    for vert in graph:
        if vert.getId() != source_id:
            print("Vertex", vert.getId(), "is at distance", vert.getDistance(), "from the source vertex", source_id)
            # get the path
            path.clear()
            currentVertex = vert
            while currentVertex.getPred():
                path.insert(0, currentVertex.getId())
                currentVertex = currentVertex.getPred()
            print("\tPath:", source_id, *path)


# Method to be called, it will run the correct auxiliary method if the end node if specified or not
def dijkstra(aGraph, start, end=-1):
    if start is None:
        print("Starting node does not exist")
        return

    if end is None:
        print("Destination node does not exist")
        return

    # Reset the nodes
    for aVertex in aGraph:
        aVertex.setColor('white')
        aVertex.setDistance(sys.maxsize)
        aVertex.setPred(None)

    if end != -1:  # end vertex specified, call the specific method
        _dijkstra_se(aGraph, start, end)

    else:  # end vertex not specified, call the general method
        _dijkstra(aGraph, start)


# Test code
if __name__ == "__main__":
    myGraph = Graph(undirect=True)
    # myGraph.addEdge("u", "v", 2)
    # myGraph.addEdge("u", "w", 5)
    # myGraph.addEdge("u", "x", 1)
    # myGraph.addEdge("v", "w", 3)
    # myGraph.addEdge("v", "x", 2)
    # myGraph.addEdge("x", "y", 1)
    # myGraph.addEdge("x", "w", 3)
    # myGraph.addEdge("y", "w", 1)
    # myGraph.addEdge("z", "y", 1)
    # myGraph.addEdge("w", "z", 5)

    myGraph.addEdge("A", "B", 2)
    myGraph.addEdge("A", "D", 2)
    myGraph.addEdge("B", "E", 5)
    myGraph.addEdge("B", "C", 4)
    myGraph.addEdge("B", "D", 1)
    myGraph.addEdge("E", "F", 3)
    myGraph.addEdge("E", "G", 2)
    myGraph.addEdge("G", "F", 9)
    myGraph.addEdge("C", "F", 6)
    myGraph.addEdge("G", "I", 3)
    myGraph.addEdge("C", "H", 10)
    myGraph.addEdge("I", "H", 3)

    source_vert = myGraph.getVertex("A")

    # Compute Dijkstra's algorithm from the source to all the nodes
    dijkstra(myGraph, source_vert)
    printPaths(myGraph, source_vert)

    # Uncomment these lines to get the path from source to a destination
    # dest_vert = myGraph.getVertex("G")
    # dijkstra(myGraph, source_vert, dest_vert)


