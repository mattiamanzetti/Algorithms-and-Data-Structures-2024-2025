# Verify if an undirected graph is a tree
#
# An undirected graph is a tree if the following conditions are verified:
# - There are no cycles
# - The graph is connected
#
# HINTS: You can use DFS to perform both the verifications!

from Graphs import Graph


# Return True if the graph is a tree, False otherwise
def isTree(graph):

    # Reset all vertices to white
    for aVertex in graph:
        aVertex.setColor('white')
        aVertex.setPred(-1)

    # Get the first vertex of the graph as starting point
    keys = list(graph.getVertices())
    aVertex = graph.getVertex(keys[0])

    # Cycle verification

    # TODO...

    # Disconnection verification

    # TODO...

    return True


# STANDARD IMPLEMENTATION OF A DFS VISIT (TO MODIFY)
# NOTE: Discovery and Finish time are not needed
def dfsvisit(graph, startVertex):
    startVertex.setColor('gray')

    # graph.time += 1
    # startVertex.setDiscovery(graph.time)

    for nextVertex in startVertex.getConnections():
        if nextVertex.getColor() == 'white':
            nextVertex.setPred(startVertex)
            dfsvisit(graph, nextVertex)
    startVertex.setColor('black')

    # graph.time += 1
    # startVertex.setFinish(graph.time)


# Test code
if __name__ == "__main__":

    # WARNING: DO NOT MODIFY THE GRAPH STRUCTURE!
    g1 = Graph(True)

    g1.addEdge("v0", "v1")
    g1.addEdge("v1", "v2")
    g1.addEdge("v1", "v3")
    g1.addEdge("v3", "v4")
    g1.addEdge("v2", "v0")  # this line creates a cycle

    # WARNING: DO NOT MODIFY THE GRAPH STRUCTURE!
    g2 = Graph(True)

    g2.addEdge("v0", "v1")
    g2.addEdge("v1", "v2")
    g2.addEdge("v1", "v3")
    g2.addEdge("v3", "v4")
    g2.addEdge("v5", "v6")  # this line creates a disconnected graph

    # WARNING: DO NOT MODIFY THE GRAPH STRUCTURE!
    g3 = Graph(True)

    g3.addEdge("v0", "v1")
    g3.addEdge("v1", "v2")
    g3.addEdge("v1", "v3")
    g3.addEdge("v3", "v4")
    g3.addEdge("v5", "v4")

    # Expected result = FALSE
    print(isTree(g1))

    # Expected result = FALSE
    print(isTree(g2))

    # Expected result = TRUE
    print(isTree(g3))
