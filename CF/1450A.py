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
    t = I()
    answers = ['  '] * t
    for i in range(t):
        size = I()
        st = S()
        answers[i] = ''.join(sorted(list(st)))
    Out('\n'.join(answers))
