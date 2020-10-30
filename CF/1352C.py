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


if __name__ == '__main__':
    q = I()
    answers = ['         '] * q
    for i in range(q):
        n, k = In()
        answers[i] = str(k + (k - 1) // (n - 1))
    stdout.write('\n'.join(answers))
