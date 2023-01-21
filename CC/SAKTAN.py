# cook your dish here
def func(r, c, ro, co):
    count = 0
    n = r * c
    erow = 0
    ecol = 0
    orow = 0
    ocol = 0
    for i in ro:
        if i % 2 == 0:
            erow += 1
    for i in co:
        if i % 2 == 0:
            ecol += 1

    orow = r - erow
    ocol = c - ecol
    count = (orow * ecol) + (erow * ocol)
    return (count)


t = int(input())
s = ""
for i in range(t):
    rcq = input().split()
    r = int(rcq[0])
    c = int(rcq[1])
    ro = [0 for i in range(r)]
    co = [0 for i in range(c)]

    q = int(rcq[2])
    for j in range(q):
        inp = input().split()
        ro[int(inp[0]) - 1] += 1
        co[int(inp[1]) - 1] += 1

    s = s + str(func(r, c, ro, co)) + "\n"

print(s)
