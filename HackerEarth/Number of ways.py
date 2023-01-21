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

MOD = int(1e9) + 7


def intArr():
    return map(int, input().split())


def In():
    return int(input())


def fun(k: int):
    x = pow(10, 4)
    curr = 1
    temp = [1] * (x + 1)
    for i in range(1, min(x + 1, k + 1)):
        temp[i] = curr
        curr += temp[i]
        curr %= MOD

    for i in range(min(x + 1, k + 1), x + 1):
        q = 0 if i - k - 1 < 0 else temp[i - k - 1]
        curr -= q
        temp[i] = curr % MOD
        curr += temp[i]
        curr %= MOD

    return temp.copy()


def func():
    global dp
    x, k = intArr()
    return dp[k - 1][x]


def main():
    for _ in range(In()):
        print(func())
    return


if __name__ == '__main__':
    dp = [[1] * pow(10, 4) for _ in range(100)]
    for p in range(1, 101):
        dp[p - 1] = fun(p)
    main()
