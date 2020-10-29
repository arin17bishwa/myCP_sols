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

def func(a):
    s = sum(a)
    if s == 0:
        return 'NO'
    if s > 0:
        a.sort(reverse=True)
        return 'YES\n' + ' '.join(map(str, a))
    a.sort()
    return 'YES\n' + ' '.join(map(str, a))


if __name__ == '__main__':
    t = I()
    answers = [''] * t
    for i in range(t):
        n = I()
        l = list(In())
        answers[i] = func(l)
    stdout.write('\n'.join(answers).rstrip())
