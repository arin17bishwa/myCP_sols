import sys

sys.stdin = open('/home/bishwajit/HDD/PycharmPro/myCP_sols/in.txt', 'r')


def In():
    return int(input())


def intArr(sep=' '):
    return map(int, input().strip().split(sep))


def func():
    n = In()
    arr = list(intArr())
    l1 = sorted(arr)
    return sum(i != j for i, j in zip(arr, l1) or [0])


def main():
    for _ in range(In()):
        print(func())


if __name__ == '__main__':
    main()
