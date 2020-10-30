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
import string

if __name__ == '__main__':
    n, k = In()
    answer = ['']
    s = string.ascii_lowercase
    answer[0] = s[:k]
    answer.extend(['ab' for _ in range((n - k) // 2)])
    if (n - k) & 1:
        answer.append('a')
    Out(''.join(answer))
