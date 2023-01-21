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

def func(left, right):
    if right < 2 * left:
        return right
    return -1


if __name__ == '__main__':
    st = ''
    q = I()
    answers = [' ' * 6] * q
    for i in range(q):
        l, r = In()
        answers[i] = str(func(l, r))
    stdout.write('\n'.join(answers))
