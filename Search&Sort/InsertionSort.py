# Insertion sort
import random


def insertionSort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue
        yield alist


# Test code
if __name__ == "__main__":
    N = 30
    A = list(range(1, N + 1))
    random.shuffle(A)

    print(A)
    insertionSort(A)
    print(A)
