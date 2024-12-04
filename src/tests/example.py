import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import numpy as np
import matplotlib.gridspec as gridspec

# Варіант 1.2.3
fig = plt.figure(figsize=(10, 10))
gd = gridspec.GridSpec(2, 2)

ax1 = fig.add_subplot(gd[0, 0])

x = np.linspace(-2 * np.pi, 2 * np.pi, 512)
y = np.sin(x) + np.cos(x)
ax1.plot(x, y, color="magenta")
ax1.scatter(-4, -2)
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_title("y = sin(x) + cos(x)")
ax1.set_xlim(-2 * np.pi, 2 * np.pi)
ax1.set_ylim(-3, 3)
ax1.grid(True)

ax2 = fig.add_subplot(gd[1, 0])
x = np.linspace(-5, 5, 512)
y = (x + 1) / (x - 1)
ax2.plot(x, y, color="y")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_title("y = (x+1)/(x-1)")
ax2.set_xlim(-5, 5)
ax2.set_ylim(-5, 5)
ax2.grid(True)

ax3 = fig.add_subplot(gd[:, 1])
x = np.linspace(-10, 10, 1024)


def y1(x):
    return np.sin(x) + np.cos(x)


def y2(x):
    return (x + 1) / (x - 1)


def difference(x):
    return y1(x) - y2(x)


guesses = np.array([-6, -4, -1, 6, 7.5])
roots = fsolve(difference, guesses)
print(roots)

ax3.plot(x, y1(x), color="#42c12f", lw=3, label="y = sin(x) + cos(x)")
ax3.plot(x, y2(x), color="#FF5733", lw=2, label="y = (x+1)/(x-1)")
ax3.scatter(
    roots, y1(roots), color="brown", s=32, zorder=2, label="Intersection points"
)
ax3.set_xlim(-10, 10)
ax3.set_ylim(-5, 5)
ax3.grid(True)
ax3.legend(loc="best")
ax3.set_title("Перетин графіків")
plt.show()
