# region smaller_fastio
from sys import stdin, stdout
from os import path

if (path.exists('input.txt')):
    # ------------------Sublime--------------------------------------#
    stdin = open('input.txt', 'r');
    stdout = open('output.txt', 'w');


    def I():
        return (int(input()))


    def In():
        return (map(int, input().split()))
else:
    # ------------------PYPY FAst I/o--------------------------------#
    def I():
        return (int(stdin.readline()))


    def In():
        return (map(int, stdin.readline().split()))


    def S():
        return (stdin.readline().rstrip())


    def Sn():
        return (stdin.readline().split(' '))


# endregion

from collections import deque

def f(s):
    n=len(s)
    d=deque()
    for i in s:
        if i=='(':
            d.append(i)
        if i==')':
            if len(d)<1:pass

    pass

def func():
    st=''
    t=I()
    for _ in range(t):
        n=I()
        s=S()
        st='\n'.join((st,str(f(s))))

    stdout.write(st.lstrip())

if __name__ == '__main__':
    func()