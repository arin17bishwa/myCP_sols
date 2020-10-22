k=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
for i in range(1,12):
    l[i]+=l[i-1]
if k>l[-1]:
    print(-1)
elif k==0:
    print(0)
else:
    for i in range(12):
        if l[i]>=k:
            print(i+1)
            break