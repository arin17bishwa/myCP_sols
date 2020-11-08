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


def func(arr):
    d = {}
    n = len(arr)
    for i in range(n):
        d[arr[i]] = None
    return ' '.join(map(str, d.keys()))


if __name__ == '__main__':
    t = I()
    answers = ['      '] * t
    for i in range(t):
        n = I()
        ar = list(In())
        answers[i] = func(ar)
    Out('\n'.join(answers).lstrip())
