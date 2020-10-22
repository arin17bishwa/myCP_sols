n=int(input())
l1=list(map(int,str(n)))
s=0
for i in range(len(l1)):
    if l1[i]>0:
        l1[i]=1
for i in l1:
    s=s*10+i
print(int(str(s),2))