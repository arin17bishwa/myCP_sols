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


def func(arr: list):
    a = b = 0
    odd = [i for i in arr if i & 1]
    even = [i for i in arr if i & 1 == 0]
    odd.sort(reverse=True)
    even.sort(reverse=True)

    o = len(odd)
    e = len(even)
    odd.append(-1)
    even.append(-1)
    i = j = 0
    while not (i == o and j == e):
        if j < e:
            p = even[j]
            q = odd[i]
            if p < q:
                i += 1
            else:
                a += p
                j += 1
        else:
            i += 1

        if even[j] == -1 and odd[i] == -1:
            break
        if i < o:
            p = even[j]
            q = odd[i]
            if q < p:
                j += 1
            else:
                b += q
                i += 1
        else:
            j += 1

    if a > b:
        return 'Alice'
    elif a < b:
        return 'Bob'
    return 'Tie'


def main():
    for _ in range(int(input())):
        _ = int(input())
        arr = list(map(int, input().split()))
        print(func(arr))
    return


if __name__ == '__main__':
    main()
