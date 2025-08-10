# Selection Sort
import random


# standard way to swap item for most of languages
def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp


# Python style swap
def swapPython(A, x, y):
    A[x], A[y] = A[y], A[x]


# selection sort
def selectionSort(alist):
    for i in range(len(alist) - 1):
        positionOfMax = 0
        for j in range(len(alist) - i):
            if alist[j] > alist[positionOfMax]:
                positionOfMax = j

        swap(alist, j, positionOfMax)


# Test code
if __name__ == "__main__":
    N = 30
    A = list(range(1, N + 1))
    random.shuffle(A)

    print(A)
    selectionSort(A)
    print(A)
