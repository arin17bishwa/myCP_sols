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
    letter_case: str = "title"

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
    rt, ct, ra, ca = int_arr()
    n, m, l = int_arr()

    s_moves = []
    for _ in range(m):
        ch, cnt = input().split()
        s_moves.append((ch, int(cnt)))

    t_moves = []
    for _ in range(l):
        ch, cnt = input().split()
        t_moves.append((ch, int(cnt)))

    return count_meetings(rt, ct, ra, ca, s_moves, t_moves)


def count_meetings(Rt, Ct, Ra, Ca, S_runs, T_runs):
    mv = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    pr = Rt - Ra
    pc = Ct - Ca

    i = j = 0
    rem_s = S_runs[0][1] if S_runs else 0
    rem_t = T_runs[0][1] if T_runs else 0
    ans = 0

    while i < len(S_runs) and j < len(T_runs):
        s_dir, _ = S_runs[i]
        t_dir, _ = T_runs[j]
        vsr, vsc = mv[s_dir]
        vtr, vtc = mv[t_dir]

        k = min(rem_s, rem_t)

        dr = vsr - vtr
        dc = vsc - vtc

        if dr == 0 and dc == 0:
            if pr == 0 and pc == 0:
                ans += k
        else:
            t_candidate = None

            if dr == 0:
                if pr == 0 and dc != 0:
                    num = -pc
                    if num % dc == 0:
                        t = num // dc
                        if 1 <= t <= k:
                            t_candidate = t
            elif dc == 0:
                if pc == 0 and dr != 0:
                    num = -pr
                    if num % dr == 0:
                        t = num // dr
                        if 1 <= t <= k:
                            t_candidate = t
            else:
                num_r, den_r = -pr, dr
                num_c, den_c = -pc, dc
                if num_r % den_r == 0 and num_c % den_c == 0:
                    t1 = num_r // den_r
                    t2 = num_c // den_c
                    if t1 == t2 and 1 <= t1 <= k:
                        t_candidate = t1

            if t_candidate is not None:
                ans += 1

        pr += k * dr
        pc += k * dc

        rem_s -= k
        rem_t -= k
        if rem_s == 0:
            i += 1
            if i < len(S_runs):
                rem_s = S_runs[i][1]
        if rem_t == 0:
            j += 1
            if j < len(T_runs):
                rem_t = T_runs[j][1]

    return ans


def main():
    for _ in range(1):
        print(func())


if __name__ == "__main__":
    main()
