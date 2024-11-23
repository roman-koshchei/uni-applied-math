import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def task_1():
    fig, ax = plt.subplots()

    half_circle = patches.Wedge((0.2, 0.8), 0.1, 0, 180, color="blue")
    ax.add_patch(half_circle)

    arrow = patches.FancyArrow(0.5, 0.5, 0.2, 0, width=0.05, color="green")
    ax.add_patch(arrow)

    triangle = patches.Polygon([[0.7, 0.2], [0.8, 0.4], [0.9, 0.2]], color="red")
    ax.add_patch(triangle)

    sector = patches.Wedge((0.5, 0.8), 0.1, 0, 90, color="purple")
    ax.add_patch(sector)

    diamond = patches.Polygon(
        [[0.2, 0.2], [0.25, 0.3], [0.2, 0.4], [0.15, 0.3]], color="orange"
    )
    ax.add_patch(diamond)

    rectangle = patches.Rectangle((0.7, 0.6), 0.15, 0.1, color="yellow")
    ax.add_patch(rectangle)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.show()


def task_2():
    N = 13

    fig, ax = plt.subplots()

    angles = np.linspace(0, 2 * np.pi, N, endpoint=False)

    polygon_vertices = [(np.cos(angle), np.sin(angle)) for angle in angles]

    polygon = patches.Polygon(polygon_vertices, closed=True, edgecolor="black")
    ax.add_patch(polygon)

    for i in range(N):
        start = polygon_vertices[i]
        end = polygon_vertices[(i + 1) % N]
        arrow = patches.FancyArrow(
            start[0],
            start[1],
            end[0] - start[0],
            end[1] - start[1],
            width=0.02,
            length_includes_head=True,
            color="black",
        )
        ax.add_patch(arrow)

    ax.text(0, 0, "Polygon", fontsize=15, ha="center", va="center")

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.show()


def task_3():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    a, b, c = 1, 1, 1

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(-1, 1, 100)
    u, v = np.meshgrid(u, v)

    x = a * np.cosh(v) * np.cos(u)
    y = b * np.cosh(v) * np.sin(u)
    z = c * np.sinh(v)

    ax.plot_surface(x, y, z, color="gray", alpha=0.7)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    plt.show()


def task_4():
    u = np.linspace(-10, 10, 1000)
    x, y = np.meshgrid(u, u)

    a = 36
    b = -72
    c = 4 * x**2 + 9 * y**2 - 36 * y + 36
    D = b**2 - 4 * a * c
    D[D < 0] = 0

    sqrtD = np.sqrt(D)
    z1 = (-b + sqrtD) / (2 * a)
    z2 = (-b - sqrtD) / (2 * a)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.contour(x, y, z1, levels=50, cmap="viridis", alpha=0.7)
    ax.contour(x, y, z2, levels=50, cmap="viridis_r", alpha=0.7)

    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")
    ax.set_title("3D Contour Plot of the Surface")

    plt.show()


def task_5():
    bars_count = 17

    fig = plt.figure()
    fig.set_label("Diagram")
    ax = fig.add_subplot(111, projection="3d")

    heights_1 = np.random.rand(bars_count)
    heights_2 = np.random.rand(bars_count)
    heights_3 = np.random.rand(bars_count)

    x1 = np.zeros(bars_count)
    y1 = np.arange(bars_count)
    ax.bar3d(
        x1, y1, np.zeros(bars_count), dx=0.1, dy=0.4, dz=heights_1, color="r", alpha=0.6
    )

    x2 = np.ones(bars_count) * 3
    y2 = np.arange(bars_count)
    ax.bar3d(
        x2, y2, np.zeros(bars_count), dx=0.1, dy=0.4, dz=heights_2, color="g", alpha=0.6
    )

    y3 = np.linspace(0.05, 1, bars_count)
    x3 = np.arange(bars_count)
    ax.bar3d(
        x3, y3, np.zeros(bars_count), dx=0.1, dy=0.4, dz=heights_3, color="b", alpha=0.6
    )

    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Height")

    plt.show()


def task_6():
    fig = plt.figure(figsize=(12, 8))
    ax1 = fig.add_subplot(221, projection="3d")
    ax2 = fig.add_subplot(222, projection="3d")
    ax3 = fig.add_subplot(212, polar=True)

    # 1
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(-1, 1, 100)
    u, v = np.meshgrid(u, v)
    x = np.cosh(v) * np.cos(u)
    y = np.cosh(v) * np.sin(u)
    z = np.sinh(v)
    ax1.plot_wireframe(x, y, z, color="b")
    ax1.set_title("One-sheet hyperboloid")

    # 2
    u = np.linspace(-10, 10, 500)
    x, y = np.meshgrid(u, u)

    a = 36
    b = -72
    c = 4 * x**2 + 9 * y**2 - 36 * y + 36
    D = b**2 - 4 * a * c
    D[D < 0] = 0

    sqrtD = np.sqrt(D)
    z1 = (-b + sqrtD) / (2 * a)
    z2 = (-b - sqrtD) / (2 * a)

    ax2.contour(x, y, z1, levels=50, cmap="viridis", alpha=0.7)
    ax2.contour(x, y, z2, levels=50, cmap="viridis_r", alpha=0.7)

    ax2.set_title("3D Contour Plot of the Surface")

    # 3
    theta = np.linspace(0, 2 * np.pi, 100)
    r = 2 * np.cos(2 * theta)
    ax3.fill(theta, np.maximum(r, 0), color="lightblue", alpha=0.5)
    ax3.plot(theta, np.maximum(r, 0), color="b")
    ax3.set_title("r=2*cos(2a)")

    # Показати графіки
    plt.tight_layout()
    plt.show()


def run():
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
