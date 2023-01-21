import sys
from collections import Counter as counter
cin=sys.stdin.readline
cout=sys.stdout.write

def func(n,t,l):
    i=1
    if i==t:
        return 'YES'
    while i<=t:
        i+=l[i-1]
        if i==t:
            return 'YES'
    return 'NO'

def main():
    n,t=(map(int,cin().split()))
    l=list(map(int,cin().split()))
    st=str(func(n,t,l))
    cout(st)

if __name__ == '__main__':
    main()
