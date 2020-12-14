from sys import setrecursionlimit
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
setrecursionlimit(100000)


def eligible(s: str):
    n = len(s)
    x = int(s)
    if len(str(x)) != n or not (1 <= x <= 26):
        return 0
    return 1


def func(end: int, s: str, dp: dict):
    ans = 0
    if end == 0:
        return 1
    if end == 1:
        return eligible(s[1])+eligible(s[:2])

    if end in dp:
        return dp[end]

    x = eligible(s[end])
    if x:
        ans += func(end - 1, s, dp)
    y = eligible(s[end - 1:end + 1])
    if y:
        ans += func(end - 2, s, dp)

    dp[end] = ans
    return ans


def main():
    s = input()
    while s != '0':
        dp = {0: 1}
        print(func(len(s) - 1, s, dp))
        s = input()
    return


if __name__ == '__main__':
    main()
