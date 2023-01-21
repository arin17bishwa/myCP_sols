from bisect import bisect_left,bisect,bisect_right

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    #if i!=len(a):
    return i
    #raise ValueError

n=int(input())
prices=list(map(int,input().split()))
prices.sort()
for _ in range(int(input())):
    q=int(input())
    print(find_le(prices,q))