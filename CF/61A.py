a=input()
n=len(a)
a=int(a,2)
b=int(input(),2)
ans=bin(a^b).split('b')[1]
print('0'*(n-len(ans))+ans)