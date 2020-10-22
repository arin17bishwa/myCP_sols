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
    p=n
    if n==1:return 0

    three=two=six=0
    while p>1 and p%3==0:
        p=p//3
        three+=1
    p=n
    while p>1 and (p&1==0):
        p=p>>1
        two+=1

    if three<two:return -1

    p=(n*(1<<(three-two)))//pow(6,three)
    if p==1:return three+three-two
    return -1


def func():
    t=I()
    st=''
    for _ in range(t):
        n=I()
        st='\n'.join((st,str(f(n))))

    stdout.write(st.lstrip())


if __name__ == '__main__':
    func()