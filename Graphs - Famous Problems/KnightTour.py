from Graphs import Graph


# Create the graph of the possible knight moves
# in a chessboard of the given size
def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph


# Get the number of a cell given its coordinate in the chessboard
def posToNodeId(row, column, board_size):
    return (row * board_size) + column


# Get all the possible legal move from a given position
def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append((newX, newY))
    return newMoves


# Check if a position is inside the chessboard or not
def legalCoord(x, bdSize):
    if 0 <= x < bdSize:
        return True
    else:
        return False


# Optimize the order in which we visit the connections
# using an heuristic called Warnsdorff’s algorithm
def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c,v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]


# Compute the knight tour
def knightTour(path, currentNode, limit):
    currentNode.setColor('gray')
    path.append(currentNode.getId())
    depth = len(path)
    if depth < limit:
        # nbrList = list(currentNode.getConnections())
        nbrList = list(orderByAvail(currentNode))  # apply an heuristic to speed up the process
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(path, nbrList[i], limit)
            i = i + 1
        if not done:  # prepare to backtrack
            path.pop()
            currentNode.setColor('white')
    else:
        done = True
    return done


if __name__ == "__main__":
    size = 8
    kGraph = knightGraph(size)
    solution = []
    limit = size*size
    knightTour(solution, kGraph.getVertex(0), limit)
    print("The tour is:", solution)
