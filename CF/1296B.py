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

def func(initial):
    p = initial
    while initial > 0:
        p += initial // 10
        mod = 0
        if initial > 9:
            mod = initial % 10
        initial = initial // 10 + mod

    return p


if __name__ == '__main__':
    st = ''
    for _ in range(I()):
        n = I()
        ans = str(func(n))
        st = '\n'.join((st, ans))
    print(st.lstrip())
