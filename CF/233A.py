def f(n):
    if n&1:
        return -1
    l=[0]*n
    for i in range(0,n,2):
        l[i],l[i+1]=i+2,i+1
    return ' '.join(map(str,l))
def main():
    n=int(input())
    print(f(n))
main()