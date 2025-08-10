# Basic implementation of a binary tree

class Node:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None


# Test code
if __name__ == '__main__':
    root = Node("A")
    root.leftChild = Node("B")
    root.leftChild.leftChild = Node("D")
    root.leftChild.rightChild = Node("E")
    root.rightChild = Node("C")
    root.rightChild.leftChild = Node("F")
