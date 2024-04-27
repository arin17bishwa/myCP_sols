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


def func():
    global dp, bt
    n = In()
    arr = list(intArr())
    ans = bt = 0
    while (1 << bt) < n:
        bt += 1
    dp = [[0] * (bt + 1) for _ in range(1 << bt)]

    for i in range(1 << bt):
        dp[i][0] = arr[i] if i < n else 0

    for j in range(1, bt + 1):
        for i in range(1 << bt):
            dp[i][j] += dp[i][j - 1]
            if i & (1 << (j - 1)):
                dp[i][j] += dp[i ^ (1 << (j - 1))][j]
    answers = []
    for _ in range(In()):
        l, r, x = intArr()
        x = (x + ans) % (1 << bt)
        ans = solve(r, x) - (solve(l - 1, x) if l > 0 else 0)
        answers.append(str(ans))
    return answers


def solve(left: int, x: int) -> int:
    if x <= left:
        return dp[x][bt]
    ans = 0
    for i in range(bt - 1, -1, -1):
        if x & (1 << i):
            if (left & (1 << i)) == 0:
                x ^= 1 << i
            else:
                ans += dp[x ^ (1 << i)][i]
        if x <= left:
            ans += dp[x][i]
            break
    return ans


def main():
    for _ in range(In()):
        print(*func(), sep="\n")
    return


if __name__ == "__main__":
    dp = []
    bt = 0
    main()
