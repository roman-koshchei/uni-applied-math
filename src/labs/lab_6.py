import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


def task_1():
    x = sp.Symbol("x")
    y = sp.Function("y")

    print("Task 1:")
    sp.pprint(
        sp.dsolve(
            sp.Eq(
                sp.Derivative(y(x), x, 2) + sp.Derivative(y(x), x), sp.exp(-x) + x + 1
            ),
            y(x),
        )
    )


def task_2():
    x = sp.Symbol("x")
    y = sp.Function("y")(x)

    problem = sp.Eq(sp.Derivative(y, x, 2) + 9 * y, sp.sin(3 * x))

    print("Task 2:")

    general_solution = sp.dsolve(problem)
    print("General Solution:")
    sp.pprint(general_solution)

    part_solution = sp.dsolve(problem, ics={y.subs(x, 0): 2, y.diff(x).subs(x, 0): 4})
    print("Part Solution:")
    sp.pprint(part_solution)

    # Part solution is represented: y(x) = solution expression
    # solution expression is rhs (right-hand side)
    f = part_solution.rhs
    sp.plot(f, (x, -10, 10), title="Part Solution Graphic", xlabel="x", ylabel="y")


def task_3():
    t = sp.symbols("t")
    x, y = sp.Function("x")(t), sp.Function("y")(t)

    eq1 = sp.Eq(x.diff(t), 2 * x + 5 * y)
    eq2 = sp.Eq(y.diff(t), 2 * x + sp.sin(t))

    solution = sp.dsolve((eq1, eq2))
    print("Task 3:")
    for sol in solution:
        sp.pprint(sol)
        print()


def task_4():
    x, y = sp.symbols("x y")

    f = y - 2 * x + 6

    integral = sp.integrate(f, x, y)

    x_l_lim = 0
    x_r_lim = 2 - y  # 2

    y_top_lim = sp.sqrt(x)
    y_bottom_lim = 0

    double_integral = sp.integrate(
        f, (x, x_l_lim, x_r_lim), (y, y_bottom_lim, y_top_lim)
    )
    sp.pprint(double_integral)

    x_vals = np.linspace(0, 2, 1000)
    y_vals_sqrt_x = np.sqrt(x_vals)
    y_vals_2_minus_x = 2 - x_vals

    plt.figure(figsize=(8, 6))

    y_region_upper = np.minimum(y_vals_sqrt_x, y_vals_2_minus_x)
    plt.fill_between(
        x_vals,
        y_region_upper,
        0,
        color="lightblue",
        alpha=0.7,
    )

    plt.plot(x_vals, y_vals_sqrt_x, label="y = √x", color="blue")
    plt.plot(x_vals, y_vals_2_minus_x, label="y = 2 - x", color="green")
    plt.axhline(0, color="black", linewidth=0.8, linestyle="--", label="y = 0")
    plt.xlim([-0.5, 2.5])
    plt.ylim([-0.5, 2.5])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Region D bounded by y=0, y=√x, y=2-x")
    plt.legend()
    plt.grid(True)
    plt.show()


def task_5():
    x, y, r, theta = sp.symbols("x y r theta")

    # Define the boundaries in Cartesian
    line_eq = sp.sqrt(3) * x
    circle_eq = sp.sqrt(4 - (x - 2) ** 2)

    # Solve intersection between line and circle
    intersection = sp.solve(sp.sqrt(3) * x - sp.sqrt(4 - (x - 2) ** 2), x)
    x_intersect = float(intersection[0])  # Take the valid root

    # Cartesian area integration
    cartesian_area = sp.integrate(
        sp.integrate(1, (y, 0, sp.sqrt(3) * x)), (x, 0, x_intersect)
    ) + sp.integrate(
        sp.integrate(1, (y, 0, sp.sqrt(4 - (x - 2) ** 2))), (x, x_intersect, 2)
    )

    # Polar boundary (r = 4cos(theta)), limits theta = 0 to pi/3
    polar_area = sp.integrate(1 / 2 * (4 * sp.cos(theta)) ** 2, (theta, 0, sp.pi / 3))

    # Evaluate areas
    cartesian_area_eval = cartesian_area.evalf()
    polar_area_eval = polar_area.evalf()

    # Visualization
    theta_vals = np.linspace(0, np.pi / 3, 500)
    r_vals = 4 * np.cos(theta_vals)

    # Convert polar to Cartesian
    x_polar = r_vals * np.cos(theta_vals)
    y_polar = r_vals * np.sin(theta_vals)

    # Cartesian bounds
    x_vals = np.linspace(0, 2, 500)
    y_sqrt3x = np.sqrt(3) * x_vals
    y_circle = np.sqrt(4 - (x_vals - 2) ** 2)

    plt.figure(figsize=(12, 6))

    # Cartesian plot
    plt.subplot(1, 2, 1)
    plt.fill_between(
        x_vals, 0, np.minimum(y_sqrt3x, y_circle), color="lightblue", alpha=0.7
    )
    plt.plot(x_vals, y_sqrt3x, label=r"$y = \sqrt{3}x$", color="green")
    plt.plot(x_vals, y_circle, label=r"$(x-2)^2 + y^2 = 4$", color="blue")
    plt.axhline(0, color="black", linestyle="--", linewidth=0.8)
    plt.title("Декартова система координат")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()

    # Polar plot
    plt.subplot(1, 2, 2, projection="polar")
    plt.fill(x_polar, y_polar, color="lightblue", alpha=0.7, label="Область D")
    plt.plot(x_polar, y_polar, color="blue", label=r"$r = 4\cos\theta$")
    plt.title("Полярна система координат")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()


def run():
    task_1()
    print()
    task_2()
    print()
    task_3()
    print()
    task_4()
    print()
    # task_5()
