from math import ceil

# region smaller_fastio
from sys import stdin, stdout


def I():
    return int(stdin.readline())


def In():
    return map(int, stdin.readline().split())


def S():
    return stdin.readline().rstrip()


def Sn():
    return stdin.readline().split(" ")


def Out(whatever):
    return stdout.write(whatever)


# endregion


def func(n, k, arr):
    not_risky = len([i for i in arr if 10 <= i <= 79])
    return ceil(not_risky / k) + ceil((n - not_risky) / k)


if __name__ == "__main__":
    t = I()
    answers = [" "] * t
    for i in range(t):
        size, d = In()
        ar = list(In())
        answers[i] = str(func(size, d, ar))
    Out("\n".join(answers))
