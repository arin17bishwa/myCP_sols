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


def func(arr):
    k = max(arr)
    n = len(arr)
    for j in range(n):
        if arr[j] == k:
            if j > 0:
                if arr[j] > arr[j - 1]:
                    return j + 1
            if j < n - 1:
                if arr[j] > arr[j + 1]:
                    return j + 1
    return -1


if __name__ == '__main__':
    q = I()
    answers = ['     '] * q
    for i in range(q):
        n = I()
        l = list(In())
        answers[i] = str(func(l))
    Out('\n'.join(answers))
