from math import ceil
from sys import setrecursionlimit
from collections import deque

setrecursionlimit(10 ** 5)
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


def intArr():
    return map(int, input().split())


def In():
    return int(input())


def _dist(x1, y1, x2, y2):
    return pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 0.5)


def is_conn_circle(c1: tuple, c2: tuple):
    r1, r2 = c1[2], c2[2]
    return pow(r1 - r2, 2) <= pow(c1[0] - c2[0], 2) + pow(c1[1] - c2[1], 2) <= pow(r1 + r2, 2)


def is_on(c1, x, y):
    return pow(c1[0] - x, 2) + pow(c1[1] - y, 2) == pow(c1[2], 2)


class DSU:
    def __init__(self, n: int):
        self.root = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.rank[rx] >= self.rank[ry]:
                self.root[ry] = rx
                self.rank[rx] += self.rank[ry]
            else:
                self.root[rx] = ry
                self.rank[ry] += self.rank[rx]


def func():
    n = In()
    sx, sy, tx, ty = intArr()
    arr = [tuple(intArr()) for _ in range(n)]
    vis = [0] * n
    s = t = 0
    adj = [[] for _ in range(n)]

    def dfs(v):
        nonlocal vis, adj, t
        vis[v] = 1
        if v == t:
            return 1
        for u in adj[v]:
            if vis[u]:
                continue
            if dfs(u):
                return 1
        return 0

    for i in range(n):
        for j in range(i + 1, n):
            if is_conn_circle(arr[i], arr[j]):
                adj[i].append(j)
                adj[j].append(i)

    for i in range(n):
        if is_on(arr[i], sx, sy):
            s = i
        if is_on(arr[i], tx, ty):
            t = i

    return dfs(s)


def main():
    for _ in range(1):
        print('Yes' if func() else 'No')
    return


if __name__ == '__main__':
    main()
