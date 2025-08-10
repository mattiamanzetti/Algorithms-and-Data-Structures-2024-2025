# Insertion Sort with visualization

import random
from matplotlib import pyplot as plt, animation


def insertionSort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue
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


# Test code
if __name__ == "__main__":
    N = 30
    A = list(range(1, N + 1))
    random.shuffle(A)

    generator = insertionSort(A)
    visualize(generator, "Insertion Sort O(n\N{SUPERSCRIPT TWO})")
