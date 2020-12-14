# region smaller_fastio
from sys import stdin, stdout


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


def func(n, k):
    arr = [(i + 1) * (pow(-1, i % 2)) for i in range(n)]
    neg = n >> 1
    q = n - k
    i = n - 1
    if neg < q:
        while i > -1 and neg != q:
            if arr[i] > 0:
                arr[i] = -arr[i]
                neg += 1
            i -= 1
    elif neg > q:
        while i > -1 and neg != q:
            if arr[i] < 0:
                arr[i] = -arr[i]
                neg -= 1
            i -= 1

    return ' '.join(map(str, arr))


if __name__ == '__main__':
    t = I()
    answers = [' '] * t
    for i in range(t):
        m, x = In()
        answers[i] = str(func(m, x))
    print('\n'.join(answers))
