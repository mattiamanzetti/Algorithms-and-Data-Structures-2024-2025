# Check if a binary tree is complete or not
#
# E.g.:
#               A              TRUE
#            /     \
#          B        C
#        /   \     /  \
#       D    E    F    G
#     /  \
#    H    I
#
#               A              FALSE
#            /     \
#          B        C
#        /   \       \
#       D    E        G
#
#
#               A              FALSE
#            /     \
#          B        C
#        /   \
#       D    E
#     /  \
#    H    I
#
#               A              FALSE
#            /     \
#          B        C
#        /   \
#       D    E
#          /
#         I
#
#               A              TRUE
#            /     \
#          B        C
#        /   \     /
#       D    E    F
#
# 
# https://youtu.be/olbiZ-EOSig?si=YesmfyhLCYxfr-MG

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from LinearStructures import Queue, Stack

class Node:
    # WARNING: DO NOT MODIFY THIS INITIALIZATION METHOD!
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

######### ITERATIVE SOLUTION #########

def verifyCompleteIterative(root):
    """
    Iterative solution
    """
    if root is None:
        return True
    q = Queue()
    q.enqueue(root)
    test = False # test becomes true when we encounter a Null child
    while q.size() > 0:
        current_node = q.dequeue()
        if current_node is None:
            test = True
        else:
            if test:
                return False
            else:
                q.enqueue(current_node.leftChild)
                q.enqueue(current_node.rightChild)
    return True

def verifyCompleteIterative1(root):
    """
    Alternative (longer) iterative solution
    """
    if root is None:
        return True
    q = Queue()
    q.enqueue(root)
    test = False # The variable becomes true when we encounter a Null child
    while q.size() > 0:
        current_node = q.dequeue()

        if current_node.leftChild is not None:
            if test:
                return False # If we have already encountered a Null child and current_node.leftChild is not Null, then the tree is not complete
            else:
                q.enqueue(current_node.leftChild)
        else: 
            test = True # We encountered the first Null child

        if current_node.rightChild is not None:
            if test:
                return False # If we have already encountered a Null child and current_node.rightChild is not Null, then the tree is not complete
            else:
                q.enqueue(current_node.rightChild)
        else: 
            test = True # We encountered the first Null child

    return True

######### RECURSIVE SOLUTION #########

def verifyCompleteRecursive(root):
    """
    Recursive solution
    """
    total_nodes = countNodes(root)
    return auxVerifyCompleteRecursive(root, 1, total_nodes)

def countNodes(root):
    """ 
    Auxiliary function for the recursive solution 
    """
    if root is None:
        return 0
    return 1 + countNodes(root.leftChild) + countNodes(root.rightChild)

def auxVerifyCompleteRecursive(node, index, total_nodes):
    """
    Auxiliary function for the recursive solution
    """
    if node is None:
        return True
    if index > total_nodes:
        return False
    return (auxVerifyCompleteRecursive(node.leftChild, 2 * index, total_nodes) and auxVerifyCompleteRecursive(node.rightChild, 2 * index + 1, total_nodes))

# Test code
if __name__ == '__main__':

    # WARNING: DO NOT MODIFY THE TREE STRUCTURE!
    root1 = Node("A")
    root1.leftChild = Node("B")
    root1.leftChild.leftChild = Node("D")
    root1.leftChild.leftChild.leftChild = Node("H")
    root1.leftChild.leftChild.rightChild = Node("I")
    root1.leftChild.rightChild = Node("E")
    root1.rightChild = Node("C")
    root1.rightChild.leftChild = Node("F")
    root1.rightChild.rightChild = Node("G")

    # WARNING: DO NOT MODIFY THE TREE STRUCTURE!
    root2 = Node("A")
    root2.leftChild = Node("B")
    root2.leftChild.leftChild = Node("D")
    root2.leftChild.rightChild = Node("E")
    root2.rightChild = Node("C")
    root2.rightChild.rightChild = Node("G")

    # WARNING: DO NOT MODIFY THE TREE STRUCTURE!
    root3 = Node("A")
    root3.leftChild = Node("B")
    root3.leftChild.leftChild = Node("D")
    root3.leftChild.leftChild.leftChild = Node("H")
    root3.leftChild.leftChild.rightChild = Node("I")
    root3.leftChild.rightChild = Node("E")
    root3.rightChild = Node("C")

    # WARNING: DO NOT MODIFY THE TREE STRUCTURE!
    root4 = Node("A")
    root4.leftChild = Node("B")
    root4.leftChild.leftChild = Node("D")
    root4.leftChild.rightChild = Node("E")
    root4.leftChild.rightChild.leftChild = Node("I")
    root4.rightChild = Node("C")

    # WARNING: DO NOT MODIFY THE TREE STRUCTURE!
    root5 = Node("A")
    root5.leftChild = Node("B")
    root5.leftChild.leftChild = Node("D")
    root5.leftChild.rightChild = Node("E")
    root5.rightChild = Node("C")
    root5.rightChild.leftChild = Node("F")


    # Expected result TRUE
    print("Iterative solution:", verifyCompleteIterative(root1))
    print("Alternative iterative solution:", verifyCompleteIterative1(root1))
    print("Recursive solution:", verifyCompleteRecursive(root1))
    print()

    # Expected result FALSE
    print("Iterative solution:", verifyCompleteIterative(root2))
    print("Alternative iterative solution:", verifyCompleteIterative1(root2))
    print("Recursive solution:", verifyCompleteRecursive(root2))
    print()

    # Expected result FALSE
    print("Iterative solution:", verifyCompleteIterative(root3))
    print("Alternative iterative solution:", verifyCompleteIterative1(root3))
    print("Recursive solution:", verifyCompleteRecursive(root3))
    print()

    # Expected result FALSE
    print("Iterative solution:", verifyCompleteIterative(root4))
    print("Alternative iterative solution:", verifyCompleteIterative1(root4))
    print("Recursive solution:", verifyCompleteRecursive(root4))
    print()

    # Expected result TRUE
    print("Iterative solution:", verifyCompleteIterative(root5))
    print("Alternative iterative solution:", verifyCompleteIterative1(root5))
    print("Recursive solution:", verifyCompleteRecursive(root5))

