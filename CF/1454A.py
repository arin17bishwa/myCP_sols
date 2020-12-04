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


def func(n):
    l = [n - i for i in range(n)]
    if n & 1:
        p = n >> 1
        l[-1], l[p] = l[p], l[-1]
    return ' '.join(map(str, l))


if __name__ == '__main__':
    t = I()
    answers = ['  '] * t
    for i in range(t):
        n = I()
        answers[i] = func(n)
    Out('\n'.join(answers))
