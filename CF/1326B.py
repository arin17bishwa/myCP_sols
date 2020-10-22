# region smaller_fastio
from sys import stdin, stdout
from os import path

if (path.exists('input.txt')):
    # ------------------Sublime--------------------------------------#
    stdin = open('input.txt', 'r');
    stdout = open('output.txt', 'w');


    def I():
        return (int(input()))


    def In():
        return (map(int, input().split()))
else:
    # ------------------PYPY FAst I/o--------------------------------#
    def I():
        return (int(stdin.readline()))


    def In():
        return (map(int, stdin.readline().split()))


    def S():
        return (stdin.readline().rstrip())


    def Sn():
        return (stdin.readline().split(' '))


# endregion


def func(n, b):
    a = [0] * n
    x = -1
    x = max(x, b[0])
    a[0] = b[0]
    for i in range(1, n):
        x = max(x, a[i - 1])
        a[i] = x + b[i]
    return a


if __name__ == '__main__':
    st = ''
    n = I()
    l = list(In())
    ans = func(n, l)
    print(*ans)
