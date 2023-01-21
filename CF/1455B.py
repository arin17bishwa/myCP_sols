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


def func(n):
    low = 1
    high = 1414
    while low < high:
        mid = ((low + high) // 2)
        k = (mid * (mid + 1)) // 2
        if k >= n:
            high = mid
        else:
            low = mid + 1

    return high - n + (high * (high + 1)) >> 1


if __name__ == '__main__':
    t = I()
    answers = [' '] * t
    for i in range(t):
        x = I()
        answers[i] = str(func(x))
    Out('\n'.join(answers))
