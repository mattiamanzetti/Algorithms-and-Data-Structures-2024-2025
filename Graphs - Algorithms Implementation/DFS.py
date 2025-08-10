from Graphs import Graph, Vertex


def dfs(graph):
    # Reset the vertices
    for aVertex in graph:
        aVertex.setColor('white')
        aVertex.setPred(None)

    for aVertex in graph:
        if aVertex.getColor() == 'white':
            dfsvisit(graph, aVertex)


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



# Test code
if __name__ == "__main__":

    myGraph = Graph()
    myGraph.addEdge("A", "B")
    myGraph.addEdge("A", "D")
    myGraph.addEdge("B", "C")
    myGraph.addEdge("B", "D")
    myGraph.addEdge("D", "E")
    myGraph.addEdge("E", "B")
    myGraph.addEdge("E", "F")
    myGraph.addEdge("F", "C")
    # myGraph.addEdge("G", "F")
    # myGraph.addEdge("G", "H")
    # myGraph.addEdge("H", "I")
    # myGraph.addEdge("I", "G")

    for vert in myGraph:
        print(vert)

    dfs(myGraph)

    for vert in myGraph:
        print(vert.getId(), vert.getDiscovery(), vert.getFinish())

    # myGraph = Graph()
    # myGraph.addEdge("A", "B")
    # myGraph.addEdge("A", "D")
    # myGraph.addEdge("D", "B")
    # myGraph.addEdge("E", "B")
    # myGraph.addEdge("E", "F")
    # myGraph.addEdge("F", "C")
    # myGraph.addEdge("F", "G")
    # myGraph.addEdge("G", "E")
    # myGraph.addEdge("H", "C")
    # myGraph.addEdge("H", "I")
    # myGraph.addEdge("G", "I")

    # for vert in myGraph:
    #     print(vert)
    #
    # dfs(myGraph)
    #
    # for vert in myGraph:
    #     print(vert.getId(), vert.getDiscovery(), vert.getFinish())

    myGraph = Graph()
    myGraph.addEdge("A", "B")
    myGraph.addEdge("B", "C")
    myGraph.addEdge("D", "E")
    myGraph.addEdge("E", "A")
    myGraph.addEdge("F", "B")
    myGraph.addEdge("C", "G")
    myGraph.addEdge("F", "H")
    myGraph.addEdge("D", "H")
    myGraph.addEdge("F", "I")
    myGraph.addEdge("I", "E")
    myGraph.addEdge("I", "G")

    for vert in myGraph:
        print(vert)

    dfs(myGraph)

    for vert in myGraph:
        print(vert.getId(), vert.getDiscovery(), vert.getFinish())
