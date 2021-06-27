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


def dist(arr):
    ans=0
    n=len(arr)
    for i in range(1,n):
        if arr[i]==arr[i-1]:
            ans+=1
        ans+=1

    return ans


def func():
    n,k=intArr()
    l1=list(input())
    arr=list(intArr())
    ans=[]
    y=dist(l1)
    for i in arr:
        temp=0
        x=l1[i-1]
        # print(l1,temp)
        if i!=1:
            if x==l1[i-2]:
                temp-=1
            else:
                temp+=1
        if i!=n:
            # print(x,l1[i])
            if x==l1[i]:
                # print(1)
                temp-=1
            else:
                # print(2)
                temp+=1
        l1[i-1]=str(int(not(int(x))))
        y+=temp
        ans.append(y)
    return ans






def main():
    for _ in range(In()):
        # ans=(func())
        print(*func(),sep='\n')
        # print(ans,sep='\n')
    return


if __name__ == '__main__':
    main()
