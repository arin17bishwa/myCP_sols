#DONE

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


def f(n, k, s):
    wins = loss = 0
    win_streak = 0
    lose_streaks = []
    for i in range(n):
        if s[i] == 'W':
            wins += 1
            if i == 0 or s[i - 1] == 'L':
                win_streak += 1
        else:
            loss += 1
            if i == 0 or s[i - 1] == 'W':
                lose_streaks.append(0)
            lose_streaks[-1] += 1
    if k >= loss:
        return 2 * n - 1
    if wins == 0:
        if k == 0:
            return 0
        return 2 * k - 1

    if s[0] == 'L':
        lose_streaks[0] = 1e9
    if s[-1] == 'L':
        lose_streaks[-1] = 1e9
    wins += k
    lose_streaks.sort()
    for i in lose_streaks:
        if i > k:
            break
        k -= i
        win_streak -= 1
    return 2 * wins - win_streak


def func():
    st = ''
    t = I()
    for _ in range(t):
        n, k = In()
        s = input()
        st = '\n'.join((st, str(f(n, k, s))))
    print(st.lstrip())


if __name__ == '__main__':
    func()
