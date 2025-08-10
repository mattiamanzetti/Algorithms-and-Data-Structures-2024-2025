# AVL Tree implementation by Prof. Gerry Jenkins
# GitHub Repository: https://github.com/gerryjenkinslb/Python_AVL


class AVLNode:  # node class hidden from client
    def __init__(self, key, value = 0):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # bottom starts at height of 1

    def __iter__(self):  # this is a generator functions due to the yields
        """The standard inorder traversal of a binary tree for self that returns nodes"""
        if self.left:
            for node in self.left:  yield node  # generate left node
        yield self  # generate center node
        if self.right:
            for node in self.right: yield node  # generate right node

    def __repr__(self):
        return f"Node( k={self.key}, v={self.value}, h={self.height})"


# AVLTree implement a binary search AVL Tree with the following interface functions:
#         __contains__(y)     y in t
#         __getitem__(y)      t[y]
#         __setitem__(k, v)   t[k] = v
#         __delitem__(k)      del t[k]
#         __len__()           len(t)
#         __iter__()          for k,v in t: - in-order traversal

class AVLTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __setitem__(self, key, value):
        self.root = self._put(self.root, key, value)

    def _put(self, node, key, value):  # recursive _put follow tree down till place found for new node
        if not node: # place found, return new node
            self.size += 1
            return AVLNode(key, value)

        elif key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else: # equal
            node.value = value  # key already in tree, change value
            return node # return existing node
        return self._adjust_node(node)

    def _adjust_node(self, node):
        node.height = 1 + max(self._height(node.right), self._height(node.left))
        balance = self._balance(node)

        # check for imbalance and rotate to correct
        if balance > 1: # left heavy
            if self._balance(node.left) < 0:
                node.left = self._leftRotate(node.left) # Left Right
            return self._rightRotate(node) # catch either Left Right or Right Right
        elif balance < -1:
            if self._balance(node.right) > 0:
                node.right = self._rightRotate(node.right) # Right Left
            return self._leftRotate(node) # catch either Right Left or Left Left

        return node

    def __delitem__(self, key):
        self.root = self._delete(self.root, key)

    # Recursive function to delete a node with given key from subtree with given node.
    # It returns node of the modified subtree.
    def _delete(self, node, key):

        if not node:
            return node  # not found

        # find node with key
        elif key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:  # equal, it is found
            if node.left is None: # case of only right child
                return node.right # replace node with child
            elif node.right is None: # case of only left child
                return node.left # replace node with child

            # case of two children
            succ = self._get_min_node(node.right) # successor of node
            node.key = succ.key # copy
            node.value = succ.value
            node.right = self._delete(node.right, succ.key)  # delete succ succ key

        # # If the tree has only one node, simply return it
        # if node is None:
        #     return node

        return self._adjust_node(node)

    def _find_node(self, node, key):
        if not node:
            return None
        if node.key == key:
            return node
        if key < node.key:
            return self._find_node(node.left, key)
        return self._find_node(node.right, key)

    def __getitem__(self, key):
        node = self._find_node(self.root, key)
        return node.value if node else None

    def __contains__(self, key):
        return self[key] is not None

    def _height(self,node):
        return node.height if node else 0

    def _balance(self, node):
        return self._height(node.left) - self._height(node.right)

    def _leftRotate(self, a): #                                  a                    b
        b = a.right  #                                            \    Left         // \    < update link //
        x = b.left  #                                              b   Rotate(a)   a   c
        b.left = a   # update b left link point to a             /  \   - - ->     \\       < update link \\
        a.right = x  # replace a.right link to now point to     x    c              x
        a.height = 1 + max(self._height(a.left), self._height(a.right))
        b.height = 1 + max(self._height(b.left), self._height(b.right))
        return b

    def _rightRotate(self, a):  #                                     a                b
        b = a.left  #                                                /    Right       / \\  < update link \\
        x = b.right  #                                              b     Rotate(a)  c   a
        b.right = a  # update b right link point to a             /  \   - - ->     //      < update link //
        a.left = x  # replace c left link to now point to x      c    x            x
        a.height = 1 + max(self._height(a.left), self._height(a.right))
        b.height = 1 + max(self._height(b.left), self._height(b.right))
        return b

    def _get_min_node(self, node):
        return self._get_min_node(node.left) if node.left else node

    def __iter__(self): # client iterate in order key/values
        if not self.root: return
        for n in self.root: yield (n.key, n.value)


# Test code
if __name__ == "__main__":
    myTree = AVLTree()
    myTree[3] = "red"
    myTree[4] = "blue"
    myTree[6] = "yellow"
    myTree[2] = "green"
    myTree[7] = "orange"
    myTree[10] = "violet"
    myTree[11] = "purple"
    myTree[5] = "white"
    myTree[15] = "black"
    myTree[8] = "brown"

    for node in myTree:
        print(node)

    print()

    del myTree[4]
    myTree[20] = "magenta"
    del myTree[6]

    for node in myTree:
        print(node)

