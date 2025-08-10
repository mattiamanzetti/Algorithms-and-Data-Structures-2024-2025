import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Graphs import Graph, Vertex
from LinearStructures import Queue


def buildGraph(wordFile):
    d = {}  # dictionary will contain ‘buckets’ of words
    newgraph = Graph()
    wfile = open(wordFile, 'r')

    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    newgraph.addEdge(word1, word2)
    return newgraph


def bfs(g, start_vert_key):
    startVert = g.getVertex(start_vert_key)
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


def traverse(g, vert_name):
    currentVertex = g.getVertex(vert_name)
    while currentVertex.getPred():
        print(currentVertex.getId() + " - Distance: ", currentVertex.getDistance())
        currentVertex = currentVertex.getPred()
    print(currentVertex.getId() + " - Distance: ", currentVertex.getDistance())


if __name__ == "__main__":
    g = buildGraph("words.txt")

    bfs(g, "fool")
    traverse(g, 'sage')


