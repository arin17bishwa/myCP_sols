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
from math import sqrt


def f(n):
    if n & 1 == 0:
        return 2
    lim = int(sqrt(n))
    for i in range(3, lim + 1):
        if n % i == 0:
            return i
    return n


def func(n, k):
    if n & 1 == 0:
        return n + 2 * k
    return n + 2 * (k - 1) + f(n)


if __name__ == '__main__':
    st = ''
    for _ in range(I()):
        n, k = In()
        ans = str(func(n, k))
        st = '\n'.join((st, ans))
    print(st.lstrip())
