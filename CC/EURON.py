from sys import setrecursionlimit
setrecursionlimit(10 ** 6)


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


def merge(l, m, r):
    global arr
    n1 = m - l + 1
    n2 = r - m
    L = arr[l:m + 1]
    R = arr[m + 1:r + 1]
    i = j = k = temp = 0

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[l + k] = L[i]
            i += 1
        else:
            temp += (n1 - i)
            arr[l + k] = R[j]
            j += 1
        k += 1
    for i1 in range(i, n1):
        arr[l + k] = L[i1]
        k += 1
    for j1 in range(j, n2):
        arr[l + k] = R[j1]
        k += 1

    return temp


def intArr():
    return map(int,input().split())


def In():
    return int(input())


def invCount(l, r):
    global ans
    if l < r:
        mid = l + (r - l) // 2
        invCount(l, mid)
        invCount(mid + 1, r)
        ans += merge(l, mid, r)
    # print(*arr)
    return ans


def func():
    global arr
    n=In()
    _=input()
    arr=list(intArr())
    return invCount(0,n-1)


def main():
    print(func())
    return


if __name__ == '__main__':
    arr=[]
    ans=0
    main()
