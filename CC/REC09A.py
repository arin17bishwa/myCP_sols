# cook your dish here
def func(l1, k):
    s = sum(l1)
    if s > k:
        return "NO"
    if s == k:
        return "YES"
    r = k - s
    l1.sort()
    if r > l1[len(l1) - 1] or r < l1[0] or r in l1:
        return "NO"

    return "YES"


l = [int(y) for y in input().split()]
n = l[0]
k = l[1]
l1 = [int(y) for y in input().split()]
print(func(l1, k))
