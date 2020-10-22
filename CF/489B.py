n=int(input())
lb=list(map(int,input().split()))
m=int(input())
lg=list(map(int,input().split()))
lb.sort()
lg.sort()
ans=0
for i in range(n):
    for j in range(m):
        #if lg[j]-lb[i]>1:
         #   break
        if abs(lg[j]-lb[i])<2:
            lg[j]=200
            ans+=1
            break
print(ans)