def transformer(p):
    return(int(p)%2)
n=int(input())
#l1=list(map(int,))
l=list(map(transformer,input().split()))
z=l[:3].count(0)
one=3-z
if z>one:
    print(l.index(1)+1)
else:
    print(l.index(0)+1)