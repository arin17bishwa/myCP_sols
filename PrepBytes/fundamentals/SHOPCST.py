import sys

sys.stdin = open('/home/bishwajit/HDD/PycharmPro/myCP_sols/in.txt', 'r')


def In():
    return int(input())


def intArr(sep=' '):
    return map(int, input().strip().split(sep))


import heapq


def func(arr: list):
    h = arr
    heapq.heapify(h)
    while len(h) > 1:
        x, y = heapq.heappop(h), heapq.heappop(h)
        heapq.heappush(h, x + y)
    return h[0]


def main():
    for _ in range(1):
        arr = [1, 2, 3]
        print(func(arr))


if __name__ == '__main__':
    main()
