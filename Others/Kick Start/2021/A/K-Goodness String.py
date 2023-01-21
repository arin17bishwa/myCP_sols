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


def calc(l1:list):
    n=len(l1)
    ans=0
    for i in range(n//2):
        if l1[i]!=l1[n-1-i]:
            ans+=1
    return ans


def func(n,k,s):
    mid=n//2
    l1=list(s)
    orig_score=calc(l1)
    ans=0
    # print(orig_score,k,mid)
    if orig_score<k:
        i=0
        while orig_score<k and i<mid:
            if l1[i]==l1[n-1-i]:
                ans+=1
                orig_score += 1
            i+=1

    elif orig_score>k:
        i = 0
        while orig_score > k and i < mid:
            if l1[i] != l1[n - 1 - i]:
                ans += 1
                orig_score -= 1
            i += 1
    return ans


def main():
    for i in range(In()):
        n,k=intArr()
        s=input()
        print('Case #{}: {}'.format(i+1,func(n,k,s)))


if __name__ == '__main__':
    main()
