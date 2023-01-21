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


def func(n, m, arr):
    x = y = (-1, -1)
    l1 = [(-1, -1) for _ in range(n)]
    f = 1
    for i in range(n):
        p = arr[i]
        try:
            start = p.index('1')
        except ValueError:
            continue
        last = start
        f = 0
        for j in range(m):
            if p[j] == '1':
                last = j
        l1[i] = (start, last)

    if f:
        return 'NO'

    for i in range(n):
        if l1[i][0] != -1:
            x = (l1[i], i)
            break

    for i in range(n - 1, -1, -1):
        if l1[i][0] != -1:
            y = (l1[i], i)
            break

    for i in range(x[1], y[1] + 1):
        if l1[i][0] != x[0][0] or l1[i][1] != y[0][1]:
            return 'NO'
        p = arr[i]
        for j in range(x[0][0], y[0][1] + 1):
            if p[j] == '0':
                return 'NO'
    return 'YES'


def main():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        arr = [input() for _ in range(n)]
        print(func(n, m, arr))
    return


if __name__ == '__main__':
    main()
