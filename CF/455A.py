N = pow(10, 5) + 1

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


if __name__ == '__main__':
    n = I()
    arr = list(In())
    counter = [0] * N
    for i in arr:
        counter[i] += 1
    dp = [[0, 0] for _ in range(N)]
    dp[1] = [0, counter[1]]

    for i in range(2, N):
        dp[i][1] = counter[i] * i + max(dp[i - 2])
        dp[i][0] = max(dp[i - 1])

    print(max(dp[N - 1]))
