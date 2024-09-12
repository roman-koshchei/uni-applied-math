import numpy as np

def run():
  problem_2_1_13()
  print()
  problem_2_2_13()
  print()
  problem_2_4_13()
  print()
  problem_3_1_13()


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