def func(n):
    origin=(0,0)
    x=[f(origin, n, direc=i) for i in range(4)]
    print(n,len(ans),len(set(ans)))


def f(co_ord, step, direc=0):
    arr=[]
    x=(0,1)
    y=(2,3)
    if step==0:
        ans.append(co_ord)
        return co_ord
    if direc==0:
        arr.extend([f((co_ord[0]-1,co_ord[1]),step-1,i) for i in y])
    elif direc==1:
        arr.extend([f((co_ord[0]+1,co_ord[1]),step-1,i) for i in y])
    elif direc==2:
        arr.extend([f((co_ord[0], co_ord[1] + 1),step-1,i) for i in x])
    else:
        arr.extend([f((co_ord[0], co_ord[1] -1),step-1,i) for i in x])
    return arr[0],arr[1]


if __name__ == '__main__':
    for k in range(1,100):
        ans=[]
        func(k)