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


def main():
    global arr
    for _ in range(In()):
        n,q=intArr()
        arr=list(intArr())
        # arr.insert(0,0)
        odds=[0]*(n+1)
        for i in range(1,n+1):
            if arr[i-1]&1:
                odds[i]=odds[i-1]+1
            else:
                odds[i]=odds[i-1]

        e=m=0
        t=1
        for _ in range(q):
            left,right=intArr()
            if odds[right]-odds[left-1]:
                if t:
                    e+=1
                else:
                    m+=1
            # k=0
            # for i in range(left,right+1):
            #     if arr[i-1]&1:
            #         k=1
            #         break
            # if k:
            #     if t:
            #         e+=1
            #     else:
            #         m+=1

            t=not t

        if e>m:
            print('Eren')
        elif e<m:
            print('Mikasa')
        else:
            print('Tie')


if __name__ == '__main__':
    arr=[]
    main()
