from math import sqrt


def factors(n):
    lim=int(sqrt(n))+1
    ans=1
    for i in range(2,lim+1):
        temp=0
        while n%i==0:
            temp+=1
            n//=i
        ans*=(temp+1)
    if n!=1:
        ans<<=1
    return ans


def func(n=100):
    curr=ans=-1
    for i in range(1,int(1e5)):
        n=(i*(i+1))>>1
        x=factors(n)
        if x>curr:
            ans=n
            curr=x
        if x>500:
            print(n,x)
            return
        # print(n,factors(n))
    print(ans,curr)

if __name__ == '__main__':
    func()
