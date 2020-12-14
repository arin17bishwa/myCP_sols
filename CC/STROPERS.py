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


def operate(s: list, number):
    number -= 1
    c = s.count('1')
    n = len(s)
    if c == n or c == 0:
        return s
    i = j = 0
    while i < n:
        f = 0
        if s[i] == '1':
            i += 1
            continue
        p = j = i + 1
        # print(j)
        c = 0
        while j < n:

            if s[j] == '1':
                c += 1
                if c == 2:
                    f = 1
                    i = j + 1
                    break
            j += 1
        if f:
            # print(1111111)
            # print(i,p)
            if p >= 2:
                # print(s[p-1:i],s[i-1:p-2:-1])
                s[p - 1:i] = s[i - 1:p - 2:-1]
            else:
                # print(s[p - 1:i], s[i - 1::-1])
                s[p - 1:i] = s[i - 1::-1]
            i -= 2

        i += 1
    if number:
        return operate(s, number)
    return s


def func(s: str):
    n = len(s)
    sub = []
    for i in range(1, n + 1):
        for j in range(n - i + 1):
            sub.append(s[j:j + i])
    # x = map(list, set(sub))
    # print(sub)
    # print(set(sub))
    y = map(lambda x: operate(x, 3), map(list, sub))
    z = list(map(''.join, y))
    # print(set(z))
    return len(set(z))


def main():
    t = int(input())
    for _ in range(t):
        s = input()
        print(func(s))
    return


if __name__ == '__main__':
    main()
