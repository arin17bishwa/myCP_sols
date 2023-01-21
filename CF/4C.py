st=''

def add1(a,b,c,p,q,r):
    d1, d2, d3 = p - a, q - b, r - c
    #print(a,b,c,'\n',p,q,r)
    #print('diff:',d1,d2,d3)
    if d1==d2:
        if d1==0:
            #print('here')
            if d3==0:
                return 0
            return 1#d1==0 and d3!=0
        if d1!=0:
            if d3!=0:
                return 2
            return 1
    else:
        if d3==0:
            return 2
    return 3

def multiply1(a,b,c,p,q,r):
    d1, d2, d3 = p - a, q - b, r - c
    m=3
    if a!=0 and b!=0:
        f1,f2=p/a,q/b
        if f1==f2 and f1.is_integer():
            if d3!=0:
                m=min(m,2)
            else:
                m = min(m, 1)
        else:
            if d3==0:
                m=min(m,2)
        if d3!=0:
            f1,f2=(p-d3)/a,(q-d3)/b
            if f1==f2 and f1.is_integer():
                m=min(m,2)

    if (a+d3)!=0 and (b+d3)!=0 and d3!=0:
        f1,f2=p/(a+d3),q/(b+d3)
        if f1==f2 and f1.is_integer():
            m = min(m, 2)
    return m



def func(a,b,c,p,q,r):
    m=3
    if (a==p and b==q and c==r):#d1=d2=d3=0 handled
        #print('hrer')
        m=min(m,0)#return 0
    if a!=0 and b!=0 and c!=0:
        f1,f2,f3=p/a,q/b,r/c
        if f1==f2 and f2==f3 and f1.is_integer():
            m=min(m,1)#return 1
    d1,d2,d3=p-a,q-b,r-c
    if (d1==d2 and d2==d3) or (p==q and q==r and r==0):
        m=min(m,1)#return 1
    m=min(m,add1(a,b,c,p,q,r),add1(b,c,a,q,r,p),add1(a,c,b,p,r,q))
    m=min(m,multiply1(a,b,c,p,q,r),multiply1(b,c,a,q,r,p),multiply1(a,c,b,p,r,q))
    m=min(m,3-[d1,d2,d3].count(0))
    print(m)
    return m


for _ in range(int(input())):
    a,b,c=map(int,input().split())
    p,q,r=map(int,input().split())
    st+=str(func(a,b,c,p,q,r))+'\n'
print(st[:-1])