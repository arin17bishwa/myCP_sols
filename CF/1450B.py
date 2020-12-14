# region smaller_fastio
from sys import stdin, stdout


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


def dist(a, b, c, d):
    return abs(a - c) + abs(b - d)


def func(n, k, arr):
    if n == 1:
        return 0
    for i in range(n):
        f=1
        for j in range(n):
            if i == j:
                continue
            p = dist(arr[i][0], arr[i][1], arr[j][0], arr[j][1])
            if p > k:
                f=0
                break
        if f:
            return 1
    return -1


if __name__ == '__main__':
    t = I()
    answers = [' '] * t
    for i in range(t):
        n, lim = In()
        arr = [[0, 0] for _ in range(n)]
        for j in range(n):
            arr[j] = list(In())

        answers[i] = str(func(n, lim, arr))

    Out('\n'.join(answers))
