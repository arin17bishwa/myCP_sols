# cook your dish here
def func(l1):
    mi = min(l1)
    tot = (len(l1) * mi)
    c = mi
    # print(c,tot)
    l1 = l1[:(l1.index(mi))]
    while (len(l1)) > 0:
        # print(l1)
        l2 = l1[::-1]
        mi = min(l2)
        len1 = len(l1)
        ind2 = l2.index(mi)
        ind1 = len1 - ind2 - 1
        if (mi - c) < 1:
            l1 = l1[:ind1]
        # print('s')
        tot += ((ind1 + 1) * (mi - c))
        l1 = l1[:ind1]
        c = mi

    return (str(tot))


st = ''
for _ in range(int(input())):
    n = int(input())
    l1 = [int(y) for y in input().split()]
    st = st + func(l1) + '\n'

print(st)
