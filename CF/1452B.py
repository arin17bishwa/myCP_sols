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


def func(n, l):
    s = sum(l)
    m = max(l)
    k = max(m, (s + n - 2) // (n - 1))
    return k * (n - 1) - s


if __name__ == '__main__':
    t = I()
    ans = ['  '] * t
    for i in range(t):
        size = I()
        arr = list(In())
        ans[i] = str(func(size, arr))
    Out('\n'.join(ans))
