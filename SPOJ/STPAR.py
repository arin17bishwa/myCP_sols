from collections import deque
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


def func(arr: list):
    n = len(arr)
    road = deque(iterable=arr)
    street = deque()
    ans = [0] * n
    i = 0
    while i < n and len(road) > 0:
        if len(street) > 0:
            x = street.pop()
            if i + 1 == x:
                ans[i] = x
                i += 1
                continue
            else:
                street.append(x)
        y = road.pop()
        if y == i + 1:
            ans[i] = y
            i += 1
        else:
            street.append(y)
    while len(street) > 0:
        ans[i] = street.pop()
        i += 1

    q = all([ans[i] == i + 1 for i in range(n)])
    if q:
        return 'yes'
    return 'no'


def main():
    n = int(input())
    while n:
        arr = list(map(int, input().split()))[::-1]
        print(func(arr))
        n = int(input())
    return


if __name__ == '__main__':
    main()
