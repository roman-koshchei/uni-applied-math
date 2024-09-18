import math
import numpy as np
import sympy as sp

def run():
  problem_2_1_13()
  print()
  problem_2_2_13()
  print()
  problem_2_4_13()
  print()
  problem_3_1_13()
  print()
  problem_5_1_13()
  print()
  problem_5_3_13()
  print()
  problem_6_2_13()


def problem_2_1_13():
  a = np.array([[1, 2], [-2, 1]])
  res = np.linalg.matrix_power(a, 3) - 4 * np.linalg.matrix_power(a, 2) + a - np.eye(2)
  print("2.1.13")
  print("x =", res)

def problem_2_2_13():
  a = np.array([[1, 2, -3], [0, 1, 2], [1, 0, 4]])
  b = np.array([[1, 1, 1], [2, -3, 1], [4, 1, 5]])

  x = np.linalg.solve(a, b)
  print("2.2.13")
  print("x =", x)

def problem_2_4_13():
  a = np.array([
    [-2, 2, 1, -1, -1],
    [3, 0, -1, 1, -1],
    [1, -1, 3, 2, 4],
    [2, 1, 3, 2, 2]
  ])

  rank = np.linalg.matrix_rank(a)
  print("2.4.13")
  print("rank =", rank)

def problem_3_1_13():
  args = np.array([
    [3, 1, 2],
    [1, 3, 2],
    [2, 1, -1]
  ])

  solutions = np.array([
    -2,
    2,
    -1
  ])

  x = np.linalg.solve(args, solutions)
  print("3.1.13")
  print("x =", x)

def problem_5_1_13():
  a, b = sp.symbols('a,b')
  expression = sp.expand((5*a + 2*b) * (-1*a + 3*b)) 

  print("5.1.13 (a)")
  print(expression)

  angle = np.pi / 4
  moduleA = math.sqrt(2)
  moduleB = 3

  res = math.sqrt(moduleA**2 - 2 * moduleA * moduleB * math.cos(angle) + moduleB**2)
  print("5.1.13 (b)")
  print(res)

def problem_5_3_13():
  a = np.array([
    [3, -2, 3],
    [2, -1, 3],
    [5, 1, 12]
  ])
  
  b = np.array([10, 4, 0])

  x = np.linalg.solve(a, b)
  print("5.3.13")
  print(x)

def problem_6_2_13():
  a = np.array([0, -2, 4])
  b = np.array([-2, -2, 1])
  c = np.array([3, -3, 2])
  d = np.array([3, 3, 4])
  
  ab = b - a
  ac = c - a
  ad = d - a

  s = np.linalg.norm(np.cross(ab, ac)) / 2
  v = abs(np.dot(ab, np.cross(ac, ad))) / 6

  print("6.2.13")
  print("S =", s)
  print("V =", v)

  
