import sys

sys.stdin = open('/home/bishwajit/HDD/PycharmPro/myCP_sols/in.txt', 'r')


def In():
    return int(input())


def intArr(sep=' '):
    return map(int, input().split(sep))


def func():
    n = In()
    if n % 100 == 0:
        if n % 400 == 0:
            return 1
        return 0
    return 0 if n % 4 else 1


def main():
    for _ in range(In()):
        print('Yes' if func() else 'No')


if __name__ == '__main__':
    main()
