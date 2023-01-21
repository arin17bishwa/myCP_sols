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


def f(x, y):
    global arr
    arr[x][y] = '*'


def func():
    global arr
    n = len(arr)
    ords = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '*':
                ords.append([i, j])

    a, b = ords
    if a[0] == b[0]:
        if a[0] == 0:
            x = 1
        else:
            x = 0
        f(x, a[1])
        f(x, b[1])
    elif a[1] == b[1]:
        if a[1] == 0:
            y = 1
        else:
            y = 0
        f(a[0], y)
        f(b[0], y)
    else:
        f(a[0], b[1])
        f(b[0], a[1])
    return '\n'.join([''.join(i) for i in arr])


def main():
    global arr
    for _ in range(In()):
        n = In()
        arr = [list(input()) for _ in range(n)]
        print(func())
    return


if __name__ == '__main__':
    arr = []
    main()
