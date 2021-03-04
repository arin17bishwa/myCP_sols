"""INCOMPLETE"""

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
# region Stack
from collections import deque


class Stack(deque):
    def empty(self):
        return len(self)==0

    def top(self):
        x=self.pop()
        self.append(x)
        return x

    def bottom(self):
        x=self.popleft()
        self.appendleft(x)
        return x

# endregion


def intArr():
    return map(int,input().split())


def In():
    return int(input())


def f(l1):
    st=Stack()
    ans=[]
    n=len(l1)
    for i in range(n):
        ans.append(n)
        while len(st)>0 and st.top()[0]<=l1[i]:
            ans[st.top()[1]]=i
            st.pop()
        st.append((arr[i],i))
    return ans


def func():
    global arr
    n=len(arr)
    left,right=f(arr[::-1]),f(arr)

    pass


def main():
    global arr
    for _ in range(In()):
        n=In()
        arr=list(intArr())
        print(func())


if __name__ == '__main__':
    arr=[]
    main()
