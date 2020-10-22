# #DONE

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
from math import ceil


def func(a, b, c, d):
    if a <= b:
        return b
    extra = c - d
    if extra < 1:
        return -1
    return b + c * (ceil((a - b) / extra))


if __name__ == '__main__':
    st = ''
    for _ in range(I()):
        a, b, c, d = In()
        ans = str(func(a, b, c, d))
        st = '\n'.join((st, ans))
    print(st.lstrip())
