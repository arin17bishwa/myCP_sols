n=int(input())
a=b=0
s=''
while n>0:
    if n%7==0:
        b+=1
        n-=7
    else:
        a+=1
        n-=4
if n<0:
    print(-1)
else:
    print('4'*a+'7'*b)