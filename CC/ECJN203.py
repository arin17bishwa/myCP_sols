# region smaller_fastio
from os import path
from sys import stdin, stdout

if path.exists("input.txt"):
    # ------------------Sublime--------------------------------------#
    stdin = open("input.txt", "r")
    stdout = open("output.txt", "w")

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


# endregion
cout = stdout.write


def func():
    n = I()
    l = []
    for i in range(n):
        x, y = In()
        l.append((y, -x, -(i + 1)))
    l.sort()
    print(" ".join(map(lambda x: str(-x[2]), l)))


if __name__ == "__main__":
    func()
