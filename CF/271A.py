n=int(input())
i=n+1
while True:
    l = len(set(list(str(i))))
    if l>3:
        print(i)
        break
    i+=1