st = ""
from sys import setrecursionlimit

setrecursionlimit(10**6)

global k


def transformer(i):
    if i == "x":
        return 0
    return 1


def func(l):
    n = len(l)
    j = n - 1
    i = c1 = c2 = 0
    while i < n - 1:
        if l[i] == l[i + 1]:
            i += 1
            continue
        else:
            c1 += 1
            i += 2
    while j > 0:
        if l[j] == l[j - 1]:
            j -= 1
        else:
            c2 += 1
            j -= 2
    return max(c1, c2)


for _ in range(int(input())):
    # n,k=map(int,input().split())
    # n = int(input())
    # inp=input().split()
    # s=input()
    l1 = list(map(transformer, input()))
    # l=[]
    # l1=list(map(int,input().split()))
    # l2 = list(map(int, input().split()))
    # l1=input().split()
    # l2=input().split()
    # func(l1,n,m)
    # print(func(a,b))
    st += str(func(l1)) + "\n"
print(st)
