"""https://codeforces.com/problemset/problem/472/A"""


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


def prime_test(n):
    if n==1:
        return 0
    if n<4:
        return 1
    if n&1==0:
        return 0
    lim=int(pow(n,0.5))+1

    for i in range(3,lim+1,2):
        if n%i==0:
            return 0
    return 1


def func():
    n=In()
    for i in range(4,n-3):
        if not prime_test(i) and not prime_test(n-i):
            return '{} {}'.format(i,n-i)


def optimal():
    n=In()
    return '{} {}'.format(9,n-9) if n&1 else '{} {}'.format(8,n-8)


def main():
    for _ in range(1):
        print(func())
    return


if __name__ == '__main__':
    main()
