from collections import defaultdict, deque
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


def func():
    global n, m, a, b, c
    to_color = defaultdict(deque)
    answer = [0] * m
    last = -1
    x = c[-1]
    for i in range(n):
        if b[i] != x:
            continue
        if a[i] != b[i]:
            last = i
        elif last == -1 and a[i] == b[i]:
            last = i
    if last == -1:
        return 'NO'
    for i in range(n):
        if a[i] != b[i] and i != last:
            to_color[b[i]].append(i)

    for j in range(m - 1):
        if len(to_color[c[j]]) == 0:
            answer[j] = last + 1
        else:
            x = to_color[c[j]].pop()
            a[x] = c[j]
            answer[j] = x + 1
    answer[-1] = last + 1
    a[last] = c[-1]
    for i in range(n):
        if a[i] != b[i]:
            return 'NO'
    return 'YES\n{}'.format(' '.join(map(str, answer)))


if __name__ == '__main__':
    for _ in range(int(input())):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = list(map(int, input().split()))
        print(func())
