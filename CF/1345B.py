from sys import setrecursionlimit
# region bisection methods
from bisect import bisect_right, bisect_left


def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError


def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i - 1]
    raise ValueError


def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i - 1]
    raise ValueError


def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


# endregion

# region smaller_fastio
from sys import stdin, stdout
from os import path

if path.exists('input.txt'):
    # ------------------Sublime--------------------------------------#
    stdin = open('input.txt', 'r')
    stdout = open('output.txt', 'w')


    def I():
        return int(input())


    def In():
        return map(int, input().split())
else:
    # ------------------PYPY FAst I/o--------------------------------#
    def I():
        return int(stdin.readline())


    def In():
        return map(int, stdin.readline().split())


    def S():
        return stdin.readline().rstrip()


    def Sn():
        return stdin.readline().split(' ')


def Out(whatever):
    return stdout.write(whatever)


# endregion

setrecursionlimit(10 ** 6)
dp = {0: 0, 1: 2}

HIGH = 25820


def req(h):
    global dp
    if h in dp:
        return dp[h]
    x = req(h - 1) + h - 1 + (h << 1)
    dp[h] = x
    return x


def func(n):
    global arr
    ans = 0
    while n > 1:
        p = find_le(arr, n)
        ans += 1
        n -= p

    return ans


if __name__ == '__main__':
    arr = [req(i) for i in range(HIGH + 1)]
    t = I()
    ans = ['   '] * t
    for i in range(t):
        n = I()
        ans[i] = str(func(n))
    Out('\n'.join(ans))
