import math

st = ''


def func(l1, l2, m):
    l = [0 for _ in range(m)]
    l3 = [0 for _ in range(m)]
    n = len(l1)
    for i in range(n):
        l[l1[i] - 1] += l2[i]
        l3[l1[i] - 1] += 1
        # print(i,' , ',l )
    k = 1000000001
    for i in range(m):
        if l3[i] != 0:
            k = min(k, l[i])
    return k


for _ in range(int(input())):
    n, m = map(int, input().split())
    # n = int(input()
    # s=input()
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    # l1=input().split()
    # l2=input().split()
    st += str(func(l1, l2, m)) + '\n'

print(st)
