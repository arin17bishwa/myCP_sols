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


def check(arr, initial=0):
    initial = initial
    n, m = len(arr), len(arr[0])
    for i in range(n):
        curr = initial
        for j in range(m):
            if (curr == 0 and arr[i][j] == 'W') or (curr == 1 and arr[i][j] == 'R'):
                return 0
            curr = not curr
        initial = not initial
    return 1


def make(n, m, initial=0):
    arr = [[0] * m for _ in range(n)]
    initial = initial

    for i in range(n):
        curr = initial
        for j in range(m):
            arr[i][j] = 'W' if curr else 'R'
            curr = not curr
        initial = not initial
    return arr.copy()


def func():
    n, m = intArr()
    arr = [list(input()) for _ in range(n)]
    f1 = check(arr, 1)
    f2 = check(arr, 0)
    if f1 == 0 and f2 == 0:
        return 'NO'
    elif f1 == 1:
        print('YES')
        return '\n'.join([''.join(i) for i in make(n, m, 1)])
    else:
        print('YES')
        return '\n'.join([''.join(i) for i in make(n, m, 0)])


def main():
    for _ in range(In()):
        print(func())
    return


if __name__ == '__main__':
    main()
