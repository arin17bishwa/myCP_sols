"""NOT DONE"""

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


# region segment-tree(personal)
'''
        Implementation wrt Max
'''
global tree, arr


def eff_build(arr):
    n = len(arr)
    seg = [0] * ((n << 1) + 1)
    for i in range(n):
        seg[n + i] = arr[i]
    for i in range(n - 1, 0, -1):
        seg[i] = max(seg[i << 1] , seg[i << 1 | 1])
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
    seg[ind] = max(left, right)
    return seg[ind]


def query(seg, ind, l, r, L, R):
    if r < L or l > R:
        return -1
    if l >= L and r <= R:
        return seg[ind]
    mid = (l + r) // 2
    left = query(seg, (ind << 1 | 1), l, mid, L, R)
    right = query(seg, (ind << 1) + 2, mid + 1, r, L, R, )
    return max(left , right)  # Max


# endregion


def main():
    n=int(input())
    arr=list(map(int,input().split()))
    k=int(input())
    seg_tree=build(arr)
    for i in range(n-k+1):
        print(query(seg_tree,0,0,len(arr)-1,i,i+k-1),end=' ')

    return


if __name__ == '__main__':
    main()
