# Second Exercise: Delete the middle element of Stack
#
# Write a program that removes the middle element of a Stack
# E.g.: input [1, 2, 3, 4, 5]
#       output [1, 2, 4, 5]
#
# Try to solve it in two ways, using recursion and using iteration
#
# NOTE: you can use an auxiliary stack

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def deleteMidElemIteration(st):
    if st.isEmpty():
        return
    
    size = st.size()
    temp = Stack()
    for _ in range(int(size / 2)):
        temp.push(st.pop())
    st.pop()
    for _ in range(int(size / 2)):
        st.push(temp.pop())
    
    return st

def deleteMidElemRecursion(st, mid_point, pos):
    if st.isEmpty():
        return
    
    item = st.pop()
    deleteMidElemRecursion(st, mid_point, pos + 1)
    if pos != mid_point:
        st.push(item)
    
    return st

# Test Code
if __name__ == "__main__":
    st = Stack()

    for i in range(1, 10):
        st.push(i)

    print(st)
    # print(deleteMidElemIteration(st))
    print(deleteMidElemRecursion(st, int(st.size() / 2), 0))
