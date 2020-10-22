n=int(input())
l,f=[],0
for i in range(n):
    l.append(list(map(int,input().split())))
l.sort()
for i in range(n-1):
    if l[i][0]<l[i+1][0] and l[i][1]>l[i+1][1]:
        f=1
        break
if f:
    print('Happy Alex')
else:
    print('Poor Alex')