t = int(input())
n = []
m = []
l1 = []
l2 = []
for i in range(t):
    l4 = []
    inp = input()
    l4 = inp.split(" ")
    n.append(int(l4[0]))
    m.append(int(l4[1]))
    inp = input()
    l1.append(inp)

for i in range(t):
    l2 = list(map(int, l1[i].rstrip().split()))
    a = n[i]
    b = m[i]
    s = "YES"
    l3 = [0 for k in range(a)]
    for j in range(b):
        p = l2[j]
        l3[p - 1] = l3[p - 1] + 1
        ma = max(l3)
        if (ma - 2) in l3:
            s = "NO"
            break

    print(s)
