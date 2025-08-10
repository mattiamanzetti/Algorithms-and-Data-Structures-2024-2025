# Given a BST and a number N, return the node key in the BST that is closest to N,
# i.e. the node key with the minimum absolute difference with B.
#
# E.g.
# Given the following BST and N=7 the closest node is 5, since |7-5| = 2 is the minimum difference
#
#             15
#         /       \
#       10        20
#      /  \     /   \
#    5    12   19   25
#

# WARNING: DO NOT MODIFY


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from LinearStructures import Queue

# BST Node
class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None


# Basic BST implementation
class BST:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._addNode(self.root, val)

    def _addNode(self, node, val):
        if val < node.key:
            if node.left is None:
                node.left = Node(val)
            else:
                self._addNode(node.left,val)

        if val > node.key:
            if node.right is None:
                node.right = Node(val)
            else:
                self._addNode(node.right, val)

# END DO NOT MODIFY

""" 
def getClosestValue(root, val):
    if root.key == val:
        return val
    
    else:
        # closest = root.key
        # print(_getClosestValue(root, val, closest))
        _getClosestValue(root, val)

def _getClosestValue(node, val):
    if node is None:
        distance = float('+inf')
    
    else:
        distance = abs(node.key - val)

    
    return # the node's key
"""


def getClosestValue(root, val):
    if root is None:
        return None
    
    q = Queue()
    q.enqueue(root)
    closest = root.key
    min_distance = abs(root.key - val)

    while q.size() > 0:
        current_node = q.dequeue()
        if abs(current_node.key - val) < min_distance:
            min_distance, closest = abs(current_node.key - val), current_node.key
        
        if current_node.left is not None:
            q.enqueue(current_node.left)
        
        if current_node.right is not None:
            q.enqueue(current_node.right)
    
    return closest


# Test Code
if __name__ == '__main__':

    # Sample BST
    bst1 = BST()
    bst1.add(15)
    bst1.add(10)
    bst1.add(20)
    bst1.add(5)
    bst1.add(12)
    bst1.add(19)
    bst1.add(25)

    # VALUES TO TEST

    N = 7  # expected result 5
    print(getClosestValue(bst1.root, N))

    N = 14  # expected result 15
    print(getClosestValue(bst1.root, N))

    N = 20  # expected result 20
    print(getClosestValue(bst1.root, N))

    N = 13  # expected result 12
    print(getClosestValue(bst1.root, N))

    N = 18  # expected result 19
    print(getClosestValue(bst1.root, N))
