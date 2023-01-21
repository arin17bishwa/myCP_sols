t = int(input())
s = ""
for i in range(t):
    p = ""
    n = int(input())
    l1 = list(map(int, input().rstrip().split()))
    ma = max(l1)
    mi = min(l1)
    if l1.index(ma) < l1.index(mi):
        p = str(ma) + " " + str(mi)

    else:
        p = str(mi) + " " + str(ma)
    s = s + p + "\n"

print(s)
