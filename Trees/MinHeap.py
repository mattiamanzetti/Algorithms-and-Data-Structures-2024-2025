# Implementation of a Min Heap

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    # heapify up, book implementation
    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    # Insert a new element, logically equivalent to a enqueue in the priority queue
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    # Heapify down recursive implementation
    def heapify(self, i):

        # Find the smallest among the curent node and its children
        smallest = i
        l = 2 * i
        r = 2 * i + 1

        if l <= self.currentSize and self.heapList[i] > self.heapList[l]:
            smallest = l

        if r <= self.currentSize and self.heapList[smallest] > self.heapList[r]:
            smallest = r

        # If current tree is not the smallest, swap with the smallest and continue 'heapifying'
        if smallest != i:
            self.heapList[i], self.heapList[smallest] = self.heapList[smallest], self.heapList[i]
            self.heapify(smallest)

    # Heapify down, book implementation
    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    # Auxiliary method to find the index of the min child
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    # Extract the min element, logically equivalent to a dequeue from the priority queue
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        # self.heapify(1)
        self.percDown(1)
        return retval

    # Transform a given list in a min heap
    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]

        while i > 0:
            # self.heapify(i)
            self.percDown(i)
            i = i - 1


# Test code
if __name__ == "__main__":
    myList = [2, 4, 5, 8, 6, 9, 7]

    # create a binary heap from a list
    bh = BinHeap()
    bh.buildHeap(myList)
    print(bh.heapList[1:])

    # extract min
    bh.delMin()
    print(bh.heapList[1:])

    # insert a new value
    bh.insert(3)
    print(bh.heapList[1:])



