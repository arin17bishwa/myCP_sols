'''DONE'''

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

def func():
    t=I()
    st = ''
    for _ in range(t):
        n=I()
        k=ans=1
        while True:
            k=((k+1)<<1)-1
            if n%k==0:ans=n//k;break
        st='\n'.join((st,str(ans)))
    print(st[1:])

if __name__ == '__main__':
    func()
