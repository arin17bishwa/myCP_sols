from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

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
global arr, ans


def merge(l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = arr[l:m + 1]
    R = arr[m + 1:r + 1]
    i = j = k = temp = 0

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[l + k] = L[i]
            i += 1
        else:
            temp += (n1 - i)
            arr[l + k] = R[j]
            j += 1
        k += 1
    for i1 in range(i, n1):
        arr[l + k] = L[i1]
        k += 1
    for j1 in range(j, n2):
        arr[l + k] = R[j1]
        k += 1

    return temp


def invCount(l, r):
    global ans
    if l < r:
        mid = l + (r - l) // 2
        invCount(l, mid)
        invCount(mid + 1, r)
        ans += merge(l, mid, r)
    # print(*arr)
    return ans


if __name__ == '__main__':
    t = I()
    S()
    answers = ['  '] * t
    for i in range(t):
        ans = 0
        n = I()
        arr = [0 for _ in range(n)]
        for j in range(n):
            arr[j] = I()
        S()
        answers[i] = str(invCount(0, n - 1))
    Out('\n'.join(answers).lstrip())
