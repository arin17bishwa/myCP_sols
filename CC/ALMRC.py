"""
FROM https://www.codechef.com/viewsolution/61973024
"""

# region fastio
import os
import sys
from io import BytesIO, IOBase
from sys import setrecursionlimit
from typing import List

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
setrecursionlimit(10**5 + 5)


def intArr():
    return map(int, input().split())


def In():
    return int(input())


def prefill() -> None:
    global factorial
    for i in range(2, 20):
        factorial.append(factorial[-1] * i)


def rec(x: int) -> None:
    global nums
    if x == 18:
        return
    n = nums[-1]
    nums.append(10 * n + 3)
    rec(x + 1)
    nums.append(10 * n + 6)
    rec(x + 1)


def bin_arr(arr: List[int], n: int, off: int = 0) -> int:
    left, right = 0, len(arr) - 1
    ans = 0
    while left <= right:
        mid = (left + right) >> 1
        if arr[mid] > n:
            right = mid - 1
        else:
            ans = mid
            left = mid + 1
    return ans + off


def shift(i: int, j: int) -> None:
    global v
    j += i
    val = v[j]
    for k in range(j, i, -1):
        v[k] = v[k - 1]
    v[i] = val


def check(n: int) -> bool:
    if n == 0:
        return True
    return ((n % 10 == 6) or (n % 10 == 3)) and (check(n // 10))


def func():
    global v
    n, q = intArr()
    N = min(n, 20)
    cnt = 1
    v = list(range(1, N + 1))
    if (n < 20) and (q > factorial[n - 1]):
        return -1
    q -= 1
    ans = bin_arr(nums, n - 20, 0)
    while q:
        ind = bin_arr(factorial, q, 1)
        q0 = q // factorial[ind - 1]
        shift(N - 1 - ind, q0)
        q -= q0 * factorial[ind - 1]
    for i in range(N):
        if (check(n - N + i + 1)) and (check(v[i] + n - N)):
            ans += 1
        cnt += 1
    return ans


def main():
    for _ in range(In()):
        print(func())
    return


if __name__ == "__main__":
    factorial = [1]
    nums = [0]
    v = []
    prefill()
    rec(0)
    nums.sort()
    main()
