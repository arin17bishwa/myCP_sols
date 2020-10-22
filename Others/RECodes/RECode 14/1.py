# region smaller_fastio
from sys import stdin,stdout
from os import path


if (path.exists('input.txt')):
    #------------------Sublime--------------------------------------#
    stdin=open('input.txt','r');stdout=open('output.txt','w');
    def I():return (int(input()))
    def In():return(map(int,input().split()))
else:
    #------------------PYPY FAst I/o--------------------------------#
    def I():return (int(stdin.readline()))
    def In():return(map(int,stdin.readline().split()))

#endregion
import math
def f(n,k):
    overs = math.ceil(n / k)
    ans=0
    if n<=k:return n*2
    if k==1:return n

    if n%k==0:
        ans+=overs*(2*k-1)+1
    else:
        ans=(overs-1)*(2*k-1)+(n%k)*2
    return ans


def func():
    t=I()
    st=''
    for _ in range(t):
        k,n=In()
        st+='\n'+str(f(n,k))
    print(st[1:])

if __name__ == '__main__':
    func()