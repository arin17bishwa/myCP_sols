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
    k, a, b, x, y = int_arr()

    type1 = doable(k, a, x)
    type2 = doable(k - type1 * x, b, y)
    try1 = type1 + type2

    type2 = doable(k, b, y)
    type1 = doable(k - type2 * y, a, x)
    try2 = type1 + type2

    return max(try1, try2)


def doable(current_temp: int, required_temp: int, drop_temp: int) -> int:
    if required_temp > current_temp:
        return 0

    return 1 + ((current_temp - required_temp) // drop_temp)


def main():
    for _ in range(iin()):
        print(func())


if __name__ == "__main__":
    main()
