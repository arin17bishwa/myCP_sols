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


def func(s):
    answer = 0
    d = {
        '(': [],
        ')': [],
        '[': [],
        ']': []
    }
    n = len(s)
    for i in range(n):
        x = s[i]
        d[x].append(i)
    m, n = len(d['(']), len(d[')'])
    i = j = 0
    while i < m and j < n:
        p, q = d['('][i], d[')'][j]
        if p < q:
            answer += 1
            i += 1
            j += 1
        else:
            j += 1

    m, n = len(d['[']), len(d[']'])
    i = j = 0
    while i < m and j < n:
        p, q = d['['][i], d[']'][j]
        if p < q:
            answer += 1
            i += 1
            j += 1
        else:
            j += 1
    return answer


if __name__ == '__main__':
    t = I()
    ans = ['  '] * t
    for i in range(t):
        st = S()
        ans[i] = str(func(st))
    Out('\n'.join(ans))
