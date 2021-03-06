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

REFLECTIONS = {'0': '0', '1': '1', '2': '5', '5': '2', '8': '8'}


def intArr():
    return map(int, input().split())


def In():
    return int(input())


def check(s):
    for i in s:
        if i not in REFLECTIONS:
            return 0
    return 1


def validity(t1, h, m):
    if 0 <= int(t1[0]) < h and 0 <= int(t1[1]) < m:
        return 1
    return 0


def reflect(t1):
    temp = [0, 0]
    temp[0] = REFLECTIONS[t1[1][1]] + REFLECTIONS[t1[1][0]]
    temp[1] = REFLECTIONS[t1[0][1]] + REFLECTIONS[t1[0][0]]
    return temp.copy()


def incTime(t1, h, m):
    hr, mi = t1[0], t1[1]
    mi = int(mi) + 1
    hr = int(hr)
    hr += mi // m
    mi %= m
    hr %= h
    temp = [str(hr).zfill(2), str(mi).zfill(2)]
    return temp.copy()


def func(h, m, l1):
    curr = l1.copy()
    while 1:
        temp1 = ''.join(curr)
        if check(temp1):
            reflected = reflect(curr)
            if validity(reflected.copy(), h, m):
                return ':'.join(curr)
        curr = incTime(curr, h, m)


def main():
    for _ in range(In()):
        h, m = intArr()
        l1 = input().split(':')
        print(func(h, m, l1))
    return


if __name__ == '__main__':
    main()
