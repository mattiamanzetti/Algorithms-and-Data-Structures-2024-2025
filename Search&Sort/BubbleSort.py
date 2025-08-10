# Bubble sort
import random

# standard way to swap item for most of languages
def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp


# Python style swap
def swapPython(A, x, y):
    A[x], A[y] = A[y], A[x]


def bubbleSort(alist):
    for i in range(len(alist) - 1):
        for j in range(len(alist) - 1 - i):
            if alist[j] > alist[j + 1]:
                swap(alist, j, j + 1)


# more efficient implementation
def shortBubbleSort(alist):
    exchanges = True

    for i in range(len(alist) - 1):
        if not exchanges:
            return
        exchanges = False

        for j in range(len(alist) - 1 - i):
            if alist[j] > alist[j + 1]:
                swap(alist, j, j + 1)
                exchanges = True


# Test code
if __name__ == "__main__":
    N = 30
    A = list(range(1, N + 1))
    random.shuffle(A)
    print(A)
    shortBubbleSort(A)
    print(A)
