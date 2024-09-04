import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sin 

# Example usage
x = symbols('x')
f = sin(x)
print(f)


# Plotting example
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()
