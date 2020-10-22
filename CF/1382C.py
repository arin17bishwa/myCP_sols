def func(x):
    a=''
    b=''
    f=0
    l=list(map(int,x))
    for i in l:
        if f==0:
            if i==2:
                a+='1'
                b+='1'
            elif i==0:
                a+='0'
                b+='0'
            else:
                f=1
                a+='1'
                b+='0'

        else:
            a+='0'
            b+=str(i)
    print(a)
    print(b)


for _ in range(int(input())):
    n=int(input())
    x=input()
    func(x)