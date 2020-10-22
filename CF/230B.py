import math
from bisect import bisect_left,bisect,bisect_right
def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return 1
    return 0
def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        if (prime[p] == True):

            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    l1 = []
    for i in range(n + 1):
        if prime[i] == True:
            l1.append(i)
    return (l1)
primes=SieveOfEratosthenes(1000000)
n=int(input())
l=list(map(int,input().split()))
for i in l:
    p=(math.sqrt(i))
    if p%1!=0:
        print('NO')
        continue
    if index(primes,p):
        print('YES')
    else:
        print("NO")