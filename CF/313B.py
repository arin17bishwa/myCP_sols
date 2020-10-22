s=input()
n=len(s)
l=[0]
for i in range(0,n-1):
    if s[i]==s[i+1]:
        l.append(1)
    else:
        l.append(0)
q=int(input())
for i in range(1,n):
    l[i]+=l[i-1]
for _ in range(q):
    low,r=map(int,input().split())
    print(l[r-1]-l[low-1])