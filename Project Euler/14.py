from functools import lru_cache

dp={}


@lru_cache
def collatz_rec(n):
    if n<2:
        return 1
    if n&1:
        return collatz_rec(3*n+1)+1
    else:
        return collatz_rec(n//2)+1
    

def collatz(n):
    ans=0
    k=n
    while n>1:
        if n&1:
            n=(3*n+1)//2
            ans+=1
        else:
            n>>=1
        ans+=1
        if n in dp:
            ans+=dp[n]
            break

    dp[k]=ans
    return ans


def func(n=1000000):
    ans=0
    curr=0
    for i in range(n//2,n):
        x=collatz(i)+1
        if x>curr:
            ans=i
            curr=x

    print(ans)


if __name__ == '__main__':
    func(n=1000000)
