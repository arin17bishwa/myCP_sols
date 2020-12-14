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


def func(n, k):
    if k > n:
        return 'NO'
    if (n - (k - 1)) & 1:
        ans = [1] * k
        ans[-1] = n - (k - 1)
        return '\n'.join(('YES', ' '.join(map(str, ans))))
    if ((k - 1) << 1) < n and (n - ((k - 1) << 1)) & 1 == 0:
        ans = [2] * k
        ans[-1] = n - ((k - 1) << 1)
        return '\n'.join(('YES', ' '.join(map(str, ans))))
    return 'NO'


if __name__ == '__main__':
    t = I()
    answers = ['  '] * t
    for i in range(t):
        x, y = In()
        answers[i] = func(x, y)
    Out('\n'.join(answers))
