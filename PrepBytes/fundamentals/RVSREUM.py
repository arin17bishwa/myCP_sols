import sys

sys.stdin = open('/home/bishwajit/HDD/PycharmPro/myCP_sols/in.txt', 'r')


def In():
    return int(input())


def intArr(sep=' '):
    return map(int, input().strip().split(sep))


def func():
    n = In()
    ans = 0
    while n:
        ans = ans * 10 + n % 10
        n //= 10
    return ans


def main():
    for _ in range(1):
        print(func())


if __name__ == '__main__':
    main()
