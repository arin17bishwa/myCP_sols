from bisect import bisect
from typing import Iterable, Callable
from bisect import bisect_left

# region fast io
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
    def inner1(*args, **kwargs) -> str:
        res = function(*args, **kwargs)
        if res < 0:
            return "NEGATIVE"
        if res > 0:
            return "POSITIVE"
        return "0"

    return inner1


def get_output(inp: int) -> str:
    if inp < 0:
        return "NEGATIVE"
    if inp > 0:
        return "POSITIVE"
    return "0"


def func():
    n, q = int_arr()
    arr = list(int_arr())
    arr.sort()
    for _ in range(q):
        x = iin()
        k = bisect_left(arr, x)
        if k < n and arr[k] == x:
            print(get_output(0))
        else:
            print(get_output(1) if k & 1 == 0 else get_output(-1))
    return


def main():
    for _ in range(1):
        func()


if __name__ == "__main__":
    main()
