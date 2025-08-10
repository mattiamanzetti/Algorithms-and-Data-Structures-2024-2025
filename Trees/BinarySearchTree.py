# Book implementation of a BST

class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.value = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.value = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key, self.value
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root is None:
            return None
        res = self._get(key, self.root)
        if res:
            return res.value

        return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        if currentNode.key == key:
            return currentNode
        if key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def findSuccessor(self, node):
        succ = node.rightChild
        while succ.hasLeftChild():
            succ = succ.leftChild
        return succ

    def spliceOut(self, node):
        if node.isLeaf():
            if node.isLeftChild():
                node.parent.leftChild = None
            else:
                node.parent.rightChild = None
        elif node.hasRightChild():
            if node.isLeftChild():
                node.parent.leftChild = node.rightChild
            else:
                node.parent.rightChild = node.rightChild
            node.rightChild.parent = node.parent

    def remove(self, currentNode):
        if currentNode.isLeaf():  # leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():  # this node has two children
            succ = self.findSuccessor(currentNode)
            self.spliceOut(succ)
            currentNode.key = succ.key
            currentNode.value = succ.value

        else:  # this node has one child
            if currentNode.isLeftChild():
                if currentNode.hasLeftChild():  # has a leftChild child
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                else:  # has a rightChild child
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
            elif currentNode.isRightChild():
                if currentNode.hasLeftChild():  # has a leftChild child
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:  # has a rightChild child
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
            else:  # current node is the root1
                if currentNode.hasLeftChild(): # has a leftChild child
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.value,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
                else:  # has a rightChild child
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.value,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)


# Test code
if __name__ == "__main__":

    # FIRST BST
    bst1 = BinarySearchTree()
    bst1[47] = "A"
    bst1[39] = "B"
    bst1[63] = "C"
    bst1[16] = "D"
    bst1[43] = "E"
    bst1[57] = "F"
    bst1[71] = "G"
    bst1[45] = "H"
    bst1[52] = "I"
    bst1[59] = "J"
    bst1[44] = "K"
    bst1[68] = "L"

    for node in bst1:
        print(node)

    bst1.delete(43)
    print(bst1[57])

