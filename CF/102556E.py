import itertools, math
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


def func(ans, i, f, *args):
    global multiples
    n = len(multiples)
    if i == n - 1:
        if f == 0:
            return ans / multiples[i]
        else:
            return ans * multiples[i]
    return func(ans, i + 1, 0) * func(ans, i + 1, 1)


def main():
    global p, multiples
    initial = float(input())
    n = int(input())
    for i in range(n):
        x = input().split(':')[1].split(';')
        for j in x:
            if "Might Multiplier" in j:
                p = float(j.split('x')[1])
                multiples.append(p)
                break
    perms = [''.join(i) for i in itertools.product('01', repeat=len(multiples))]
    n = len(multiples)
    arr = []
    for i in perms:
        p = initial
        for j in range(n):
            if i[j] == '1':
                p *= multiples[j]
            else:
                p /= multiples[j]
        arr.append(p)
    x = sum(map(math.log, arr))
    x /= len(arr)
    return math.exp(x)


if __name__ == '__main__':
    multiples = []
    p = 0
    print(main())
