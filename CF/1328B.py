st=''
def func(n,k):
    l=list('a'*n)
    s=''
    for i in range(n-1,-1,-1):
        if k<=n-i-1:
            l[i]='b'
            l[n-k]='b'
            for j in l:
                s+=j
            return s
        k-=n-i-1
for _ in range(int(input())):
    n,k=map(int,input().split())
    st+=str(func(n,k))+'\n'
print(st)