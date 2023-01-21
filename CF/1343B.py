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

def f(n):
    if n%4!=0:return 'NO'
    l=[]
    st='YES\n'
    l=[i for i in range(2,n+1,2)]+[i for i in range(1,n+1,2)]
    l[-1]=3*(n>>1)-1
    return ''.join((st,' '.join(map(str,l))))


def func():
    t=I()
    st=''
    for _ in range(t):
        n=I()
        st='\n'.join((st,f(n)))
    stdout.write(st.lstrip())

if __name__ == '__main__':
    func()