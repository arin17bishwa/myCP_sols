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
    return map(int,input().split())


def In():
    return int(input())


def func(n,k1,k2,w,b):
    # if k1==k2:
    #     if w<=k1 and b<=n-k1:
    #         return 'YES'
    #     return 'NO1'
    # if abs(k1-k2)%2==1:
    #     return 'NO2'
    # p=(k1+k2)//2
    # q=2*n-p
    # if p>=w and b<=q:
    #     return 'YES'
    # return 'NO3'

    p1=min(k1,k2)
    p2=p1+(max(k1,k2)-p1)//2
    if p2<w:
        return 'NO'
    q1=min(n-k1,n-k2)
    q2=q1+(max(n-k1,n-k2)-q1)//2
    if q2<b:
        return 'NO'
    return 'YES'

def main():
    for _ in range(In()):
        n,k1,k2=intArr()
        w,b=intArr()
        print(func(n,k1,k2,w,b))


if __name__ == '__main__':
    main()
