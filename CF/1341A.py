# #DONE

# region smaller_fastio
from os import path
from sys import stdin, stdout

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

def func(a, b, c, d, n):
    tot_high = c + d
    tot_low = c - d
    low=(a-b)*n
    high=(a+b)*n
    if low>tot_high or high<tot_low:
        return 'No'
    return 'Yes'


def f(grain_low, grain_high, tot_low, tot_high, n):
    if grain_low > grain_high:
        return 'No'
    mid = (grain_low + grain_high) // 2
    k = mid * n
    if k >= tot_low:
        if k <= tot_high:
            return 'Yes'
        else:
            return f(grain_low, mid - 1, tot_low, tot_high, n)
    else:
        return f(mid + 1, grain_high, tot_low, tot_high, n)


if __name__ == '__main__':
    t = I()
    st = ''
    for _ in range(t):
        n, a, b, c, d = In()
        st = '\n'.join((st, func(a, b, c, d, n)))
    stdout.write(st.lstrip())
