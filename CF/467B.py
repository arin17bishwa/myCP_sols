def format(a):
    a = bin(int(a)).split('b')[1]
    a = '0' * (n - len(a)) + a
    return a

n,m,k=map(int,input().split())
l=[]
c=s=0
for _ in range(m):
    a=format(input())
    l.append(a)
fed=format(input())
for i in l:
    c=0
    for j in range(n):
        if fed[j]!=i[j]:
            c+=1
            if c>k:
                break
    if c<=k:
        s+=1
print(s)