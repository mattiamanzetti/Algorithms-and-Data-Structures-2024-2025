from Graphs import Graph, Vertex
from LinearStructures import Stack


def topological_sorting(graph):
    st = Stack()
    for aVertex in graph:
        if aVertex.getColor() == 'white':
            dfsvisit(graph, aVertex, st)
    return st


def dfsvisit(graph, startVertex, st):
    startVertex.setColor('gray')
    graph.time += 1
    startVertex.setDiscovery(graph.time)
    for nextVertex in startVertex.getConnections():
        if nextVertex.getColor() == 'white':
            nextVertex.setPred(startVertex)
            dfsvisit(graph, nextVertex, st)
    startVertex.setColor('black')
    graph.time += 1
    st.enqueue(startVertex)
    startVertex.setFinish(graph.time)


# Test code
if __name__ == "__main__":

    myGraph = Graph()
    myGraph.addVertex("CupMilk")
    myGraph.addVertex("HeatGriddle")
    myGraph.addVertex("Egg")
    myGraph.addVertex("CupMix")
    myGraph.addVertex("PourCup")
    myGraph.addVertex("Oil")
    myGraph.addVertex("Turn")
    myGraph.addVertex("HeatSyrup")
    myGraph.addVertex("Eat")

    myGraph.addEdge("CupMilk", "CupMix")
    myGraph.addEdge("Egg", "CupMix")
    myGraph.addEdge("Oil", "CupMix")
    myGraph.addEdge("CupMix", "PourCup")
    myGraph.addEdge("CupMix", "HeatSyrup")
    myGraph.addEdge("HeatGriddle", "PourCup")
    myGraph.addEdge("PourCup", "Turn")
    myGraph.addEdge("Turn", "Eat")
    myGraph.addEdge("HeatSyrup", "Eat")

    # for vert in myGraph:
    #     print(vert)

    st = topological_sorting(myGraph)

    while not st.isEmpty():
        vert = st.pop()
        print(vert.getId(), vert.getDiscovery(), vert.getFinish())


