# Selection sort with visualization

import random
from matplotlib import pyplot as plt, animation


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
                                   interval=100,
                                   )

    # for showing the animation on screen
    plt.show()
    plt.close()


if __name__ == "__main__":
    N = 30
    A = list(range(1, N + 1))
    random.shuffle(A)

    # test selection sort
    generator = selectionSort(A)
    visualize(generator, "Selection Sort O(n\N{SUPERSCRIPT TWO})")
