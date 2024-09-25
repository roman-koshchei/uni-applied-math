import numpy as np


def run():
    a = np.array([1, 2, 3], float)
    b = np.array([0, 2, 1, 0], int)

    c = a.take(b)
    print(c)
    # c = a + b

    # print(c)

    # print(c.mean())

    # n = np.array([[1,2,3,4], [5,2,6,7]], float)

    # print(n)
    # print(n >= 5)
    # print(n[n >= 5])
