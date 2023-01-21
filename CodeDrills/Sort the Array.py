def func(k):
    # k+=1
    global l1
    lim1=int(pow(k,0.5))
    sq=[i*i for i in range(lim1+1)]
    arr=sq[:]
    for i in range(1,lim1+1):
        arr.append(i)
        for x in sq:
            if i*x<=k:
                arr.append(x*i)
    print(list(set(arr)))

    # print(set(l1)-set())


if __name__ == '__main__':
    arr=[1,2,3,5,2,5,2,5,3,6,8,5,6,2,4,5]
    l1=[]
    n=len(arr)
    for i in range(n):
        for j in range(n):
            l1.append(arr[i]^arr[j])
    arr.sort()
    print(arr)