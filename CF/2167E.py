# region fast io
import os
import sys
from io import BytesIO, IOBase
from typing import Iterable, Callable

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

    def readline(self, *args, **kwargs) -> bytes:
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


def int_arr() -> Iterable[int]:
    return map(int, input().split())


def iin() -> int:
    return int(input())


def yn_dec(function) -> Callable:
    letter_case: str = "upper"

    def inner1(*args, **kwargs) -> str:
        res = function(*args, **kwargs)
        ans = "yes" if res else "no"
        if letter_case == "upper":
            return ans.upper()
        if letter_case == "title":
            return ans.title()
        if letter_case == "lower":
            return ans.lower()
        return res

    return inner1


def func():
    n, k, x = int_arr()
    arr = sorted(int_arr())

    lo, hi = 0, x
    ans = lo

    while lo <= hi:
        mid = (lo + hi) // 2
        if is_possible(arr, mid, k, x):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    return prepare(arr, ans, x, k)


def is_possible(arr: list[int], r: int, k: int, x: int) -> bool:
    tot = 0
    curr = 0
    for i in arr:
        left = max(0, i - r + 1)
        right = min(x, i + r - 1)
        if curr <= left - 1:
            tot += left - curr
            if tot >= k:
                return True
        curr = max(curr, right + 1)
        if curr > x:
            break
    if curr <= x:
        tot += x - curr + 1
    return tot >= k


def prepare(arr: list[int], r: int, x: int, k: int) -> list[int]:
    ans: list[int] = []
    curr = 0

    for i in arr:
        left = max(0, i - r + 1)
        right = min(x, i + r - 1)
        while curr < left and len(ans) < k:
            ans.append(curr)
            curr += 1
        curr = max(curr, right + 1)
        if curr > x or len(ans) >= k:
            break

    while curr <= x and len(ans) < k:
        ans.append(curr)
        curr += 1
    return ans


def main():
    for _ in range(iin()):
        print(*func())


if __name__ == "__main__":
    main()
