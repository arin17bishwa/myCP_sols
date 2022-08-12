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


def intArr():
    return map(int, input().split())


def In():
    return int(input())


def match(l1: list, s: list, st: int):
    if 2 * (len(l1)) > len(s):
        return 0
    for i in range(len(l1)):
        if l1[i] != s[st + i]:
            return 0
    return 1


def func():
    n = In()
    s = list(input())
    if n == 1:
        return 1
    return rec(s, 0, n - 1)


def rec(s: list, used: int, end: int):
    if end == 0:
        return 0 if used else 1
    n = end + 1
    if used:
        if n % 2 == 1:
            return 0
        return s[:n // 2] == s[n // 2:n] and rec(s, used=0, end=n // 2 - 1)
    if n % 2 == 1:
        return rec(s, used=1, end=end - 1)

    return rec(s, used=1, end=end - 1) or (s[:n // 2] == s[n // 2:n] and rec(s, used=0, end=n // 2 - 1))


def main():
    for _ in range(In()):
        print('YES' if func() else 'NO')
    return


if __name__ == '__main__':
    main()
