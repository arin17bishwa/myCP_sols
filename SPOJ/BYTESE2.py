"""NOTE: Python3 is not officially accepted in SPOJ for this problem. Just translate it to Python2."""
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
    compress = {}
    j = 0
    l1 = [0] * (n << 1)
    for i in arr:
        l1[j] = i[0]
        l1[j + 1] = i[1]
        j += 2
    l1.sort()
    j = 0
    for i in l1:
        if i not in compress:
            compress[i] = j
            j += 1
    freq = [0] * j
    j -= 1
    for i in arr:
        freq[compress[i[0]]] += 1
        freq[compress[i[1]]] -= 1
    for i in range(1, j + 1):
        freq[i] += freq[i - 1]
    return max(freq)


def main():
    for _ in range(int(input())):
        n = int(input())
        arr = [tuple(map(int, input().split())) for _ in range(n)]
        print(func(arr))
    return


if __name__ == '__main__':
    main()
