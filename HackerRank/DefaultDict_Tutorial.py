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

# endregion
from collections import defaultdict

if __name__ == '__main__':
    n, m = In()
    d1 = defaultdict(list)
    for i in range(1, n + 1):
        x = S()
        d1[x].append(str(i))
    st = ''
    for _ in range(m):
        x = S()
        p = d1.get(x, ('-1',))
        st = '\n'.join((st, ' '.join(p)))
    stdout.write(st.lstrip())
