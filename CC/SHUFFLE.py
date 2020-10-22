import math

st = ''


def func(n, k, l1):
    l2 = sorted(l1)
    for i in range(n):
        p = l2[i]
        x = 0
        f = 1
        while i + x * k < n:
            if l1[i + x * k] == l2[i]:
                f = 0
                l1[i + x * k], l1[i] = l1[i], l1[i + x * k]
                break
            x += 1
        if f:
            return 'no'
    return 'yes'


for _ in range(int(input())):
    # d={0:1000,1:1000}
    n, k = map(int, input().split())
    l1 = list(map(int, input().split()))
    # l2=list(map(int,input().split()))
    st = st + str(func(n, k, l1)) + '\n'
print(st)
