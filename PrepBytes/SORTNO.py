import sys

sys.stdin = open('/home/bishwajit/HDD/PycharmPro/myCP_sols/in.txt', 'r')


def In():
    return int(input())


def intArr(sep=' '):
    return map(int, input().strip().split(sep))


def func():
    n = In()
    arr = list(intArr())
    low = mid = 0
    high = n - 1
    while mid <= high:
        x = arr[mid]
        if x == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif x == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:
            mid += 1
    return arr


def main():
    for _ in range(In()):
        print(*func())


if __name__ == '__main__':
    main()
