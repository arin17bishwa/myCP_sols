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


def func(a, b):
    even1 = a >> 1
    even2 = b >> 1
    odd1 = a - even1
    odd2 = b - even2
    return even1 * even2 + odd1 * odd2


if __name__ == '__main__':
    t = I()
    answer = [' '] * t
    for i in range(t):
        x, y = In()
        answer[i] = str(func(x, y))
    Out('\n'.join(answer))
