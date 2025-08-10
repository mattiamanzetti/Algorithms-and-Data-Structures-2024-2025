# Implementation of Level Order Traversal

from LinearStructures import Queue, Stack


# Basic binary tree
class Node:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None


# Level order or BFS traversal
def levelOrder(root):

    # Base Case
    if root is None:
        return

    # Create an empty queue
    # for level order traversal
    q = Queue()

    # Enqueue Root and initialize height
    q.enqueue(root)

    while q.size() > 0:

        # Print front of queue and
        # remove it from queue
        currentNode = q.dequeue()
        print(currentNode.key)

        # Enqueue left child
        if currentNode.leftChild is not None:
            q.enqueue(currentNode.leftChild)

        # Enqueue right child
        if currentNode.rightChild is not None:
            q.enqueue(currentNode.rightChild)


# Test code
if __name__ == "__main__":
    r = Node('Book')
    r.leftChild = Node('Chapter 1')
    r.leftChild.leftChild = Node('Section 1.1')
    r.leftChild.rightChild = Node('Section 1.2')
    r.leftChild.rightChild.leftChild = Node('Section 1.2.1')
    r.leftChild.rightChild.rightChild = Node('Section 1.2.2')
    r.rightChild = Node('Chapter 2')
    r.rightChild.leftChild = Node('Section 2.1')
    r.rightChild.rightChild = Node('Section 2.2')
    r.rightChild.rightChild.leftChild = Node('Section 2.2.1')
    r.rightChild.rightChild.rightChild = Node('Section 2.2.2')

    print('\nLEVEL ORDER')
    levelOrder(r)