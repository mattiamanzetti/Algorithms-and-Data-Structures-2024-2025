# Simpler implementation of a BST using recursion

class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def __iter__(self):
        if self.leftChild:
            for elem in self.leftChild:
                yield elem
        yield self.key, self.value
        if self.rightChild:
            for elem in self.rightChild:
                yield elem


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    # Insert a node
    def put(self, key, val=None):
        if self.root is None:
            self.root = Node(key, val)
        else:
            self._put(self.root, key, val)

    def _put(self, node, key, val=None):
        if key < node.key:
            if node.leftChild is None:
                node.leftChild = Node(key, val)
            else:
                self._put(node.leftChild, key, val)

        if key > node.key:
            if node.rightChild is None:
                node.rightChild = Node(key, val)
            else:
                self._put(node.rightChild, key, val)

    def __setitem__(self, k, v):
        self.put(k, v)

    # Get the value of a node
    def get(self, key):
        if self.root is None:
            return None
        node = self._get(self.root, key)
        if node:
            return node.value
        return None

    def _get(self, node, key):
        if not node:
            return None
        if node.key == key:
            return node
        if key < node.key:
            return self._get(node.leftChild, key)
        else:
            return self._get(node.rightChild, key)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    # Deleting a node
    def delete(self, key):
        self.root = self._delete(self.root, key)

    # Auxiliary method to find the successor
    def _findSuccessor(self, node):
        successor = node.rightChild

        # Find the leftmost leaf
        while successor.leftChild is not None:
            successor = successor.leftChild

        return successor

    def _delete(self, node, key):
        if not node:
            return node  # not found

        # find node with key
        if key < node.key:
            node.leftChild = self._delete(node.leftChild, key)
        elif key > node.key:
            node.rightChild = self._delete(node.rightChild, key)
        else:  # equal, it is found
            if node.leftChild is None:
                if node.rightChild is None:  # case of leaf node
                    return None
                else:   # case of only rightChild child
                    return node.rightChild  # replace node with child
            elif node.rightChild is None:   # case of only leftChild child
                return node.leftChild  # replace node with child

            # case of two children
            succ = self._findSuccessor(node)  # get the successor of the node
            node.key = succ.key  # copy
            node.rightChild = self._delete(node.rightChild, succ.key)  # delete succ succ key

        return node

    def __delitem__(self, key):
        self.delete(key)


# Test code (DO NOT MODIFY!)
if __name__ == '__main__':

    # FIRST BST
    bst1 = BST()
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

    bst1.delete(44)
    print(bst1[57])


