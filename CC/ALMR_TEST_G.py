from collections import deque

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
sys.setrecursionlimit(10 ** 5 + 5)


def intArr():
    return map(int, input().split())


def In():
    return int(input())


class Edge:
    def __init__(self, x: int, y: int, cap: int, flow: int):
        self.x = x
        self.y = y
        self.cap = cap
        self.flow = flow

    def __str__(self):
        return '(to: {}, from: {}, cap: {}, flow: {})'.format(self.x, self.y, self.cap, self.flow)

    def __repr__(self):
        return self.__str__()


class DinicFlow:
    inf = 10 ** 18

    def __init__(self, v: int):
        self.n = v
        self.cur = [0] * (v + 1)
        self.d = [0] * (v + 1)
        self.adj = [[] for _ in range(v + 1)]
        self.source = self.sink = 0
        self.e = []
        self.vis = []
        self.s = []
        self.t = []

    def addEdge(self, fr: int, to: int, cap: int) -> None:
        # print('called addEdge()')
        e1 = Edge(fr, to, cap, 0)
        e2 = Edge(to, fr, 0, 0)
        self.adj[fr].append(len(self.e))
        self.e.append(e1)
        self.adj[to].append(len(self.e))
        self.e.append(e2)

    def bfs(self):
        # print('called bfs()')

        q = deque()
        self.d[:] = [-1] * (self.n + 1)
        q.append(self.source)
        self.d[self.source] = 0
        while q and self.d[self.sink] < 0:
            x = q.popleft()
            for i in range(len(self.adj[x])):
                ID = self.adj[x][i]
                y = self.e[ID].y
                # print(self.adj)
                if self.d[y] < 0 and self.e[ID].flow < self.e[ID].cap:
                    q.append(y)
                    self.d[y] = self.d[x] + 1
        return self.d[self.sink] >= 0

    def dfs(self, x: int, flow: int) -> int:
        # print('called dfs()')

        if not flow:
            return 0
        if x == self.sink:
            return flow
        for i in range(self.cur[x], len(self.adj[x])):
            ID = self.adj[x][self.cur[x]]
            y = self.e[ID].y
            self.cur[x] += 1
            if self.d[x] + 1 != self.d[y]:
                continue
            pushed = self.dfs(y, min(flow, self.e[ID].cap - self.e[ID].flow))
            if pushed:
                self.e[ID].flow += pushed
                self.e[ID ^ 1].flow -= pushed
                return pushed
        return 0

    def maxFlow(self, src: int, snk: int) -> int:
        # print('called maxFlow()')

        self.source = src
        self.sink = snk
        flow = 0
        while self.bfs():
            self.cur[:] = [0] * (self.n + 1)
            pushed = self.dfs(self.source, self.inf)
            while pushed:
                flow += pushed
                pushed = self.dfs(self.source, self.inf)
        return flow

    def dfs2(self, m: int) -> None:
        # print('called dfs2()')

        self.vis[m] = True
        for i in self.adj[m]:
            if self.e[i].flow < self.e[i].cap and not self.vis[self.e[i].y]:
                self.dfs2(self.e[i])

    def minCut(self) -> None:
        # print('called minCut()')

        self.vis = [False] * self.n
        self.dfs2(self.source)
        for i in range(self.n):
            if i == self.source or i == self.sink:
                continue
            if self.vis[i]:
                self.s.append(i)
            else:
                self.t.append(i)


def func():
    n, t, x = intArr()
    N = max(n, t)
    obj = DinicFlow(2 * N + 3)
    src, snk = 2 * N + 1, 2 * N + 2
    for i in range(1, N + 1):
        obj.addEdge(src, i, 1)
        obj.addEdge(i + N, snk, 1)
    for i in range(1, n + 1):
        p = In()
        for _ in range(p):
            l, r = intArr()
            while r >= l:
                obj.addEdge(i, r + N, 1)
                r -= 1
    return x * obj.maxFlow(src, snk)


def main():
    for _ in range(In()):
        print(func())
    return


if __name__ == '__main__':
    main()
