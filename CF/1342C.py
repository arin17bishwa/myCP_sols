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


def func(s):
    s = ''.join((s, 'R'))
    l = []
    n = len(s)
    for i in range(n):
        if s[i] == 'R':
            l.append(i + 1)
    m = -1
    k = len(l)
    if k == 0:
        return n + 1
    prev = 0
    for i in range(k):
        m = max(m, l[i] - prev)
        prev = l[i]
    return m


if __name__ == '__main__':
    t = I()
    ans = ['  '] * t
    for i in range(t):
        s = S()
        ans[i] = str(func(s))
    Out('\n'.join(ans))
