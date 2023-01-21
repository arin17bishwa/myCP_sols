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


def f(arr, i):
    if i <= 0 or i >= len(arr) - 1:
        return 0
    return (arr[i] > arr[i - 1] and arr[i] > arr[i + 1]) or (arr[i] < arr[i - 1] and arr[i] < arr[i + 1])


def func(arr, n):
    if n < 3:
        return 0
    l1 = [f(arr, i) for i in range(1, n - 1)]
    ans = sum(l1)
    answer = ans
    for i in range(n):
        p = arr[i]
        old = sum([f(arr, j) for j in range(i - 1, i + 2)])
        for j in [i - 1, i + 1]:
            if 0 <= j < n:
                for k in range(-1, 2):
                    arr[i] = k + arr[j]
                    new = sum([f(arr, ind) for ind in range(i - 1, i + 2)])
                    ans = min(ans, answer - old + new)
        arr[i] = p
    return ans


def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        print(func(arr, n))
    return


if __name__ == '__main__':
    main()
