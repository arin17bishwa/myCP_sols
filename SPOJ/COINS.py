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


def func(n, dp):
    if n in dp:
        return dp[n]
    dp[n] = max(n, (func(n // 2, dp) + func(n // 3, dp) + func(n // 4, dp)))
    return dp[n]


if __name__ == '__main__':
    dp = {0: 0, 1: 1}
    answers = []
    for i in range(10):
        try:
            n = I()
            answers.append(str(func(n, dp)))
        except Exception:
            break
    Out('\n'.join(answers))
