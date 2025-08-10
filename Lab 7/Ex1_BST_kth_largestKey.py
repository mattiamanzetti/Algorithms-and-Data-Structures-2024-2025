# Given a BST and a number k find the node with the  k'th-largest key and return its content (key, value)
# E.g. With the following tree if k=1 the node is 22, since it is the largest key
#                              if k=2 the node is 12, since it is the second-largest key
#      10
#     /  \
#    8 	  12
#   / \     \
#  3   9    22
#

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from LinearStructures import Stack 
from BST import BST

# YOU CAN MODIFY THE FOLLOWING FUNCTION IN ANY WAY
# YOU CAN ADD ADDITIONAL FUNCTIONS IF NEEDED

def get_kthLargest(root, k):
    # IMPORTANT: yon cannot solve the problem by storing all the nodes inside a list
    # NOTE: you can use a stack or a queue, but it is not mandatory

    # Inorder traversal; save values in a stack; push k values
    s_key = Stack()
    s_value = Stack()
    inorder(root, s_key, s_value)

    if k == 1:
        return f"{s_key.peek()}, {s_value.peek()}"
    else:
        for _ in range(k-1):
            s_key.pop()
            s_value.pop()
        return f"{s_key.peek()}, {s_value.peek()}"
    
def inorder(root, s_key, s_value):
    if root:
        inorder(root.leftChild, s_key, s_value)
        s_key.push(root.key)
        s_value.push(root.value)
        inorder(root.rightChild, s_key, s_value)
    


# Test code
if __name__ == "__main__":
    # WARNING: DO NOT MODIFY THE TREE STRUCTURE!
    myTree = BST()
    myTree[10] = "A"
    myTree[8] = "B"
    myTree[12] = "C"
    myTree[3] = "D"
    myTree[9] = "E"
    myTree[22] = "F"

    k = 1  # expected result 22, F
    print(get_kthLargest(myTree.root, k))

    k = 2  # expected result 12, C
    print(get_kthLargest(myTree.root, k))
