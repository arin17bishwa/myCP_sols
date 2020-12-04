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


def func(m, l):
    n = m << 1
    even = []
    odd = []
    for i in range(n):
        if l[i] & 1:
            odd.append(str(i + 1))
        else:
            even.append(str(i + 1))
    p, q = len(even), len(odd)
    if q & 1:
        _ = odd.pop()
        _ = even.pop()
        p -= 1
        q -= 1
    elif p == 0:
        _ = odd.pop()
        _ = odd.pop()
        q -= 2
    else:
        _ = even.pop()
        _ = even.pop()
        p -= 2
    ans = []
    for i in range(0, p - 1, 2):
        ans.append(' '.join((even[i], even[i + 1])))
    for i in range(0, q - 1, 2):
        ans.append(' '.join((odd[i], odd[i + 1])))
    return '\n'.join(ans).rstrip()


if __name__ == '__main__':
    t = I()
    answers = ['  '] * t
    for i in range(t):
        size = I()
        arr = list(In())
        answers[i] = str(func(size, arr))
    Out('\n'.join(answers))
