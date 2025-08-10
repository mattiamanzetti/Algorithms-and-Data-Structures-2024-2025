# Recursive and iterative implementation of DFS traversals

from LinearStructures import Stack


# Basic binary tree
class Node:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None


# DFS Traversals

def preorder(root):
    if root:
        print(root.key)
        preorder(root.leftChild)
        preorder(root.rightChild)


def preorder_iter(root):
    if root is None:
        return

    st = Stack()
    st.push(root)

    while not st.isEmpty():

        current = st.pop()
        print(current.key)
        if current.rightChild is not None:
            st.push(current.rightChild)
        if current.leftChild is not None:
            st.push(current.leftChild)


def postorder(root):
    if root:
        postorder(root.leftChild)
        postorder(root.rightChild)
        print(root.key)


def postorder_iter(root):
    if root is None:
        return

    st = Stack()
    current = root

    while not st.isEmpty() or current is not None:

        while current:
            if current.rightChild is not None:
                st.push(current.rightChild)
            st.push(current)

            current = current.leftChild

        current = st.pop()

        if current.rightChild is not None and st.peek() == current.rightChild:
            st.pop()
            st.push(current)
            current = current.rightChild
        else:
            print(current.key)
            current = None


def inorder(root):
    if root:
        inorder(root.leftChild)
        print(root.key)
        inorder(root.rightChild)


def inorder_iter(root):
    if root is None:
        return

    current = root
    st = Stack()

    while not st.isEmpty() or current is not None:

        if current is not None:
            st.push(current)
            current = current.leftChild

        elif not st.isEmpty():
            current = st.pop()
            print(current.key)
            current = current.rightChild


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

    print('PREORDER')
    preorder(r)
    preorder_iter(r)
    print('\nINORDER')
    inorder(r)
    inorder_iter(r)
    print('\nPOSTORDER')
    postorder(r)
    postorder_iter(r)
