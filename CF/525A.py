import string
# region smaller_fastio
from sys import stdin, stdout


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


if __name__ == '__main__':
    ans = 0
    n = I()
    st = S()
    x = {i: 0 for i in string.ascii_lowercase}
    for i in range(0, (n << 1) - 2, 2):
        key = st[i]
        door = st[i + 1]
        x[key] += 1
        if x[door.lower()] > 0:
            x[door.lower()] -= 1
        else:
            ans += 1

    Out(str(ans))
