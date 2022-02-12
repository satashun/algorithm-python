import numpy as np


def mat_mul(a, b):
    p, q, r = len(a), len(b), len(b[0])
    c = [[0] * r for _ in range(p)]
    for k in range(q):
        for i in range(p):
            for j in range(r):
                c[i][j] += a[i][k] * b[k][j]
    return c


def mat_pow(a, n):
    res = [[0] * len(a) for _ in range(len(a))]

    for i in range(len(a)):
        res[i][i] = 1

    while n > 0:
        if n % 2:
            res = mat_mul(a, res)
        a = mat_mul(a, a)
        n //= 2

    return res


def fib(n):
    # [0, 1, 1, ...]
    a = [[0, 1], [1, 1]]
    b = [[0], [1]]
    a = mat_pow(a, n)
    b = mat_mul(a, b)
    return b[0][0]


def fib_np(n):
    # numpy
    # [0, 1, 1, ...]
    a = np.array([[0, 1], [1, 1]])
    a = np.linalg.matrix_power(a, n)
    b = np.array([[0], [1]])
    a = np.dot(a, b)
    print(a)
    return a[0][0]

"""
for i in range(10):
    print(i, fib(i), fib_np(i))
"""
