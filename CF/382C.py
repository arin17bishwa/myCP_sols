def func(n,l1):
    if n==1:
        print(-1)
        return 0
    s=set(l1)
    if len(s)==1:
        print(1)
        print(l1[0])
        return 0
    l1.sort()
    diff=min(l1[-1]-l1[-2],l1[1]-l1[0])
    l = []
    if n == 2:
        if diff==0:
            print(1)
            print(l1[0])
            return 0
        l.append(l1[0]-diff)
        if diff&1==0:
            l.append(l1[0]+diff//2)
        l.append(l1[1]+diff)
        print(len(l))
        print(*l)
        return 0

    for i in range(1,n):
        d=l1[i]-l1[i-1]
        if d<diff:
            print(0)
            return 0
        elif d==diff:
            continue
        else:
            if d==2*diff:
                l.append(l1[i]-diff)
            else:
                print(0)
                return 0
            if len(l)>1:
                print(0)
                return 0
    if len(l)==1:
        print(1)
        print(l[0])
        return 0

    print(2)
    print(l1[0]-diff,l1[-1]+diff)



n=int(input())
l1=list(map(int,input().split()))
(func(n,l1))
