# Given a Binary Tree, return the sum of all the nodes present in a level for each level of the tree
#
#  E.g.
#
#          20             Sum of level 0 = 20
#        /    \
#      15      40         Sum of level 1 = 55
#    /    \      \
#  10      30     50      Sum of level 2 = 90
#    \           /
#     22        3         Sum of level 3 = 25
#
#

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from LinearStructures import Queue, Stack

#
# DO NOT MODIFY THE FOLLOWING LINES!
#

class Node:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

#
# DO NOT MODIFY THE PREVIOUS LINES!
#


# YOU CAN MODIFY THE FOLLOWING FUNCTION IN ANY WAY
# YOU CAN ADD ADDITIONAL FUNCTIONS IF NEEDED

def level_sum_recursive(root, level, totals):
    if root is None:
        return

    if level >= len(totals):
        totals.append(0)

    totals[level] += root.key
    level_sum_recursive(root.leftChild, level + 1, totals)
    level_sum_recursive(root.rightChild, level + 1, totals)

def compute_level_sum_recursive(root):
    totals = []
    level = 0

    if root is not None:
        level_sum_recursive(root, level, totals)

    return totals    

# Test Code
if __name__ == '__main__':
    root1 = Node(20)
    root1.leftChild = Node(15)
    root1.leftChild.leftChild = Node(10)
    root1.leftChild.leftChild.rightChild = Node(22)
    root1.leftChild.rightChild = Node(30)
    root1.rightChild = Node(40)
    root1.rightChild.rightChild = Node(50)
    root1.rightChild.rightChild.leftChild = Node(3)

    # Expected outcome for the given example:
    #
    #  Sum of level 0 is 20
    #  Sum of level 1 is 55
    #  Sum of level 2 is 90
    #  Sum of level 3 is 25

    totals = compute_level_sum_recursive(root1)
    for idx, num in enumerate(totals):
        print("Sum of level", idx, "is", num)

