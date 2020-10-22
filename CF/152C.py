modulo=pow(10,9)+7
def modularExponentiation(x,n):
    result=1
    while n>0:
        if n&1:
            result=(result*x)%modulo
        x=(x*x)%modulo
        n=n//2
    return result

n,m=map(int,input().split())
print(modularExponentiation(m+1,n-1))