# region fastio
import os
import sys
from functools import reduce
from io import BytesIO, IOBase
from math import sqrt, gcd

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


# region bisection methods
from bisect import bisect_right, bisect_left


def index(a, x):
    "Locate the leftmost value exactly equal to x"
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError


def find_lt(a, x):
    "Find rightmost value less than x"
    i = bisect_left(a, x)
    if i:
        return a[i - 1]
    raise ValueError


def find_le(a, x):
    "Find rightmost value less than or equal to x"
    i = bisect_right(a, x)
    if i:
        return a[i - 1]
    return -1


def find_gt(a, x):
    "Find leftmost value greater than x"
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


def find_ge(a, x):
    "Find leftmost item greater than or equal to x"
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


# endregion


def factors(n):
    lim = int(sqrt(n)) + 1
    fac = []
    for i in range(1, lim):
        if n % i == 0:
            fac.append(i)
            if i * i != n:
                fac.append(n // i)
    return fac


def func(n, m, arr):
    if n == 0:
        return 0
    if m > 1:
        hcf = reduce(gcd, arr)
    else:
        hcf = arr[0]
    fac = factors(hcf)
    fac.sort()
    x = find_le(fac, n)
    if x == -1:
        return 0
    return n - x


def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        arr = list(map(int, input().split()))
        print(func(n, m, arr))

    return


if __name__ == "__main__":
    main()
