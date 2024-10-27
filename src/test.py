import numpy as np
import matplotlib.pyplot as plt
import math

# 1 | 2 | 3
# legenda
# x and y lines, different colors and arrows
# 1.2.6 (a, b)


def run():
    fig = plt.figure(figsize=(16, 9))

    x = np.linspace(-10, 10, 400)

    # a
    y_a = 1 / (np.power(x, 2) + 2)

    ax1 = fig.add_subplot(221)
    ax1.plot(x, y_a, color="blue")

    ax1.grid()
    ax1.set_title(r"Plot of $y =\frac{1}{x^2 + 2}$")

    ax1.scatter(-4, 0, color="red")

    # b
    y_b = (1 / np.tan(x)) ** 3

    ax2 = fig.add_subplot(222)
    ax2.plot(x, y_b, color="orange")

    ax2.grid()
    # Limit the y-axis to avoid extreme values, because graphic will be bad
    ax2.set_ylim(-50, 50)
    ax2.set_title(r"Plot of $y = \cot^3(x)$")

    # a and b
    ax3 = fig.add_subplot(212)

    ax3.plot(x, y_a, color="b", label=r"$y = \frac{1}{x^2 + 2}$")
    ax3.plot(x, y_b, color="orange", label=r"$y = \cot^3(x)$")

    # points of intersection
    tolerance = 0.02
    intersections = np.isclose(y_a, y_b, atol=tolerance)
    intersect_x = x[intersections]
    intersect_y = y_a[intersections]

    # scatter draws points!
    ax3.scatter(
        intersect_x,
        intersect_y,
        color="black",
        zorder=3,
        alpha=0.5,
        label="Intersections",
    )

    ax3.set_title(r"Plots of  $y =\frac{1}{x^2 + 2}$ and $y = \cot^3(x)$")
    ax3.set_xlabel("x-axis")
    ax3.set_ylabel("y-axis")
    ax3.grid()
    ax3.legend(loc="upper right")
    ax3.set_ylim(-10, 10)

    n = intersect_x.size
    i = 0
    while i < n:
        print(intersect_x.item(i), intersect_y.item(i))
        i += 1

    plt.tight_layout()
    plt.show()
