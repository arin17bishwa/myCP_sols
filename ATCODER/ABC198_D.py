import itertools as it
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


def main():
    s = [list(map(ord, input())) for _ in range(3)]
    chars = set(s[0] + s[1] + s[2])
    if len(chars) > 10:
        return 'UNSOLVABLE'

    inv = [0] * 256

    for i, c in enumerate(chars):
        inv[c] = i

    for i in range(3):
        for j in range(len(s[i])):
            s[i][j] = inv[s[i][j]]

    for perm in it.permutations(range(10), len(chars)):
        if any([perm[s[i][0]] == 0 for i in range(3)]):
            continue

        temp = [0] * 3
        for i in range(3):
            for j in s[i]:
                temp[i] = temp[i] * 10 + perm[j]

        if sum(temp[:2]) == temp[2]:
            return '\n'.join(map(str, temp))

    return 'UNSOLVABLE'


if __name__ == '__main__':
    print(main())
