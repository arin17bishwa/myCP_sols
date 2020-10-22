n,t=map(int,input().split())
s=input()
l=list(s)
f=0
for j in range(t):
    if f:
        break
    f=1
    i=0
    while i<(n-1):
        if l[i]=='B' and l[i+1]=='G':
            #print('swapping:',i,i+1)
            f=0
            l[i]='G'
            l[i+1]='B'
            #print(*l)
            i+=1
        i+=1
    #print(*l)
for i in l:
    print(i,end='')