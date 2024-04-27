# cook your dish here
from math import gcd
from math import sqrt


def transformer(i):
    if i == 'd' or i == 'f':
        return 1
    return 0


def changer(s):
    l = []
    for i in s:
        if i == 'H':
            l.append(1)
        elif i == 'T':
            l.append(0)
    return l


def lcm(i, j):
    # print('calc gcd of',i,j)
    return ((i * j) // gcd(i, j))


def Prime_factors(n):
    s = sqrt(n)
    l = []
    while (n % 2) == 0:
        n = n >> 1
    i = 3
    while i < (int(s) + 1) and n > 1:
        if n % i == 0:
            l.append(i)
            while n % i == 0:
                n = n // i
        i += 2
    return l


def leapyear(n):
    if n % 100 == 0:
        if n % 400 == 0:
            return True
        return False
    if n % 4 == 0:
        return True
    return False


st = ''
p = pow(10, 9) + 7


def func(n, l1, l2):
    m1 = max(l1)
    m2 = max(l2)
    if m1 == m2:
        return 'NO'
    return 'YES'


for _ in range(int(input())):
    # n,m=map(int,input().split())
    n = int(input())
    # inp=input().split()
    # s=input()
    # l1 = list(map(transformer, input()))
    # l=[]
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    # l1=input().split()
    # l2=input().split()
    # func(p,l2)
    st += str((func(n, l1, l2))) + '\n'
print(st)
