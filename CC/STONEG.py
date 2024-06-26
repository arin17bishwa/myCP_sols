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
    n = In()
    arr = list(intArr())
    pref = [arr[0]] * n
    suffix = [arr[-1]] * n
    pref_sum = [0] * n
    suffix_sum = [0] * n

    for i in range(1, n - 1):
        x = max(arr[i], pref[i - 1] + 1)
        pref_sum[i] = pref_sum[i - 1] + (x - arr[i])
        pref[i] = x

    for i in range(n - 2, -1, -1):
        x = max(arr[i], suffix[i + 1] + 1)
        suffix_sum[i] = suffix_sum[i + 1] + (x - arr[i])
        suffix[i] = x

    ans = float("inf")
    for i in range(1, n - 1):
        curr = pref_sum[i - 1] + suffix_sum[i + 1]
        curr += max(pref[i], suffix[i]) - arr[i]
        ans = min(ans, curr)

    return ans


def main():
    for _ in range(In()):
        print(func())
    return


if __name__ == "__main__":
    main()
