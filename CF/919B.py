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

def func(n):
    ans = 0
    while n > 0:
        ans += n % 10
        n //= 10
    return ans


if __name__ == '__main__':
    k = I()-1
    answer = 19
    while k:
        answer += 9
        if func(answer) == 10:
            k -= 1
    Out(str(answer))
