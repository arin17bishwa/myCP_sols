s=input()
f=1
for i in s:
    if i=='H' or i=='Q' or i=='9':
        print('YES')
        f=0
        break
if f:
    print("NO")