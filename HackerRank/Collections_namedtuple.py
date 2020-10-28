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
from collections import namedtuple


def func():
    """Without using named tuple(under 4 lines)"""
    n = int(input())
    index = input().split().index('MARKS')
    print(sum([int(input().split()[index]) for _ in range(n)]) / n)


if __name__ == '__main__':
    n = I()
    stud = namedtuple('student', input().strip().split())
    print(sum(int(stud(*input().strip().split()).MARKS) for _ in range(n)) / n)
