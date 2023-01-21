import itertools,collections
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


def func(arr,n,r):
    k=len(arr)
    ans=a=b=s=0
    l1=[0]*(n+4)
    for i in arr:
        l1[i]=1
    for i in range(1,r+1):
        b+=l1[i]
    print(l1)
    for i in range(1,n-r-1):
        p=i+r-1
        print(p)
        while b<2:
            while l1[p]==1:
                p-=1
            l1[p]+=1
            ans+=1
        b=b+l1[i+r]-l1[i]

    return ans


def main():
    n,k,r=intArr()
    arr=[In() for _ in range(k)]
    print(func(arr,n,r))
    return


def f(s:str):
    # s=s
    s=s.replace(' ','').lower()
    temp=s[::-1]
    print(s,temp)
    return s==temp


if __name__ == '__main__':
    f('Ma dam')



