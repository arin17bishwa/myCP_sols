from math import sqrt
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


def func(n, k):
    if k >= n:
        return 1
    x = int(sqrt(n))
    high = min(x + 1, k)
    ans = n
    for i in range(high, 0, -1):
        if n % i == 0:
            p = n // i
            if p <= k:
                ans = min(ans, p, i)
            ans = min(ans, p)
    return ans


if __name__ == '__main__':
    t = I()
    ans = ['  '] * t
    for i in range(t):
        n, k = In()
        ans[i] = str(func(n, k))
    Out('\n'.join(ans))
