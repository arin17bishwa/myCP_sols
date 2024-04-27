st = ""
from sys import setrecursionlimit

setrecursionlimit(10**6)


def transformer(i):
    if i == "x":
        return 0
    return 1


def func(n):
    return (n - 1) // ((n & (~(n - 1))) << 1)


for _ in range(int(input())):
    # n,k=map(int,input().split())
    n = int(input())
    # inp=input().split()
    # s=input()
    # l1 = list(map(transformer, input()))
    # l=[]
    # l1 = list(map(int, input().split()))
    # l2 = list(map(int, input().split()))
    # l1=input().split()
    # l2=input().split()
    # func(l1,n,m)
    # print(func(a,b))
    st += str((n - 1) // ((n & (~(n - 1))) << 1)) + "\n"
print(st)
