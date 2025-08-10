# Example of binary tree with some custom methods to add nodes

class Node:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, key):
        if self.leftChild is None:
            self.leftChild = Node(key)
        else:
            t = Node(key)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, key):
        if self.rightChild is None:
            self.rightChild = Node(key)
        else:
            t = Node(key)
            t.rightChild = self.rightChild
            self.rightChild = t

        return self.key


if __name__ == "__main__":
    root = Node("A")
    root.insertLeft("B")
    root.leftChild.insertLeft("D")
    root.leftChild.insertRight("E")
    root.insertRight("C")
    root.rightChild.insertLeft("F")




