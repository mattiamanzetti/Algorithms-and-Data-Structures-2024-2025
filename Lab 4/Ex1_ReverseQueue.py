# Reverse the content of a Queue using Recursion
# You can use only one Queue, no other data structures are needed
# You cannot use any iterative loop

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
    
def reverseQueue(q):
    if q.isEmpty():
        return

    elem = q.dequeue()
    reverseQueue(q)
    q.enqueue(elem)

if __name__ == "__main__":
    q = Queue()

    for i in range(1, 10):
        q.enqueue(i)

    print(q)
    reverseQueue(q)
    print(q)