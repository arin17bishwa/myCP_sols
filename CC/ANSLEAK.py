# cook your dish here
# cook your dish here
from random import choice


def func(l1, n, m, k):
    l = []
    for a in range(n):
        i = l1[a]
        l2 = []
        q = max(i)
        lx = [i + 1 for i in range(m)]
        for b in range(m):
            if i[b] == q:
                l2.append(b + 1)
        q = choice(lx)
        l.append(q)
    print(*l)


for _ in range(int(input())):
    n, m, k = map(int, input().split())
    l1 = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        l = list(map(int, input().split()))
        for j in l:
            l1[i][j - 1] += 1
    func(l1, n, m, k)
