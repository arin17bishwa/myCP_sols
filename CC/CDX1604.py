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


def func(arr: list):
    arr.sort()
    n = len(arr)
    ans = 0
    for i in range(1, n + 1):
        ans += abs(arr[i - 1] - i)
    return ans


if __name__ == "__main__":
    t = I()
    answers = [" "] * t
    for i in range(t):
        n = I()
        arr = list(In())
        answers[i] = str(func(arr))
    print("\n".join(answers))
