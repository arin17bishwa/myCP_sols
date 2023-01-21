n,m=map(int,input().split())
l1=[]
l=[]
for i in range(m):
    a,b=map(str,input().split())
    l.extend([a,b])
s=input().split()
ans=''
for i in range(n):
    word = s[i]
    ind=l.index(word)
    if ind&1==0:
        other=l[ind+1]
    else:
        other=l[ind-1]
    if len(word)<=len(other):
        l1.append(word)
    else:
        l1.append(other)
print(*l1)