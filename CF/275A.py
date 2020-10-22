import sys
from collections import Counter as counter
import math
from bisect import bisect_left,bisect,bisect_right

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    #if i:
    return i
    #raise ValueError

def func(n,a,b):
    l1 = a + b
    freq_l1 = dict(counter(l1))
    for i in freq_l1.values():
        if i%2!=0:
            return -1
    #a.sort()
    #b.sort()
    afreq=dict(counter(a))
    bfreq=dict(counter(b))
    l=[]
    am=[]
    bm=[]
    for i in freq_l1.keys():
        x=(afreq.get(i,0)-bfreq.get(i,0))//2
        q=abs(x)
        if x>0:
            am.extend([i]*q)
        elif x<0:
            bm.extend([i]*q)
    ans=0
    am.sort()
    bm.sort(reverse=True)
    k=len(am)
    for i in range(k):
        ans+=min(am[i],bm[i])
    return ans

def main():
    st=''
    for _ in range(int(input())):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        st='\n'.join((st,str(func(n,a,b))))
    print(st[1:])
main()