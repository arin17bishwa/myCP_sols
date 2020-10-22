def func(a, b):
    z = a * (a - 1) // 2
    t = b * (b - 1) // 2
    return z + t


t = int(input())
s = ""
for i in range(t):
    n = int(input())
    l1 = list(map(int, input().rstrip().split()))
    a = l1.count(0)
    b = l1.count(2)
    s = s + str(func(a, b)) + "\n"

print(s)
