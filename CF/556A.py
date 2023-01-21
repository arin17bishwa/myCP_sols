n=int(input())
s=input()
one=s.count('1')
print(n-2*min(one,n-one))