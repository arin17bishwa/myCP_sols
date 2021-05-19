#region normal solution
# c=0
# def func(n,l):
#     l = sorted(l[1:])
#     l1=[]
#     for i in l:
#         for j in l:
#             if i+j not in l1:
#                 l1.append(i+j)
#     f = 1
#     while f:
#         if n in l1:
#             pass
#
#
# l=list(map(int,input().split()))
# n=l[0]
# print(func(n,l))
#endregion

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


def func(n):
    global dp,a,b,c
    if n<1:
        return 0
    


def main():
    global dp,a,b,c
    n,a,b,c=intArr()
    dp=[-float('inf')]*(n+1)
    # for i in {a, b, c}:
    #     dp[i]=1
    dp[a]=1
    dp[b]=1
    dp[c]=1
    print(func(n))


if __name__ == '__main__':
    dp=[]
    a=b=c=0
    main()