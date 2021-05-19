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


def func(n, m, k):
    global arr
    ans = 0
    p = min(n, m)
    for i in range(1, 1 + n):
        for j in range(1, 1 + m):
            arr[i][j] += arr[i][j - 1]

    for j in range(1, 1 + m):
        for i in range(1, 1 + n):
            arr[i][j] += arr[i - 1][j]

    for q in range(1, n + 1):
        for i in range(1, n - q + 2):
            low = 1
            high = m - q + 1
            z = f = 0
            while low <= high:
                mid = (low + high) >> 1
                x = arr[i + q - 1][mid + q - 1] - arr[i + q - 1][mid - 1] - arr[i - 1][mid + q - 1] + arr[i - 1][
                    mid - 1]
                if x >= k * q * q:
                    high = mid - 1
                    z = mid
                    f = 1
                else:
                    low = mid + 1
            if f:
                ans += m - q - z + 2

    return ans


def main():
    global arr
    for _ in range(In()):
        n, m, k = intArr()
        arr = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            l1 = list(intArr())
            for j in range(m):
                arr[i + 1][j + 1] = l1[j]
        print(func(n, m, k))
    return


if __name__ == '__main__':
    arr = []
    main()
