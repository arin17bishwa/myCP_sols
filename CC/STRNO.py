import math


def Prime_factorization(n):  # with count of powers of each variable
    l = []
    i = 2
    c = 0
    while n & 1 == 0:
        n = n >> 1
        c += 1
    if c != 0:
        l.append([i, c])
    q = int(math.sqrt(n))
    i = 3
    while i <= q + 1:
        c = 0
        while n % i == 0:
            n = n // i
            c += 1
        if c:
            l.append([i, c])
        i += 1
    if n != 1:
        l.append([n, 1])
    return l


st = ""


def func(x, k):
    if x < k:
        return 0
    l = Prime_factorization(x)
    p = 0
    for i in l:
        p += i[1]
    if k > p:
        return 0
    return 1


for _ in range(int(input())):
    x, k = map(int, input().split())
    print(func(x, k))
