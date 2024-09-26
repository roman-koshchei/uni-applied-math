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


def f(x):
    a = -2
    b = 20
    c = x**2 + 2 * math.sqrt(3) * x - 4
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


def problem_4():
    x_values = np.linspace(-5, 5, 400)

    # Calculate f(x) and g(x) directly
    f_values = x_values**2 - 2  # f(x) = x^2 - 2
    g_values = np.cos(x_values + 3)  # g(x) = cos(x + 3)

    # Create a figure with two subplots
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    # Plot f(x)
    axs[0].plot(x_values, f_values, color="green", linewidth=2)
    axs[0].set_title(r"$f(x) = x^2 - 2$", fontsize=14)
    axs[0].set_xlabel("x-axis")
    axs[0].set_ylabel("f(x)")
    axs[0].axhline(0, color="black", linewidth=0.5, linestyle="--")
    axs[0].axvline(0, color="black", linewidth=0.5, linestyle="--")
    axs[0].grid(True)

    # Plot g(x)
    axs[1].plot(x_values, g_values, color="black", linewidth=1)
    axs[1].set_title(r"$g(x) = \cos(x + 3)$", fontsize=14)
    axs[1].set_xlabel("x-axis")
    axs[1].set_ylabel("g(x)")
    axs[1].axhline(0, color="black", linewidth=0.5, linestyle="--")
    axs[1].axvline(0, color="black", linewidth=0.5, linestyle="--")
    axs[1].grid(True)

    # Adjust layout and show plot
    plt.tight_layout()


def problem_5_1():
    # Set up the x values for both lines
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400) 

    X, Y = np.meshgrid(x, y)
    # Calculate Z based on the equation y^2 = 2x
    Z = Y**2 - 2*X

    # Plotting
    plt.figure(figsize=(8, 6))
    contour = plt.contour(X, Y, Z, levels=[0], colors='blue')  
    
    # Plot line 2 (4*x - 2*y - 8 = 0)
    plt.plot(x, 2*x - 4, color="red", label=r"$4x - 2y + 23 = 0$")

    # 2*x - 4 = y
    # 4*x^2 - 18*x + 16 = 0 
    roots = np.roots([4, -18, 16])

    intersection_xs = roots # x-values of intersections found analytically
    print(intersection_xs)
    intersection_ys = [2*x - 4 for x in intersection_xs]
    print(intersection_ys)

    # Plot intersection points
    plt.scatter(intersection_xs, intersection_ys, color='red', zorder=5)

    # Add titles and labels
    plt.title("Graphs of the Equations")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")

    # Add grid and legend
    plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
    plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
    plt.grid(True)
    plt.legend()

    # Show the plot
    plt.xlim(-10, 10)
    plt.ylim(-10, 20)
    plt.tight_layout()


def problem_5_2():
    # Set up the x values for both functions
    x_values = np.linspace(0, 10, 400)  # For y^2 = 2x (only non-negative x)
    y1_positive = np.sqrt(2 * x_values)  # Positive branch of the parabola
    y1_negative = -np.sqrt(2 * x_values)  # Negative branch of the parabola

    # Set up for the linear equation
    x_values_line = np.linspace(-10, 10, 400)
    y2 = 2 * x_values_line + 23 / 2

    # Create a figure with two subplots
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    # Plot the first function (parabola)
    axs[0].plot(
        x_values, y1_positive, color="blue", label=r"$y=\sqrt{2x}$", linestyle="-"
    )
    axs[0].plot(
        x_values, y1_negative, color="blue", linestyle="--", label=r"$y=-\sqrt{2x}$"
    )
    axs[0].set_title("Graph of $y^2 = 2x$", fontsize=14)
    axs[0].set_xlabel("x-axis")
    axs[0].set_ylabel("y-axis")
    axs[0].axhline(0, color="black", linewidth=0.5, linestyle="--")
    axs[0].axvline(0, color="black", linewidth=0.5, linestyle="--")
    axs[0].grid(True)
    axs[0].legend()

    # Plot the second function (line)
    axs[1].plot(
        x_values_line, y2, color="red", label=r"$y=2x+\frac{23}{2}$", linestyle="-"
    )
    axs[1].set_title("Graph of $4x - 2y + 23 = 0$", fontsize=14)
    axs[1].set_xlabel("x-axis")
    axs[1].set_ylabel("y-axis")
    axs[1].axhline(0, color="black", linewidth=0.5, linestyle="--")
    axs[1].axvline(0, color="black", linewidth=0.5, linestyle="--")
    axs[1].grid(True)
    axs[1].legend()

    # Adjust layout and show plot
    plt.tight_layout()


def problem_6():
    # 1. Створення стовпчастої діаграми з чотирма кольорами в кожному стовпчику
    N = 18  # кількість груп
    data = np.random.randint(
        10, 50, (4, N)
    )  # випадкові дані для 4 груп в кожному стовпчику
    colors = ["red", "green", "blue", "yellow"]

    fig, ax = plt.subplots(2, 2, figsize=(14, 12))

    ind = np.arange(N)
    bottom = np.zeros(N)

    for i in range(4):
        ax[0, 0].bar(
            ind, data[i], bottom=bottom, color=colors[i], label=f"Частина {i+1}"
        )
        bottom += data[i]

    ax[0, 0].set_title("Стовпчаста діаграма з чотирма кольорами")
    ax[0, 0].set_xlabel("Групи")
    ax[0, 0].set_ylabel("Значення")
    ax[0, 0].legend()

    # 2. Створення гістограми з угрупованням
    grouped_data = np.random.randn(1000)

    ax[0, 1].hist(grouped_data, bins=20, color="purple", edgecolor="black")
    ax[0, 1].set_title("Гістограма з угрупованням")
    ax[0, 1].set_xlabel("Значення")
    ax[0, 1].set_ylabel("Частота")

    # 3. Створення кругової діаграми з виділеними секторами
    sizes = np.random.randint(5, 20, N)
    labels = [f"Сектор {i+1}" for i in range(N)]
    explode = [0.1 if i < 2 else 0 for i in range(N)]  # Виділити перші два сектори

    ax[1, 0].pie(
        sizes,
        labels=labels,
        explode=explode,
        autopct="%1.1f%%",
        colors=plt.cm.tab20.colors,
    )
    ax[1, 0].set_title("Кругова діаграма з виділеними секторами")

    # 4. Діаграма розкиду даних
    x = np.random.randn(100)
    y = np.random.randn(100)
    shapes = ["o", "s", "^", "D"]
    colors_scatter = ["red", "green", "blue", "orange"]

    for i, shape in enumerate(shapes):
        ax[1, 1].scatter(
            x[i * 25 : (i + 1) * 25],
            y[i * 25 : (i + 1) * 25],
            marker=shape,
            color=colors_scatter[i],
            label=f"Група {i+1}",
        )

    ax[1, 1].set_title("Діаграма розкиду даних")
    ax[1, 1].set_xlabel("X")
    ax[1, 1].set_ylabel("Y")
    ax[1, 1].legend()

    plt.tight_layout()


def run():
    # problem_4_3_13()
    # problem_2()
    # problem_3()
    # problem_4()
    problem_5_1()
    # problem_5_2()
    # problem_6()

    plt.show()
