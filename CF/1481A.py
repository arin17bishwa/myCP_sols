from collections import Counter
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


def func(s,x,y):
    freq=Counter(s)
    fin_x=-freq.get('L',0)+freq.get('R',0)
    fin_y=freq.get('U',0)-freq.get('D',0)
    fx=fy=0
    if fin_x==x and fin_y==y:
        return 'YES'
    if (fin_x<x and x-fin_x<=freq.get('L',0)) or (fin_x>x and fin_x-x<=freq.get('R',0)) or fin_x==x:
        fx=1
    if (fin_y<y and y-fin_y<=freq.get('D',0)) or (fin_y>y and fin_y-y<=freq.get('U',0)) or fin_y==y:
        fy=1

    if fx and fy:
        return 'YES'
    return 'NO'


def main():
    for _ in range(int(input())):
        x,y=map(int,input().split())
        s=input()
        print(func(s,x,y))
    pass


if __name__ == '__main__':
    main()
