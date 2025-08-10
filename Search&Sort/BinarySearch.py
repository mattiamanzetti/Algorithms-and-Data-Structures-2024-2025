
def binarySearch(alist, item):
    l = 0
    r = len(alist) - 1
    return __binarySearch(alist, item, l, r)


def __binarySearch(alist, item, l, r):

    # Base case
    if r < l:
        return None
    else:
        mid = (l + r) // 2

        # If element is present at the middle itself
        if alist[mid] == item:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif alist[mid] > item:
            return __binarySearch(alist, item, l, mid - 1)

        # Otherwise the element can only be present
        # in right subarray
        else:
            return __binarySearch(alist, item, mid + 1, r)


if __name__ == "__main__":

    testList = [2, 3, 4, 10, 40, 50]
    x = 50
    index = binarySearch(testList, x)
    if index is not None:
        print(x, "is present in the array at index", index)
    else:
        print(x, "is not present in the array")
