n,t=map(int,input().split())
l=(list(map(int,input().split())))
l.insert(0,0)
for i in range(1,n+1):
    l[i]+=l[i-1]
end=1
start=m=0
while start<n:
    end=min(end,n)
    while end<n+1 and (l[end]-l[start])<=t:
        m=max(m,end-start)
        end+=1
    start+=1
print(m)