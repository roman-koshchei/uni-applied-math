import numpy as np
import matplotlib.pyplot as plt
import math


def problem_4_3_13():
    # Avoid t=0 to prevent division by zero in sin(t)
    t = np.linspace(0.1, 2 * np.pi, 1000)

    x = (1 + np.cos(t)) ** 2
    y = np.cos(t) / (np.sin(t) ** 2)

    plt.figure(figsize=(10, 5))

    plt.plot(
        x,
        y,
        color="green",
        linestyle=":",
        label=r"$y = \frac{\cos(t)}{\sin^2(t)},\ x = (1 + \cos(t))^2$",
    )

    plt.title(
        "Parametric Plot of $y = \\frac{\\cos(t)}{\\sin^2(t)}$, $x = (1 + \\cos(t))^2$"
    )
    plt.xlabel("x")
    plt.ylabel("y")
    plt.ylim(-10, 10)  # Set limits for y to better visualize the plot
    plt.axhline(0, color="black", linewidth=0.5, ls="--")
    plt.axvline(0, color="black", linewidth=0.5, ls="--")

    plt.grid()
    plt.legend()


def problem_2():
    # Define parameters
    a = 2
    b = -2

    # Define the range for theta
    theta = np.linspace(0, 2 * np.pi, 1000)

    # Calculate the radius p using the polar equation
    p = a / (1 + b * np.cos(theta))

    # Create the polar plot
    plt.figure(figsize=(8, 8))
    ax = plt.subplot(111, projection="polar")
    plt.plot(theta, p, label=r"$p = \frac{2}{1 - 2\cos(\theta)}$")

    # Set title and legend
    ax.set_title("Polar Curve of Second Order", va="bottom")
    ax.legend(loc="upper right")

    # Show the plot


def f(x):
    a = -2
    b = 20
    c = x**2 + 2 * math.sqrt(3) * x - 47
    roots = np.roots([a, b, c])
    return roots[0], roots[1]


def problem_3():
    x_values = np.linspace(-100, 100, 4000)
    y1_values = []
    y2_values = []

    for x in x_values:
        y1, y2 = f(x)
        y1_values.append(y1)
        y2_values.append(y2)

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y1_values, label="Curve", color="blue")
    plt.plot(x_values, y2_values, color="blue")

    plt.grid()

    # Calculate the position for the label at angle α

    # Add a label at the specified angle
    plt.text(
        -80,
        30,
        "$x^2 - 2y^2 + 2\sqrt{3}x + 20y - 47 = 0$",
        fontsize=12,
        rotation=117,
        ha="center",
        va="center",
    )

    # Set title and show legend
    plt.title("Plot of the Curve $x^2 - 2y^2 + 2\sqrt{3}x + 20y - 47 = 0$")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.legend()


def run():
    problem_4_3_13()
    problem_2()
    problem_3()

    plt.show()
