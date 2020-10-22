# region smaller_fastio
from sys import stdin, stdout
from os import path

if (path.exists('input.txt')):
    # ------------------Sublime--------------------------------------#
    stdin = open('input.txt', 'r');
    stdout = open('output.txt', 'w');


    def I():
        return (int(input()))


    def In():
        return (map(int, input().split()))
else:
    # ------------------PYPY FAst I/o--------------------------------#
    def I():
        return (int(stdin.readline()))


    def In():
        return (map(int, stdin.readline().split()))


    def S():
        return (stdin.readline().rstrip())


    def Sn():
        return (stdin.readline().split(' '))


# endregion

def func(l):
    n = len(l)
    k = l[0] % 2
    for i in l:
        if i % 2 != k:
            return 'NO'
    return 'YES'


if __name__ == '__main__':
    st = ''
    for _ in range(I()):
        n = I()
        l = list(In())
        ans = str(func(l))
        st = '\n'.join((st, ans))
    print(st.lstrip())
