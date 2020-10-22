def f(n,l):
    m=l.index(max(l))
    s=m
    m=l[::-1].index(min(l))
    if n-m-1<s:
        m-=1
    return m+s

def main():
    n=int(input())
    l=list(map(int,input().split()))
    print(f(n,l))
main()