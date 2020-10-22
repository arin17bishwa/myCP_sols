s = ""
t = int(input())
for _ in range(t):
    n = int(input())
    l1 = [0 for i in range(8)]

    for i in range(n):
        inp = [int(y) for y in input().split()]
        a, b = inp[0], inp[1]
        if a > 8:
            continue
        l1[a - 1] = max(l1[a - 1], b)

    s = s + str(sum(l1)) + "\n"

print(s)
