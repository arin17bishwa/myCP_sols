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

SUM=lambda x: (x*(x+1))//2
def func():
    n=1000-1
    ans=3*SUM(n//3)+5*SUM(n//5)-15*SUM(n//15)
    print(ans)
if __name__ == '__main__':
    func()