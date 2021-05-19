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
    a, b = intArr()
    s = list(input())
    n = len(s)
    ones = s.count('1')
    zeros = s.count('0')
    d1 = {'0': a - zeros, '1': b - ones}
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            if '?' not in (s[i], s[n - 1 - i]):
                return -1
            if s[i] == '?':
                s[i] = s[n - 1 - i]
            else:
                s[n - 1 - i] = s[i]
            d1[s[i]] -= 1
    for i in d1.values():
        if i < 0:
            return -1

    if n & 1 and s[n // 2] == '?':
        if d1['1'] & 1:
            d1['1'] -= 1
            x = '1'
        elif d1['0'] & 1:
            d1['0'] -= 1
            x = '0'
        else:
            return -1
        s[n // 2] = x
    for i in range(n // 2):
        if s[i] != '?':
            continue
        if d1['0'] > d1['1']:
            x = s[i] = s[n - 1 - i] = '0'
        else:
            x = s[i] = s[n - 1 - i] = '1'
        d1[x] -= 2
    for i in d1.values():
        if i < 0:
            return -1
    p = s.count('0')
    q = n - p
    if a != p or b != q:
        return -1
    return ''.join(s)


def main():
    for i in range(In()):
        print(func())
    return


if __name__ == '__main__':
    main()
