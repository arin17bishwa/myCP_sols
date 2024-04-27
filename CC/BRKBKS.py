s = ""


def func(l1):
    k = l1[0]
    del l1[0]
    c = 0
    i = 0
    while i < (len(l1)):
        s = 0
        while s <= k:
            s += l1[i]
            if s > k:
                break
            i += 1
            if i >= len(l1):
                break
        c += 1
    return c


for _ in range(int(input())):
    l1 = [int(i) for i in input().split()]
    s = s + str(func(l1)) + "\n"

print(s)
