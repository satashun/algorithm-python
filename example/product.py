# https://atcoder.jp/contests/abc233/submissions/28209310

from itertools import *
import sys
import itertools
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def read_np(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=' ')


def readline_np(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=' ')


N, X = map(int, readline().split())
A = []
for i in range(N):
    L, *a = map(int, readline().split())
    A.append(a)

ans = 0
for i in product(*A):
    ok = True
    y = X

    for x in i:
        if y % x == 0:
            y //= x
        else:
            ok = False

    if ok and y == 1:
        ans += 1

print(ans)
