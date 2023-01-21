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


def func(ans,x,y,depth,last):
    global answer,arr
    if (not -1<x<20) or (not -1<y<20):
        return 1

    if depth<4:
        if last!=0:
            answer=max(answer,func(ans*arr[x][y],x,y+1,depth+1,1))
        if last!=1:
            answer=max(answer,func(ans*arr[x][y],x,y-1,depth+1,0))
        if last!=2:
            answer=max(answer,func(ans*arr[x][y],x-1,y,depth+1,3))
        if last!=3:
            answer=max(answer,func(ans*arr[x][y],x+1,y,depth+1,2))
        if last!=4:
            answer=max(answer,func(ans*arr[x][y],x+1,y,depth+1,7))
        if last!=5:
            answer=max(answer,func(ans*arr[x][y],x+1,y,depth+1,6))
        if last!=6:
            answer=max(answer,func(ans*arr[x][y],x+1,y,depth+1,5))
        if last!=7:
            answer=max(answer,func(ans*arr[x][y],x+1,y,depth+1,7))
        return answer
    else:
        return ans*arr[x][y]



def main():
    global arr
    arr=[list(intArr()) for _ in range(20)]
    # print(arr)
    k=0
    for i in range(20):
        for j in range(20):
            k=max(k,func(1,i,j,0,0))
    print(k,answer)


if __name__ == '__main__':
    answer=0

    main()
    arr=[]



