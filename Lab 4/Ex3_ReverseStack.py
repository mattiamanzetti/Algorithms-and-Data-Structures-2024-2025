# Third Exercise
#
# Reversing the content of Stack using recursion
# You can use only one Stack, no other data structures are needed
# You cannot use any iterative loop
#
# HINT: you need TWO recursive functions one to empty the stack one to fill in

""" https://youtu.be/z0bS9ULg5to?si=QjUNly3pdxaTGJtv """

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from LinearStructures import Stack

def insertBack(st, item):
    if st.isEmpty():
        st.push(item) # the first time insertBack is called, the stack is empty and the value is just pushed in
    
    else:
        top_item = st.pop() # the items already in the stack are temporarely popped out
        # once the top item is popped out, it gets stored in the call stack of the recursive function
        # the memory for this temporary "storage" is automatically managed by the recursion call stack
        insertBack(st, item) 

        st.push(top_item) # this line is not executed until the recursive calls have returned 


def reverseStack(st):
    if st.isEmpty():
        return # when the stack is emptied we exit reverseStack and switch to insertBack 

    temp = st.pop()
    # once the top item is popped out, it gets stored in the call stack of the recursive function
    # the memory for this temporary "storage" is automatically managed by the recursion call stack
    reverseStack(st)

    insertBack(st, temp) # this line is not executed until the recursive calls have returned and the stack has been emptied


if __name__ == "__main__":
    st = Stack()

    for i in range(1, 10):
        st.push(i)

    print(st)
    reverseStack(st)
    print(st)
