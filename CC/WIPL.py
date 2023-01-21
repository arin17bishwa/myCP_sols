from collections import OrderedDict

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


def func(n: int, k: int, arr: list):
    s = sum(arr)
    if n < 2 or s < 2 * k:
        return -1

    arr.sort()
    d1 = OrderedDict()
    d1[arr[n - 1]] = None
    s1 = arr[n - 1]
    ans = -1
    for i in range(n - 2, -1, -1):
        d2 = OrderedDict()
        s1 += arr[i]
        for key in d1.keys():
            d2[key] = None
            d2[arr[i]] = None
            d2[arr[i] + key] = None
            if (key + arr[i] >= k) and (s1 - key - arr[i]) >= k:
                ans = n - i
                break
            if arr[i] >= k and s1 - arr[i] >= k:
                ans = n - i
                break
        if ans != -1:
            break
        d1 = d2
    return ans


def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        print(func(n, k, arr))
    return


if __name__ == '__main__':
    main()
