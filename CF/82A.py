from time import time
n=int(input())
t1=time()
d={'S':'Sheldon','L':'Leonard','P':'Penny','R':'Rajesh','H':'Howard'}
s='SLPRH'
i=0
while len(s)<=n:
    s=s+s[i]*2
    i+=1
t2=time()
print(d[s[n-1]])
print(t2-t1)