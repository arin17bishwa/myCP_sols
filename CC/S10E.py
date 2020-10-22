def comp(s):
    ma = max(s)
    c = 0
    l1 = [(ma + 1) for i in range(5)]
    for i in s:
        if i < min(l1):
            c += 1
        del l1[0]
        l1.append(i)

    return (c)


l = []
t = int(input())
for i in range(t):
    s = []
    inp = int(input())
    s = list(map(int, input().rstrip().split()))
    result = comp(s)
    l.append(result)

for i in l:
    print(i)



