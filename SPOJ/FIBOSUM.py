from math import ceil
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

MAXN = pow(10, 6)
MOD = pow(10, 9) + 7
fibb = [0] * MAXN


def f(n):
    global fibb
    if n == 0:
        return 0
    if n == 1 or n == 2:
        fibb[n] = 1
        return 1
    if n < MAXN and fibb[n]:
        return fibb[n]
    k = ceil(n / 2)
    if n & 1:
        x = pow(f(k), 2) + pow(f(k - 1), 2)
    else:
        x = ((f(k - 1) << 1) + f(k)) * f(k)
    if n < MAXN:
        fibb[n] = x % MOD
    return x


def func(n, m):
    return (f(m + 2) - f(n + 1)) % MOD


def main():
    for i in range(int(input())):
        n, m = map(int, input().split())
        print(func(n, m))
    return


if __name__ == '__main__':
    main()
