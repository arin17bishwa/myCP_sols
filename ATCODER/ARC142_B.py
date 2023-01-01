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


def checker(arr: list):
    n = len(arr)
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            t = []
            k = 0
            for a, b in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                t.append(arr[i + a][j + b])
            for x in t:
                k += x < arr[i][j]
            if k == 4:
                return 0
    return 1


def func():
    n = In()
    ans = [[n * i + j + 1 for j in range(n)] for i in range(n)]
    j = n * n
    t = [1, n * n]
    k = 0
    for i in range(n):
        for j in range(n):
            ans[i][j] = t[k]
            if k == 0:
                t[k] += 1
                k = 1
            else:
                t[k] -= 1
                k = 0
    # t = checker(ans)
    # if t == 0:
    #     raise ValueError
    # print(checker(ans))
    return [' '.join(map(str, i)) for i in ans]


def main():
    for _ in range(1):
        print(*func(), sep='\n')
    return


if __name__ == '__main__':
    main()