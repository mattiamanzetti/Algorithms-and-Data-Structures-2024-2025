
def linear_search(arr, x):
    for index, value in enumerate(arr):
        if value == x:
            return index
    return -1


if __name__ == "__main__":
    arr = [1, 10, 30, 15]
    x = 30
    index = linear_search(arr, x)
    if index > 0:
        print(x, "is present at index", index)
    else:
        print(x, "is not present in the array")