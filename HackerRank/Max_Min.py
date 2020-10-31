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


if __name__ == '__main__':
    n = I()
    k = I()
    arr = [10000] * n
    for i in range(n):
        arr[i] = I()
    arr.sort()
    ma = float('inf')
    for i in range(n - k + 1):
        ma = min(ma, arr[i + k - 1] - arr[i])
    Out(str(ma))
