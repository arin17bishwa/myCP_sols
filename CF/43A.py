n=int(input())
a=input()
l=[1,0]
b='as'
d={a:1,b:0}
for i in range(n-1):
    s=input()
    if s not in d:
        b=s
        d[s]=1
    elif s==a:
        d[a]+=1
    elif s==b:
        d[b]+=1
if d[a]>d[b]:
    print(a)
else:
    print(b)