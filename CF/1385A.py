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
    ar.sort()
    if ar[1] != ar[2]:
        return 'NO'
    return '\n'.join(('YES', ' '.join((str(ar[0]), str(ar[0]), str(ar[2])))))


if __name__ == '__main__':
    n = I()
    answers = [' '] * n
    for i in range(n):
        arr = list(In())
        answers[i] = func(arr)
    Out('\n'.join(answers))
