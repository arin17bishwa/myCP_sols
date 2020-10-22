from math import sqrt


def factors(n):
    l1 = []
    if n == 0:
        return l1
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            l1.append(i)
            if n / i != i:
                l1.append(n // i)
    return len(l1)


s = ''

for _ in range(int(input())):
    l1 = [int(i) for i in input().split()]
    a, b = min(l1[0], l1[1]), max(l1[0], l1[1])
    k = factors(b - a)
    if k == 0:
        k = -1
    s += str(k) + '\n'

print(s)
