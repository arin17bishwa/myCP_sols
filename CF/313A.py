# #DONE
# region smaller_fastio
from os import path
from sys import stdin

if (path.exists('input.txt')):
    # ------------------Sublime--------------------------------------#
    stdin = open('input.txt', 'r');
    stdout = open('output.txt', 'w');


    def I():
        return (int(input()))


    def In():
        return (map(int, input().split()))
else:
    # ------------------PYPY FAst I/o--------------------------------#
    def I():
        return (int(stdin.readline()))


    def In():
        return (map(int, stdin.readline().split()))


    def S():
        return (stdin.readline().rstrip())


    def Sn():
        return (stdin.readline().split(' '))


# endregion


def func():
    n = int(input())
    if n >= 0:
        return n
    l = list(str(abs(n)))
    if int(l[-1]) < int(l[-2]):
        return int(''.join(('-', *l[:-2], l[-1])))
    return int(''.join(('-', *l[:-1])))


if __name__ == '__main__':
    print(func())
