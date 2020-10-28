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
from collections import Counter

if __name__ == '__main__':
    n = I()
    sizes = Counter(In())
    ans = 0
    for _ in range(I()):
        a, b = In()
        p = sizes.get(a)
        if p:
            ans += b
            sizes[a] -= 1
    print(ans)
