# Quick Sort

import random


def quickSort(alist):
    first = 0
    last = len(alist) - 1
    __quickSort(alist, first, last)


def __quickSort(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        __quickSort(alist, first, splitpoint - 1)
        __quickSort(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


# Test code
if __name__ == "__main__":
    N = 30
    A = list(range(1, N + 1))
    random.shuffle(A)

    print(A)
    quickSort(A)
    print(A)
