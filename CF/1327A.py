for _ in range(int(input())):
    n,k=map(int,input().split())
    if (k*k>n) or (k%2!=n%2):
        print('NO')
    else:
        print('YES')