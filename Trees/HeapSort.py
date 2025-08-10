# Heap Sort

import random


def heapify(aList, size, i):

    # Find largest among root1 and children
    largest = i
    l = 2 * i
    r = 2 * i + 1

    if l <= size and aList[i] < aList[l]:
        largest = l

    if r <= size and aList[largest] < aList[r]:
        largest = r

    # If root1 is not largest, swap with largest and continue heapifying
    if largest != i:
        aList[i], aList[largest] = aList[largest], aList[i]
        heapify(aList, size, largest)


def heapSort(aList):

    size = len(aList)
    # insert a zero at the beginning to simplify the index computation
    aList.insert(0, 0)
    i = size // 2

    while i > 0:
        heapify(aList, size, i)
        i = i - 1
    print(aList)

    while size > 1:
        aList[1], aList[size] = aList[size], aList[1]
        size = size - 1
        heapify(aList, size, 1)

    # remove the initial zero
    aList.pop(0)


if __name__ == "__main__":

    N = 10
    A = list(range(1, N + 1))
    random.shuffle(A)
    print(A)
    heapSort(A)
    print(A)

