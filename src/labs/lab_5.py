import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import sympy.plotting as sp_plot

# variant 13


def task_2_4_13_part_1():
    x = sp.Symbol("x")

    expr1 = (sp.sin(x) + sp.sin(2 * x) - sp.sin(3 * x)) / (
        (sp.exp(3 * x**2) - 1) * sp.ln(1 + x)
    )
    expr2 = ((2 ** (x - 1)) - 1) / (x**2 - 3 * x + 2)

    limit1 = sp.limit(expr1, x, 0)
    limit2 = sp.limit(expr2, x, 1)

    print("Task 2.4.14")
    print("Limit 1: " + str(limit1))
    print("Limit 2: " + str(limit2))


def task_4_3_13_part_1():
    t = sp.Symbol("t")

    y = sp.cos(t) / (sp.sin(t) ** 2)
    x = (1 + sp.cos(t)) ** 2

    dy_dt = sp.diff(y, t)
    dx_dt = sp.diff(x, t)

    dy_dx = dy_dt / dx_dt
    d2y_dx2 = sp.diff(dy_dx, t) / dx_dt

    print("Task 4.3.12")
    print("First derivative: " + str(dy_dx.simplify()))
    print("Second derivative: " + str(d2y_dx2.simplify()))


def task_2_1_13_part_2():
    x = sp.Symbol("x")

    polynomial = x**4 - 2 * x**3 - x**2 + 2 * x
    factored_polynomial = sp.factor(polynomial)
    print("Task 2.1.13")
    print(str(factored_polynomial))


def task_3_1_13_part_2():
    x = sp.Symbol("x")

    expression = 1 / (3 * (x**2) - 8 * x - 3)
    integral = sp.integrate(expression, x)

    print("Task 3.1.13")
    print(str(integral))


def task_3_2_13_part_2():
    x, y, z = sp.symbols("x y z")

    u = (x + y**2 + z**3) ** (1 / 3)

    gradient_u = [sp.diff(u, var) for var in (x, y, z)]

    m1 = {x: 3, y: 4, z: 2}
    # component is differential for symbol
    # evalf evaluates thing with params from m1 for symbols
    grad_u_at_M1 = [component.evalf(subs=m1) for component in gradient_u]

    # norm is derivative in this case
    norm_grad_u_at_M1 = sp.sqrt(sum(component**2 for component in grad_u_at_M1))

    print("Task 3.2.13")
    print(str(norm_grad_u_at_M1))


def task_3_3_13_part_2():
    x, y = sp.symbols("x y")
    z = sp.exp(-(x**2) - (y**2)) * (2 * (x**2) + y**2)

    dz_dx = sp.diff(z, x)
    dz_dy = sp.diff(z, y)

    critical_points = sp.solve((dz_dx, dz_dy), (x, y))

    # second
    d2z_dx2 = sp.diff(dz_dx, x)
    d2z_dy2 = sp.diff(dz_dy, y)
    d2z_dxdy = sp.diff(dz_dx, y)

    extrema = []
    for point in critical_points:
        # put critical point ito second
        p = {x: point[0], y: point[1]}

        determinant = d2z_dx2.subs(p) * d2z_dy2.subs(p) - d2z_dxdy.subs(p) ** 2
        f_xx = d2z_dx2.subs(p)

        # Визначаємо тип екстремуму на основі знака визначника Гессе та значення d2z_dx2
        if determinant > 0:
            if f_xx > 0:
                extrema.append((point, "Local minimum"))
            else:
                extrema.append((point, "Local maximum"))
        elif determinant < 0:
            extrema.append((point, "Saddle (not min and not max) point"))
        else:
            extrema.append((point, "Inconclusive"))

    print("Task 3.3.13")
    print(extrema)


def task_1_3_13_part_2():
    z = -64 * sp.I
    roots = sp.root(z, 3)

    print("Task 1.3.13")
    print(roots)


def task_3_1_13_part_3():
    x = sp.Symbol("x")
    f = sp.Piecewise(
        (1, (x > -sp.pi) & (x < 0)), (sp.pi - 2 * x, (x >= 0) & (x < sp.pi))
    )

    l = sp.pi
    n = 10

    # coeficients
    a0 = (1 / (2 * l)) * sp.integrate(f, (x, -l, l))
    an = [
        (1 / l) * sp.integrate(f * sp.cos(n * sp.pi * x / l), (x, -l, l))
        for n in range(1, n + 1)
    ]
    bn = [
        (1 / l) * sp.integrate(f * sp.sin(n * sp.pi * x / l), (x, -l, l))
        for n in range(1, n + 1)
    ]

    fourier_series = a0 + sum(
        an[n - 1] * sp.cos(n * sp.pi * x / l) + bn[n - 1] * sp.sin(n * sp.pi * x / l)
        for n in range(1, n + 1)
    )

    x_vals = np.linspace(-np.pi, np.pi, 500)
    f_vals = [f.subs(x, val).evalf() for val in x_vals]
    fourier_vals = [fourier_series.subs(x, val).evalf() for val in x_vals]

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, f_vals, label="f(x)", color="blue")
    plt.plot(
        x_vals,
        fourier_vals,
        label=f"Fourier Series (N={n})",
        linestyle="--",
        color="red",
    )
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Fourier Series Approximation of f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()


def task_1_1_13_part_3():
    n = sp.symbols("n")

    total_sum = sp.summation(((2**n + 7**n) / 14**n), (n, 1, sp.oo))

    print("Task 1.1.13")
    print(total_sum)


def draw_1():
    # 6.3.13
    x = sp.Symbol("x")
    y = (x**2 - 2 * x) / (x - 1)

    sp.plot(y, (x, -5, 5))


def draw_2():
    t = sp.Symbol("t")
    x = sp.sin(t)
    y = t**2 - sp.pi * t

    sp.plot_parametric(x, y, (t, -10, 10))


def draw_3():
    # 3.1.13 + 3.2.13
    x, y = sp.symbols("x y")

    eq1 = 9 * (x**2) - 36 * (y**2) + 324
    f2 = (4 / 7) * sp.sqrt(50 - 2 * x + x**2)

    p1 = sp.plot_implicit(
        eq1,
        (x, -10, 10),
        (y, -10, 10),
        show=False,
        line_color="blue",
    )
    p2 = sp.plot(f2, (x, -10, 10), show=False, line_color="red")

    p1.extend(p2)

    p1.show()


def draw_4():
    # 4.1.13
    x, y, z = sp.symbols("x y z")

    equation = 4 * x**2 + 9 * y**2 + 36 * z**2 - 36 * y - 72 * z + 36

    z_solutions = sp.solve(equation, z)

    sp_plot.plot3d(
        z_solutions[0], z_solutions[1], (x, -10, 10), (y, -10, 10), show=True
    )


def run():
    task_2_4_13_part_1()
    print()
    task_4_3_13_part_1()
    print()
    task_2_1_13_part_2()
    print()
    task_3_1_13_part_2()
    print()
    task_3_2_13_part_2()
    print()
    task_3_3_13_part_2()
    print()
    task_1_3_13_part_2()
    print()
    # task_3_1_13_part_3()
    print()
    task_1_1_13_part_3()
    print()

    draw_1()
    draw_2()
    draw_3()
    draw_4()
