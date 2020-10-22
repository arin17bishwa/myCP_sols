master='qwertyuiopasdfghjkl;zxcvbnm,./'
c=input()
if c=='R':
    k=-1
else:
    k=1
s=input()
ans=''
for i in s:
    ans+=master[master.index(i)+k]
print(ans)