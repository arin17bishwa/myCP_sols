def decider(l):
    for i in l:
        if i=='C' or i=='M' or i=='Y':
            return 1
    return 0
n,m=map(int,input().split())
f=0
for i in range(n):
    if f==1:
        inp=input()
        continue
    p=decider(input().split())
    if p==1:
        f=1
if f:
    print('#Color')
else:
    print('#Black&White')