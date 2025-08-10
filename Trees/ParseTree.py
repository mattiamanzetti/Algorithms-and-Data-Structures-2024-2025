from LinearStructures import Stack
import operator


# Basic implementation of a binary tree

class Node:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = Node('')  # initialize the tree with an empty node
    pStack.push(eTree)
    currentTree = eTree

    for el in fplist:
        # Rule 1: opening parenthesis
        if el == '(':
            currentTree.leftChild = Node('')
            pStack.push(currentTree)
            currentTree = currentTree.leftChild

        # Rule 2: operators
        elif el in ['+', '-', '*', '/']:
            currentTree.key = el
            currentTree.rightChild = Node('')
            pStack.push(currentTree)
            currentTree = currentTree.rightChild

        # Rule 4: closing parenthesis
        elif el == ')':
            currentTree = pStack.pop()

        # Rule 3: numbers
        else:
            try:
                currentTree.key = int(el)
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(el))

    return eTree


# Evaluate the equation
def postorderEval(node):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    if node:
        res1 = postorderEval(node.leftChild)
        res2 = postorderEval(node.rightChild)
        if res1 and res2:
            return opers[node.key](res1, res2)
        else:
            return node.key


def inorderPrintexp(tree):
    exp = __inorderPrintexp(tree)
    return exp[:-1]  # adjustment to remove redundant parenthesis


# Return the original expression
def __inorderPrintexp(node):
    sVal = ""
    if node:
        sVal = '(' + __inorderPrintexp(node.leftChild)
        sVal = sVal[:-1] + str(node.key)
        sVal = sVal + __inorderPrintexp(node.rightChild) + ')'
    return sVal


# Test code
if __name__ == "__main__":
    pt = buildParseTree("( 3 + ( 4 * 5 ) )")
    print(inorderPrintexp(pt))  # get the original expression
    print(postorderEval(pt))    # evaluate the expression

