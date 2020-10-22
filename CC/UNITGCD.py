# cook your dish here
st = ''


def func(n):
    if n < 4:
        l = [i + 1 for i in range(n)]
        print(1)
        print(len(l), *l)
        return 0
    ans = n // 2
    print(ans)
    print(3, 1, 2, 3)
    if n & 1:  # odd
        p = 4
        for _ in range(ans - 1):
            print(2, p, p + 1)
            p += 2
        return 0
    else:  # even
        p = 4
        while p < n:
            print(2, p, p + 1)
            p += 2
        print(1, n)
        return 0


for _ in range(int(input())):
    n = int(input())
    func(n)
