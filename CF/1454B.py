from collections import Counter
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
    co = Counter(l)
    ans = -1
    p = [item for item in co.items() if item[1] == 1]
    if len(p) != 0:
        ans = l.index(min(p)[0])+1
    return ans



if __name__ == '__main__':
    t = I()
    answers = ['  '] * t
    for i in range(t):
        n = I()
        arr = list(In())
        answers[i] = str(func(n, arr))
    Out('\n'.join(answers))
