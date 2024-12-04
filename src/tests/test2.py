import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def task1():
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_axes([0, 0, 1, 1])

    xlim = 10
    ylim = 10
    rectSize = 1

    ax.set_xlim(0, xlim)
    ax.set_ylim(0, ylim)

    square = plt.Rectangle(
        (0, 0), rectSize, rectSize, edgecolor="red", facecolor="none", linewidth=2
    )
    ax.add_patch(square)

    xDirection = -0.05
    yDirection = -0.05

    def animate(frame):
        nonlocal xDirection
        nonlocal yDirection

        x, y = square.get_xy()

        if x >= xlim - rectSize or x <= 0:
            xDirection *= -1
        if y >= ylim - rectSize or y <= 0:
            yDirection *= -1

        new_x = x + xDirection
        new_y = y + yDirection

        square.set_xy((new_x, new_y))
        return square

    return animation.FuncAnimation(fig, animate, interval=10, cache_frame_data=False)


def task2():
    t = np.linspace(0, 2 * np.pi, 1000)

    x = 4 * (np.cos(t) ** 3)
    y = 4 * (np.sin(t) ** 3)

    fig = plt.figure()

    plt.plot(x, y)

    plt.title("x = 4 * (np.cos(t) ** 3);  y = 4 * (np.sin(t) ** 3)")

    plt.grid()


def run():
    print("Roman Koshchei, Variant 3")
    anim1 = task1()
    task2()
    plt.show()
