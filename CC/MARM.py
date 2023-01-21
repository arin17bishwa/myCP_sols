def func(n, k, s):
    if (n % 2) != 0 and (k > (n // 2)):
        s[(n - 1) // 2] = 0
    k = k % (3 * n)
    for i in range(k):
        p = i % n
        s[p] = s[p] ^ s[n - p - 1]

    return s


t = int(input())
l = []
for i in range(t):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    s = list(map(int, input().rstrip().split()))
    res = func(n, (k), s)
    l.append(res)

for i in range(t):
    for j in l[i]:
        print(j, end=" ")
    print("")