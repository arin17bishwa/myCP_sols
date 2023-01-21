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

def func(ar):
    n = len(ar)
    i = n - 1
    while i > 0 and ar[i] <= ar[i - 1]:
        i -= 1
    while i > 0 and ar[i] >= ar[i - 1]:
        i -= 1
    return str(i)


if __name__ == '__main__':
    t = I()
    answers = ['  '] * t
    for i in range(t):
        n = I()
        arr = list(In())
        answers[i] = func(arr)
    Out('\n'.join(answers).lstrip())
