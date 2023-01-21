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
    ans = []
    s = str(n)
    l = len(s)
    for j in range(l):
        if s[j] == '0':
            continue
        ans.append(str(int(s[j]) * pow(10, l - 1 - j)))
    return '\n'.join((str(len(ans)), ' '.join(ans)))

    pass


if __name__ == '__main__':
    t = I()
    answers = [' '] * t
    for i in range(t):
        num = I()
        answers[i] = func(num)
    Out('\n'.join(answers))
