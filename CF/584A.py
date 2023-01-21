n,t=map(int,input().split())
s=str(t)
if len(s)>n:
    print(-1)
else:
    s=s+'0'*(n-len(s))
    print(s)