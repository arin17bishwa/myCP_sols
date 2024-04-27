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


def func():
    global arr
    n = len(arr)
    if n == 2:
        return 1

    l1 = [[0, 0] for _ in range(n)]
    for i in range(n):
        l1[i] = [i + 1, arr[i]]
    l2 = []
    l2.extend(l1[:2])
    ans = 0
    k = 2

    for i in range(2, n):
        while len(l2) >= 2:
            p = (l2[k - 1][1] - l2[k - 2][1]) / (l2[k - 1][0] - l2[k - 2][0])
            q = (l1[i][1] - l2[k - 1][1]) / (l1[i][0] - l2[k - 1][0])
            if p <= q:
                l2.pop()
                k -= 1
            else:
                break

        l2.append(l1[i])
        k += 1
        ans = max(ans, l2[k - 1][0] - l2[k - 2][0])

    return ans


def main():
    global arr
    for _ in range(In()):
        _ = In()
        arr = list(intArr())
        print(func())
    return


if __name__ == "__main__":
    arr = []
    main()
