n,m=map(int,input().split())
l=list(map(int,input().split()))
d={}
for i in range(n-1,-1,-1):
    if l[i] in d:
        l[i]=0
    else:
        d[l[i]]=0
        l[i]=1
for i in range(1,n):
    l[i]+=l[i-1]
l.insert(0,0)
for _ in range(m):
    i=int(input())
    print(l[-1]-l[i-1])