st = ''


def func(n, l1):
    m = max(l1)
    mid = n // 2
    l = []
    for i in range(n):
        if l1[i] == m:
            l.append(i)
    last = n - 1 - l[-1]
    if last == 0:
        return 0
    first = mid - l[0]
    # print(first,last)
    p = (last - first + 1)
    return (max(0, p))


for _ in range(int(input())):
    # n,name=map(str,input().split())
    n = int(input())
    # l1=[]
    # inp=input().split()
    # s=input()
    l1 = list(map(int, input().split()))
    # l2 = list(map(int, input().split()))
    # l1=input().split()
    # l2=input().split()
    st += str(func(n, l1)) + '\n'

print(st)
