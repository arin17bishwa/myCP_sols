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


def func(m, arr):
    l1 = [0] * m
    for i in arr:
        l1[i % m] += 1
    ans = 0
    # print(l1)
    if l1[0]:
        ans = 1
        l1[0] = 0
    for i in range(1, m):
        if 2 * i == m:
            continue
        a, b = l1[i], l1[m - i]

        if a == 0 or b == 0:
            ans += a + b
            l1[i] = l1[m - i] = 0
        elif abs(a - b) < 2:
            l1[i] = l1[m - i] = 0
            ans += 1

        else:
            c = min(a, b) + 1
            l1[i] = max(0, a - c)
            l1[m - i] = max(0, b - c)
            ans += (l1[i] + l1[m - i]) + 1
            l1[i] = l1[m - i] = 0

    if m % 2 == 0 and l1[m // 2]:
        ans += 1

    return ans


def main():
    for _ in range(In()):
        n, m = intArr()
        arr = list(intArr())
        print(func(m, arr))
    return


if __name__ == '__main__':
    main()
