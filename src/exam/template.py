import sympy as sp
import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import math


def task1_1():
    x = sp.Symbol("x")
    integrand = (3 * x + 13) / ((x**2 + 2 * x + 5) * (x - 1))

    indefinite_integral = sp.integrate(integrand, x)
    sp.pprint(indefinite_integral)

    f = sp.lambdify(x, indefinite_integral, modules=["numpy"])

    x_vals = np.linspace(1, 5, 500)
    y_vals = f(x_vals)

    # remove infinity
    mask = ~np.isinf(x_vals) & ~np.isinf(y_vals)
    x_vals = x_vals[mask]
    y_vals = y_vals[mask]

    fig, ax = plt.subplots(figsize=(8, 6))
    line, = ax.plot(x_vals, y_vals, color="blue")
    ax.set_title("Animation of the Graph")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    x_left_lim = -10
    x_right_lim = 10
    y_top_lim = 5
    y_bottom_lim = -15
    ax.set_xlim(x_left_lim, x_right_lim)
    ax.set_ylim(y_bottom_lim, y_top_lim)
    
    xDirection = 0.05
    yDirection = 0.05

    def update(frame):
        nonlocal xDirection
        nonlocal yDirection

        for index, (x_value, y_value) in enumerate(zip(x_vals, y_vals)):
            x_lim_reached = x_value >= x_right_lim or x_value <= x_left_lim
            y_lim_reached = y_value >= y_top_lim or y_value <= y_bottom_lim
            
            if x_lim_reached:
                xDirection *= -1

            if  y_lim_reached:
                yDirection *= -1
    

        for index, (x_value, y_value) in enumerate(zip(x_vals, y_vals)):
            x_vals[index] = x_value + xDirection
            y_vals[index] = y_value + yDirection

        line.set_data(x_vals, y_vals)

    ani = animation.FuncAnimation(fig, update, interval=10, cache_frame_data=False)

    plt.show()

def task1_2():
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')

    background_ellipse = Ellipse((0, 0), width=15, height=10, edgecolor='blue', facecolor='lightblue', alpha=0.7)
    ax.add_patch(background_ellipse)

    moving_ellipse = Ellipse((0, 0), width=5, height=3, edgecolor='red', facecolor='red', alpha=0.9)
    ax.add_patch(moving_ellipse)

    colors = ['red', 'green', 'yellow']  # Colors for the moving ellipse

    def update(frame):
        x = 4 * np.cos(frame * 0.1)  # Circular motion for x
        y = 4 * np.sin(frame * 0.1)  # Circular motion for y
        moving_ellipse.set_center((x, y))

        color_index = (frame // (len(colors) * 10)) % len(colors)
        moving_ellipse.set_facecolor(colors[color_index])
        moving_ellipse.set_edgecolor(colors[color_index])

        return moving_ellipse,

    frames = 300  # Total number of frames
    ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

    plt.show()

    

def task2():
    t = sp.Symbol("t")
    x = sp.Function("x")(t)
    y = sp.Function("y")(t)

    eq1 = sp.Eq(x.diff(t), -x - 2 * y)
    eq2 = sp.Eq(y.diff(t), 3 * x + 4 * y)
    initial_conditions = {x.subs(t, 0): 1, y.subs(t, 0): 2}

    solution = sp.dsolve([eq1, eq2], [x, y], ics=initial_conditions)
    sp.pprint(solution)

    x_sol = solution[0].rhs
    y_sol = solution[1].rhs

    sp.plot(
        x_sol,
        y_sol,
        # (t, 0, 2),
        legend=True,
        title="Solution to the System of Differential Equations",
        xlabel="t",
        ylabel="Solutions",
        show=True,
    )


def run():
    print("Exam Template")

    task1_1()
    task1_2()
    # task2()
