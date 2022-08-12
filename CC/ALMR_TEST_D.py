"""
FROM https://www.codechef.com/viewsolution/61937321
"""
from collections import defaultdict
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


class Query:
    def __init__(self, u: int, v: int, x: int):
        self.u = u
        self.v = v
        self.x = x

    def __str__(self):
        return '({},{},{})'.format(self.u, self.v, self.x)

    def __repr__(self):
        return self.__str__()


class Solution(object):
    n = k = tt = 1
    value = []
    sz = []
    cnt = []
    ans = defaultdict(int)
    correspondingX = [[]]
    adj = []
    divisors = [[]]
    query = []

    def __init__(self):
        self.temp = 200000
        self.divisors = [[] for _ in range(self.temp + 5)]
        self.pre()

    def pre(self) -> None:
        for i in range(1, self.temp + 1):
            j = i
            for k in range(j, self.temp + 1, i):
                self.divisors[k].append(i)

    def add(self, x: int, p: int, val: int) -> None:
        for i in self.adj[x]:
            if i != p:
                self.add(i, x, val)
        self.cnt[self.value[x]] += val

    def dfs_size(self, x: int, p: int) -> None:
        for i in self.adj[x]:
            if i != p:
                self.dfs_size(i, x)
                self.sz[x] += self.sz[i]
        self.sz[x] += 1

    def dfs_cnt(self, x: int, p: int, keep: int) -> None:
        bc = mx = -1
        for i in self.adj[x]:
            if i != p:
                if self.sz[i] > mx:
                    mx = self.sz[i]
                    bc = i

        for i in self.adj[x]:
            if i != p and i != bc:
                self.dfs_cnt(i, x, 0)

        if bc != -1:
            self.dfs_cnt(bc, x, 1)

        self.cnt[self.value[x]] += 1

        for i in self.adj[x]:
            if i != p and i != bc:
                self.add(i, x, 1)

        for s in self.correspondingX[x]:
            for j in self.divisors[s]:
                self.ans[(x, s)] += self.cnt[j]

        if keep == 0:
            self.add(x, p, -1)

    def solving(self):
        n, q = intArr()
        # self.value = [0] * (n + 1)
        self.sz = [0] * (n + 1)
        self.cnt = [0] * (self.temp + 5)
        self.query = []
        self.correspondingX = [[] for _ in range(n + 1)]
        self.adj = [[] for _ in range(n + 1)]
        self.value = [0] + list(intArr())
        for _ in range(1, n):
            u, v = intArr()
            self.adj[u].append(v)
            self.adj[v].append(u)

        for _ in range(q):
            u, v, x = intArr()
            self.query.append((u, v, x))
            self.correspondingX[u].append(x)
            self.correspondingX[v].append(x)

        self.dfs_size(1, 0)
        self.dfs_cnt(1, 0, 0)
        answers = self._solving()
        return '\n'.join(answers)

    def _solving(self):
        ans = []
        for u, v, x in self.query:
            a = self.ans[(u, x)]
            b = self.ans[(v, x)]
            if a > b:
                curr = str(u)
            elif b > a:
                curr = str(v)
            else:
                curr = 'Draw'
            ans.append(curr)
        return ans


def func():
    s = Solution()
    return s.solving()


def main():
    for _ in range(1):
        print(func())
    return


if __name__ == '__main__':
    main()
