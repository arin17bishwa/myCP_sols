l=list(map(int,input().split()))
s=sum(l)
if s%5!=0 or s==0:
    print(-1)
else:
    print(s//5)