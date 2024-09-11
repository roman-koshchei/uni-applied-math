import numpy as np
import matplotlib.pyplot as plt

def run(): 
  x = np.linspace(0, 10, 50)
  y = x

  plt.subplot(2, 1, 1)
  plt.plot(x, y, "r--")

  y2 = [i**2 for i in x]
  plt.plot(x, y2, "b--")
  plt.grid()

  plt.subplot(2, 1, 2)

  plt.bar(["apple", "banana", "watermellon"], [67, 14, 90])
  plt.title("Fruits")

  plt.show()