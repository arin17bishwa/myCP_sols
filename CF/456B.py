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


if __name__ == '__main__':
    s = S()
    n = len(s)
    if n < 2:
        k = int(s)
    else:
        k = int(s[-2:])

    if k % 4 == 0:
        print(4)
    else:
        print(0)
