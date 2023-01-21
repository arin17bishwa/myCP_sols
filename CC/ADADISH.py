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
    n = len(arr)
    if n < 3:
        return max(arr)
    arr.sort()
    if n == 3:
        return min(max(arr[0] + arr[1], arr[2]), max(arr[0] + arr[2], arr[1]))
    return min(max(sum(arr[:3]), arr[3]), max(arr[0] + arr[3], arr[1] + arr[2]), max(arr[0] + arr[2], arr[1] + arr[3]))


if __name__ == '__main__':
    t = I()
    ans = ['   '] * t
    for i in range(t):
        n = I()
        arr = list(In())
        ans[i] = str(func(arr))
    Out('\n'.join(ans))
