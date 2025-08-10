# Find the Strongly Connected Component of a directed graph using Kosaraju's algorithm:
#
# - Perform DFS traversal of the graph. Push node to stack as soon as becomes black
# - Create the transpose graph by reversing the edges
# - Pop nodes one by one from the stack and again to DFS on the modified graph
# - Print the connected components


from Graphs import Graph
from LinearStructures import Stack

# Method for creating the transposed graph
#
# TODO
#


# DFS Visit
# STANDARD IMPLEMENTATION TO BE MODIFIED
def dfsvisit(graph, startVertex):
    startVertex.setColor('gray')
    graph.time += 1
    startVertex.setDiscovery(graph.time)
    for nextVertex in startVertex.getConnections():
        if nextVertex.getColor() == 'white':
            nextVertex.setPred(startVertex)
            dfsvisit(graph, nextVertex)
    startVertex.setColor('black')
    graph.time += 1
    startVertex.setFinish(graph.time)


# First DFS, fill the stack in inverted finishing order
# STANDARD IMPLEMENTATION TO BE MODIFIED
def dfs1(graph):
    for aVertex in graph:
        if aVertex.getColor() == 'white':
            dfsvisit(graph, aVertex)


# Create the transposed graph
# DRAFT TO BE COMPLETED
def getTranspose(graph):
    gt = Graph()

    # TODO

    return gt


# Second DFS, find and print the SCC
# STANDARD IMPLEMENTATION TO BE MODIFIED
def dfs2(graph):
    for aVertex in graph:
        if aVertex.getColor() == 'white':
            dfsvisit(graph, aVertex)


# Method that executes the Kosaraju's algorithm
# TO BE COMPLETED
def getSCC(graph):

    st = Stack()

    # Call to the first DFS
    #
    # TODO
    #

    # Call to transpose method
    #
    # TODO
    #

    # Call to the second DFS
    #
    # TODO
    #


# Test code
if __name__ == "__main__":
    myGraph = Graph()
    myGraph.addEdge("A", "B")
    myGraph.addEdge("B", "C")
    myGraph.addEdge("D", "B")
    myGraph.addEdge("C", "C")
    myGraph.addEdge("B", "E")
    myGraph.addEdge("C", "F")
    myGraph.addEdge("D", "G")
    myGraph.addEdge("E", "A")
    myGraph.addEdge("E", "D")
    myGraph.addEdge("F", "H")
    myGraph.addEdge("G", "E")
    myGraph.addEdge("H", "I")
    myGraph.addEdge("I", "F")

    # Expected result:
    # SCC 1: A E G B D
    # SCC 2: C
    # SCC 3: F I H
    getSCC(myGraph)
