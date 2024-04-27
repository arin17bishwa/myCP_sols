t = int(input())
l = []
for i in range(t):
    l.append(int(input()))

n = max(l)
s = "00"
q = "0"
l1 = [0, 0]
l2 = [0, 0]
for i in range(n - 2):
    len1 = len(l1)
    p = l1[len1 - 1]
    if p not in l1[: len1 - 1]:
        q = "0"
    else:
        q = str(l2[1:].index(p) + 1)
    s = s + str(q)
    l1.append(int(q))
    l2.insert(0, int(q))
# print(s)
# print(l1,l2)
# print("len1,p,q,l1,l2",len1,p,q,l1,l2)

st = ""
# print(l1)
for i in l:
    # print(l1[:i],l1[i-1])
    st = st + str(l1[:i].count(l1[i - 1])) + "\n"

print(st)
# print("l1,l2",l1,l2)
