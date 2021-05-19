import sys
sys.setrecursionlimit(500000)
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


def func(n,e,h,a,b,c):
    if n>e and n>h:
        return pow(10,18)

    ans=pow(10,18)
    l1=1

    if e>=2*n:
        ans=min(ans,n*a)
    if h>=3*n:
        ans=min(ans,n*b)

    if e>=n and h>=n:
        ans=min(ans,n*c)

    if (e//2>=1) and ((n-e//2)*3 <= h):
        if a<b:
            x = min(n-1, e//2)
        else:
            x = max(l1, n - h//3)

        y = (a-b) * x + b * n
        ans = min(ans, y)

    if (e>n) and ((e + h) >= (2*n)):
        if a<c:
            x = min(n-1, e-n)
        else :
            x = max(l1, n-h)

        y = (a-c) * x + n * c
        ans = min(ans, y)

    if ((h-n)//2)>=(n-e) and ((h-n)//2)>0:
        if b<c:
            x = min(n - 1, (h - n)//2)
        else:
            x = max(l1, n - e)

        y=(b-c)*x + n*c
        ans=min(ans,y)

    if n>2 and h>3 and e>2:
        ans=min(ans,a+b+c+func(n-3, e-3, h-4, a, b, c))

    return ans


def main():
    for _ in range(In()):
        n,e,h,a,b,c = intArr()
        ans=func(n,e,h,a,b,c)
        if ans==pow(10,18):
            print(-1)
        else:
            print(ans)
    return


if __name__ == '__main__':
    main()
