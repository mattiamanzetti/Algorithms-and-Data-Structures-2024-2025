# Merge sort variant with visualization

from matplotlib import pyplot as plt, animation
import random


def mergeSort(alist):
    start = 0
    end = len(alist) - 1
    yield from __mergesort(alist, start, end)


# function to recursively divide the array
def __mergesort(alist, start, end):

    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1

    # yield from statements have been used to yield
    # the array from the functions
    yield from __mergesort(alist, start, mid)
    yield from __mergesort(alist, mid + 1, end)
    yield from merge(alist, start, mid, end)


# function to merge the array
def merge(alist, start, mid, end):
    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if alist[leftIdx] < alist[rightIdx]:
            merged.append(alist[leftIdx])
            leftIdx += 1
        else:
            merged.append(alist[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(alist[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(alist[rightIdx])
        rightIdx += 1

    for i in range(len(merged)):
        alist[start + i] = merged[i]
        yield alist


# visualization method
def visualize(generator, text):
    # creates a figure and subsequent subplots
    fig, ax = plt.subplots()
    ax.set_title(text)
    bar_sub = ax.bar(range(len(A)), A, align="edge")

    # sets the maximum limit for the x-axis
    ax.set_xlim(0, N)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]

    # update each frame in plot
    def update(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"# of operations: {iteration[0]}")

    # creating animation object for rendering the iteration
    anim = animation.FuncAnimation(fig,
                                   func=update,
                                   fargs=(bar_sub, iteration),
                                   frames=generator,
                                   repeat=False,
                                   blit=False,
                                   interval=50,
                                   )

    # for showing the animation on screen
    plt.show()
    plt.close()


if __name__ == "__main__":
    N = 30
    A = list(range(1, N + 1))
    random.shuffle(A)

    # test merge sort
    generator = mergeSort(A)
    visualize(generator, "Merge Sort O(nlogn)")