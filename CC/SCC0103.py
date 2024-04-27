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

    def S():
        return stdin.readline().rstrip()

    def Sn():
        return stdin.readline().split(" ")


def Out(whatever):
    return stdout.write(whatever)


# endregion


if __name__ == "__main__":
    q = I()
    answers = ["   "] * q
    for i in range(q):
        n = I()
        l1 = [0] * (24 * 60 + 1)
        for _ in range(n):
            h, m = In()
            l1[60 * h + m] += 1
        answers[i] = str(max(l1))
    Out("\n".join(answers))
