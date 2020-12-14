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


def func(n, s):
    options = {0: 'NO', 1: 'YES'}
    try:
        ind = s.index('8')
    except ValueError:
        return options[0]
    if n - 1 - ind > 9:
        return options[1]
    return options[0]


if __name__ == '__main__':
    t = I()
    answers = ['   '] * t
    for i in range(t):
        size = I()
        st = S()
        answers[i] = func(size, st)
    Out('\n'.join(answers))
