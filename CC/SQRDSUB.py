import math
from math import gcd
from math import sqrt


def transformer(i):
    if i == 'd' or i == 'f':
        return 1
    return 0


def changer(i):
    if i % 2 == 1:
        return 1
    if i % 4 == 2:
        return 2
    return 0


def calc(start, end, i):
    # print(start,end,i,(i-start+1)*(end-start+1-(i-start)))
    if i == -1:
        return 0
    return (i - start + 1) * (end - start + 1 - (i - start))


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


def Prime_factorization(n):  # with count of powers of each variable
    l = []
    i = 2
    c = 0
    while n & 1 == 0:
        n = n >> 1
        c += 1
        # print('factoring 2')
    if c != 0:
        l.append([i, c])
    q = int(math.sqrt(n))
    i = 3
    # print(n)
    while i <= q + 1:
        c = 0
        # print('i is',i)
        while n % i == 0:
            n = n // i
            c += 1
        if c:
            l.append([i, c])
        i += 1
    if n != 1:
        l.append([n, 1])
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


def func(n, l1):
    i = start = end = s = c = flag = 0
    ind = start = -1
    l = list(map(changer, l1))
    # print(l)
    while i < n:
        if l[i] == 0:
            if flag:
                s += calc(start, i - 1, ind)
                flag = 0
                start = -1
            else:
                start = -1
                ind = -1

        elif l[i] == 1:
            if flag == 1:
                end = i
            else:
                if start == -1:
                    start = end = i
                else:
                    end = i

        else:  # l[i]==2
            if flag:  # ==1
                s += calc(start, i - 1, ind)
                start = ind + 1
                end = i
                ind = i

            else:
                ind = i
                flag = 1
                if start == -1:
                    start = end = i
        i += 1
    if flag:
        s += calc(start, i - 1, ind)
    # print('s',s)
    return int((n * (n + 1) / 2) - s)


for _ in range(int(input())):
    # n,m,k=map(int,input().split())
    n = int(input())
    # inp=input().split()
    # s=input()
    # l1 = list(map(transformer, input()))
    # l=[]
    l1 = list(map(int, input().split()))
    # l2 = list(map(int, input().split()))
    # l1=input().split()
    # l2=input().split()
    # func(l1,n,m)
    st += str((func(n, l1))) + '\n'
print(st)
