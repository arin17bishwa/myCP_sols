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


# endregion


def func(string):
    if string[-1] in string[:-1]:
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    st = ''
    for _ in range(I()):
        n = I()
        s = S()
        st = '\n'.join((st, func(s)))
    stdout.write(st.lstrip())
