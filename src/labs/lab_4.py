import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.animation as animation


def task_1():
    fig = plt.figure(figsize=(15, 8))
    plt.xlim(0, 10)
    plt.ylim(-10, 10)

    t = np.linspace(0.1, 2 * np.pi, 1000)

    x = (1 + np.cos(t)) ** 2
    y = np.cos(t) / (np.sin(t) ** 2)

    (line,) = plt.plot(x, y)

    colors = ["red", "blue", "green", "purple", "orange"]
    direction = 0.05

    def animate(i):
        nonlocal direction

        if i % 20 == 0:
            line.set_color(colors[(i // 20) % len(colors)])

        for index, value in enumerate(x):
            if (value >= 10 and y[index] <= 10) or value <= 0:
                direction *= -1
                break

        for index, value in enumerate(x):
            x[index] = value + direction

        line.set_data(x, y)

    plt.grid()
    return animation.FuncAnimation(fig, animate, interval=10, cache_frame_data=False)


def task_2():
    fig = plt.figure(figsize=(15, 8))
    ax: Axes3D = fig.add_subplot(111, projection="3d")

    a, b, c = 1, 1, 1

    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(-1, 1, 50)
    u, v = np.meshgrid(u, v)

    x = a * np.cosh(v) * np.cos(u)
    y = b * np.cosh(v) * np.sin(u)
    z = c * np.sinh(v)

    surface = ax.plot_surface(x, y, z, color="gray", alpha=0.7)

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(-10, 10)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    def rotate(angle):
        rotation_matrix = np.array(
            [
                [1, 0, 0],
                [0, np.cos(angle), -np.sin(angle)],
                [0, np.sin(angle), np.cos(angle)],
            ]
        )

        x_rotated, y_rotated, z_rotated = np.dot(
            rotation_matrix, [x.ravel(), y.ravel(), z.ravel()]
        )
        x_rotated = x_rotated.reshape(x.shape)
        y_rotated = y_rotated.reshape(y.shape)
        z_rotated = z_rotated.reshape(z.shape)

        ax.cla()
        ax.plot_surface(x_rotated, y_rotated, z_rotated, color="gray", alpha=0.7)

        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        ax.set_zlim(-2, 2)

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

    # Create an animation object
    return animation.FuncAnimation(
        fig, rotate, frames=np.linspace(0, 2 * np.pi, 100), interval=50
    )


def task_3():
    n = 2  # Кількість пелюсток
    theta = np.linspace(0, 2 * np.pi, 1000)
    r = 2 * np.cos(n * theta)

    fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
    ax.set_ylim(-2, 2)  # Встановлення меж для радіусу

    # Функція для ініціалізації анімації
    (line,) = ax.plot([], [], lw=2, color="red")

    def init():
        line.set_data([], [])
        return (line,)

    # Функція для анімації
    def animate(i):
        if i < 100:
            line.set_data(theta[: i * 10], r[: i * 10])
        else:
            phase = (i - 100) * 0.1
            r_moving = 2 * np.cos(n * (theta + phase))
            line.set_data(theta, r_moving)
        return (line,)

    return animation.FuncAnimation(
        fig, animate, init_func=init, frames=200, interval=50, blit=True
    )


def run():
    # anim = task_1()
    # anim2 = task_2()
    anim3 = task_3()
    plt.show()
