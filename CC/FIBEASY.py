def fibb(n):
    l1 = [0, 1]
    c = 2
    while c <= n:
        p = l1[c - 1] + l1[c - 2]
        l1.append(p % 10)
        c = c + 1
    return l1


def count(n):
    p = n
    i = 0
    while p > 1:
        p = p // 2
        i = i + 1
    return i


t = int(input())
l = []
for i in range(t):
    inp = int(input())
    l.append(inp)
n = max(l)
for i in range(t):
    n = l[i]
    c = count(n)
    if c % 4 == 0:
        print(0)
    elif (c - 1) % 4 == 0:
        if c < 3:
            print(1)
        else:
            print(9)
    elif (c - 2) % 4 == 0:
        print(2)
    else:
        print(3)
