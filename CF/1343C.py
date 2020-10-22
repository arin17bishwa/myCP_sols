

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


def f(n,l):
    s=i=0
    while i<n:
        j=i
        m1=0
        m2=-1000000000
        while i<n and l[i]<0:
            m2=max(m2,l[i])
            i+=1
        if j!=i:
            s+=m2
        j=i
        while i<n and l[i]>0:
            m1=max(m1,l[i])
            i+=1
        if j!=i:
            s+=m1
    return s

def func():
    st=''
    for _ in range(I()):
        n = I()
        l = list(In())
        st += str(f(n, l)) + '\n'
    print(st)

if __name__ == '__main__':
    func()