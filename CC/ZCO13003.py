from bisect import bisect_left, bisect, bisect_right


def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    return i - 1
    # raise ValueError


def f(n, k, l):
    alt = [0] * 1000001
    for i in l:
        alt[i] += 1
    ans = 0
    for i in range(1, 1000001):
        alt[i] += alt[i - 1]
    for i in range(n):  # while i<n :
        p = k - l[i] - 1
        if p < 0:
            continue
        c = alt[p]
        if p >= l[i]:
            c -= 1
        ans += max(0, c)
    return ans // 2


def main():
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    print(f(n, k, l))


main()
