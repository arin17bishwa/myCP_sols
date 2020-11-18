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


def func(m, s):
    if s == 0 and m == 1:
        return '{} {}'.format('0', '0')
    if s == 0 or s > 9 * m:
        return '-1 -1'

    high = []
    low = []
    q = s
    while len(high) < m:
        if s > 9:
            high.append('9')
            s -= 9
        else:
            high.append(str(s))
            s = 0
    if high[-1] != '0':
        low = high[::-1]
    elif m == 1:
        low = high[:]
    else:
        s = q
        rem = s - 1
        if rem % 9 != 0:
            low.append(str(rem % 9))
        low.extend(['9'] * (rem // 9))
        if len(low) < m - 1:
            low.extend(['0'] * (m - 1 - len(low)))
        low.sort()
        low.insert(0, '1')

    return "{} {}".format(''.join(low), ''.join(high))


if __name__ == '__main__':
    m, s = In()
    Out(func(m, s))
