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
    d1, v1, d2, v2, p = In()
    for i in range(1, 1001):
        if max(0, i - d1 + 1) * v1 + max(0, i - d2 + 1) * v2 >= p:
            print(i)
            break
