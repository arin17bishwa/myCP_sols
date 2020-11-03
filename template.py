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

# region smaller_fastio
from sys import stdin, stdout
from os import path

if path.exists('input.txt'):
    # ------------------Sublime--------------------------------------#
    stdin = open('input.txt', 'r')
    stdout = open('output.txt', 'w')


    def I():
        return int(input())


    def In():
        return map(int, input().split())
else:
    # ------------------PYPY FAst I/o--------------------------------#
    def I():
        return int(stdin.readline())


    def In():
        return map(int, stdin.readline().split())


    def S():
        return stdin.readline().rstrip()


    def Sn():
        return stdin.readline().split(' ')


def Out(whatever):
    return stdout.write(whatever)


# endregion

# region bisection methods
from bisect import bisect_right, bisect_left


def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError


def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i - 1]
    raise ValueError


def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i - 1]
    raise ValueError


def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


# endregion

# region segment-tree(personal)
'''
        Implementation wrt summation
'''
global tree, arr


def eff_build(arr):
    n = len(arr)
    seg = [0] * ((n << 1) + 1)
    for i in range(n):
        seg[n + i] = arr[i]
    for i in range(n - 1, 0, -1):
        seg[i] = seg[i << 1] + seg[i << 1 | 1]
    # print(seg)
    return seg


def build(arr):
    n = len(arr)
    seg = [0] * (4 * n + 1)
    _build(arr, seg, 0, 0, n - 1)
    return seg


def _build(arr, seg, ind, l, r):  # zero indexed
    if l == r:
        seg[ind] = arr[l]
        return seg[ind]

    mid = (l + r) // 2
    left = _build(arr, seg, (ind << 1) + 1, l, mid)
    right = _build(arr, seg, (ind << 1) + 2, mid + 1, r)
    seg[ind] = left + right
    return seg[ind]


def query(seg, ind, l, r, L, R):
    if r < L or l > R:
        return 0
    if l >= L and r <= R:
        return seg[ind]
    mid = (l + r) // 2
    left = query(seg, (ind << 1 | 1), l, mid, L, R)
    right = query(seg, (ind << 1) + 2, mid + 1, r, L, R, )
    return left + right  # Sum


def point_update(seg, node, l, r, ind, val):
    # print(node, l, r)
    if ind < l or ind > r:
        return
    if r <= ind <= l:
        seg[node] = val
        return
    mid = (l + r) >> 1
    point_update(seg, (node << 1 | 1), l, mid, ind, val)
    point_update(seg, (node << 1) + 2, mid + 1, r, ind, val)
    seg[node] = seg[(node << 1 | 1)] + seg[(node << 1) + 2]  # Sum


# endregion

# region persistent segment tree
BIG = 10 ** 9

vals = []
L = []
R = []


def create(n):
    """create a persistent segment tree of size n"""

    ind = len(vals)
    vals.append(BIG)

    L.append(-1)
    R.append(-1)

    if n == 1:
        L[ind] = -1
        R[ind] = -1
    else:
        mid = n // 2
        L[ind] = create(mid)
        R[ind] = create(n - mid)
    return ind


def setter(ind, i, val, n):
    """set set[i] = val for segment tree ind, of size n"""

    ind2 = len(vals)
    vals.append(BIG)

    L.append(-1)
    R.append(-1)

    if n == 1:
        vals[ind2] = val
        return ind2

    mid = n // 2
    if i < mid:
        L[ind2] = setter(L[ind], i, val, mid)
        R[ind2] = R[ind]
    else:
        L[ind2] = L[ind]
        R[ind2] = setter(R[ind], i - mid, val, n - mid)
    vals[ind2] = min(vals[L[ind2]], vals[R[ind2]])
    return ind2


def minimum(ind, l, r, n):
    """find mimimum of set[l:r] for segment tree ind, of size n"""

    if l == 0 and r == n:
        return vals[ind]
    mid = n // 2
    if r <= mid:
        return minimum(L[ind], l, r, mid)
    elif mid <= l:
        return minimum(R[ind], l - mid, r - mid, n - mid)
    else:
        return min(minimum(L[ind], l, mid, mid), minimum(R[ind], 0, r - mid, n - mid))


# endregion

# region DisjointSetUnion
class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)


# endregion

if __name__ == "__main__":
    arr = [i for i in range(1000000)]
    tree = build(arr)
    print(query(tree, 0, 0, len(arr) - 1, 0, 13000))
    point_update(tree, 0, 0, len(arr) - 1, 0, 15)
    print(query(tree, 0, 0, len(arr) - 1, 0, 130))
    pass
