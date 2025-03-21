# region fast io
import os
import sys
from io import BytesIO, IOBase
from math import ceil
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
    n, p = int_arr()
    arr = list(int_arr())
    ans = [float("inf") if arr[i] else 0 for i in range(n)]
    curr_mx = arr[0]
    for i in range(arr.index(0), n):
        curr = arr[i]
        if curr == 0:
            curr_mx = 0
            continue
        curr_mx = max(curr_mx, curr)
        ans[i] = min(curr_mx, ans[i])
    curr_mx = 0
    last_zero_idx = n - 1
    for last_zero_idx in range(n - 1, -1, -1):
        if arr[last_zero_idx] == 0:
            break
    for i in range(last_zero_idx, -1, -1):
        curr = arr[i]
        if curr == 0:
            curr_mx = 0
            continue
        curr_mx = max(curr_mx, curr)
        ans[i] = min(curr_mx, ans[i])
    return [ceil(i / p) for i in ans]


def main():
    for _ in range(iin()):
        print(*func())


if __name__ == "__main__":
    main()
