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


def moveSide(lefty=1):
    global arr
    n = len(arr)
    for i in range(n):
        l1 = []
        for j in range(n):
            if arr[i][j] != 0:
                l1.append(arr[i][j])
        if len(l1) < n:
            if lefty:
                l1 = l1 + [0] * (n - len(l1))
            else:
                l1 = [0] * (n - len(l1)) + l1
        arr[i] = l1.copy()


def right():
    global arr
    n = len(arr)
    i = 0
    moveSide(lefty=0)
    while i < n:
        j = n - 1
        while j > 0:
            if arr[i][j] == arr[i][j - 1]:
                arr[i][j] <<= 1
                arr[i][j - 1] = 0
                j -= 1
            j -= 1
        i += 1
    moveSide(lefty=0)


def left():
    global arr
    n = len(arr)
    moveSide(lefty=1)
    for i in range(n):
        j = 1
        while j < n:
            if arr[i][j - 1] == arr[i][j]:
                arr[i][j - 1] <<= 1
                arr[i][j] = 0
                j += 1
            j += 1
    moveSide(lefty=1)


def moveVert(upp=1):
    global arr
    n = len(arr)
    for j in range(n):
        l1 = []
        for i in range(n):
            if arr[i][j]:
                l1.append(arr[i][j])
        if len(l1) < n:
            if upp == 0:
                l1 = [0] * (n - len(l1)) + l1
            else:
                l1 = l1 + [0] * (n - len(l1))
        for i in range(n):
            arr[i][j] = l1[i]


def up():
    global arr
    n = len(arr)
    moveVert(upp=1)
    for j in range(n):
        i = 1
        while i < n:
            if arr[i][j] == arr[i - 1][j]:
                arr[i - 1][j] <<= 1
                arr[i][j] = 0
                i += 1
            i += 1
    moveVert(upp=1)


def down():
    global arr
    n = len(arr)
    moveVert(upp=0)
    for j in range(n):
        i = n - 1
        while i > 0:
            if arr[i][j] == arr[i - 1][j]:
                arr[i][j] <<= 1
                arr[i - 1][j] = 0
                i -= 1
            i -= 1
    moveVert(upp=0)


def func(direction):
    global arr
    functions = {'right': right, 'left': left, 'up': up, 'down': down}
    functions[direction]()
    return '\n'.join([' '.join(map(str, i)) for i in arr])


def main():
    global arr
    for i in range(In()):
        n, direction = input().split()
        n = int(n)
        arr = [list(intArr()) for _ in range(n)]
        print('Case #{}:\n{}'.format(i + 1, func(direction)))
    return


if __name__ == '__main__':
    arr = []
    main()
