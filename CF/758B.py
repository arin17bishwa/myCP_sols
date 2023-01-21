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


def func(s):
    n = len(s)
    x = [0] * 4
    patt = [''] * 4
    for i in range(4):
        for j in range(i, n, 4):
            if s[j] == '!':
                x[i] += 1
            else:
                patt[i] = s[j]
    ans = {patt[i]: x[i] for i in range(4)}
    return '{} {} {} {}'.format(ans['R'], ans['B'], ans['Y'], ans['G'])


if __name__ == '__main__':
    s = S()
    Out(func(s))
