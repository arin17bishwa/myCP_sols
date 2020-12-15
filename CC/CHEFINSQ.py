# region fastio
import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion


# region combinatorics nos

import math
import operator as op
from functools import reduce


def memoize(f):
    """memoization decorator for a function taking one or more arguments"""

    class memodict(dict):
        def __getitem__(self, *key):
            return dict.__getitem__(self, key)

        def __missing__(self, key):
            ret = self[key] = f(*key)
            return ret

    return memodict().__getitem__


@memoize
def catalan_recursive(n):
    if n == 0:
        return 1
    return (2 * (2 * n - 1) * catalan_recursive(n - 1)) // (n + 1)


@memoize
def euler_recursive(n, k):
    if (k == 0) or (n - 1 == k):
        return 1
    return (n - k) * euler_recursive(n - 1, k - 1) + (k + 1) * euler_recursive(n - 1, k)


@memoize
def stirling_1_recursive(n, k):
    if n == k == 0:
        return 1
    if (n == 0) or (k == 0):
        return 0
    return stirling_1_recursive(n - 1, k - 1) + (n - 1) * stirling_1_recursive(n - 1, k)


@memoize
def stirling_2_recursive(n, k):
    if (k == 1) or (n == k):
        return 1
    return stirling_2_recursive(n - 1, k - 1) + k * stirling_2_recursive(n - 1, k)


nCr = lambda n, r: reduce(op.mul, range(n - r + 1, n + 1), 1) // math.factorial(r)

multinomial = lambda k: math.factorial(sum(k)) // reduce(op.mul, (math.factorial(i) for i in k))

derangements = lambda n: int(math.factorial(n) / math.e + 0.5)

bell = lambda n: sum(stirling_2_recursive(k, n) for k in range(n + 1))

catalan = lambda n: nCr(2 * n, n) // (n + 1)

euler = lambda n, k: sum((1 - 2 * (j & 1)) * nCr(n + 1, j) * ((k + 1 - j) ** n) for j in range(k + 1))

stirling_2 = lambda n, k: sum(((-1) ** (k - j)) * nCr(k, j) * (j ** n) for j in range(k + 1)) // math.factorial(k)

# endregion


# region bisection methods
from bisect import bisect_right, bisect_left


def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return i - 1
    raise ValueError


def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return i
    raise ValueError


# endregion


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        arr.sort()
        z = arr[k - 1]
        x = find_ge(arr, z)
        y = find_le(arr, z)
        print(nCr(y - x + 1, k-x))


if __name__ == '__main__':
    main()
