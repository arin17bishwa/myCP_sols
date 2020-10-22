master='qwertyuioplkjhgfdsazxcvbnm'
def func(n,a,b):
    sub=master[:b]
    ans=sub*(n//b)+sub[:n%b]
    return ans

for _ in range(int(input())):
    n,a,b=map(int,input().split())
    print(func(n,a,b))
