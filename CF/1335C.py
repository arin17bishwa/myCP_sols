for _ in range(int(input())):
    n=int(input())
    freq=[0 for _ in range(n)]
    l=list(map(int,input().split()))
    for i in l:
        freq[i-1]+=1
    s=set(l)
    m1,m2=len(s),max(freq)
    print(max(min(m1-1,m2),min(m1,m2-1)))