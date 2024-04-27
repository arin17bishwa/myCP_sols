st = ""
p = pow(10, 9) + 7


def func(a, b):
    s1, s2 = len(str(a)), len(str(b))
    if a < 10 and b < 10:
        return a + b
    if a < 10:
        a = "0" + str(a)
    if b < 10:
        b = "0" + str(b)
    if s1 != s2:
        m = int(a) + int(b)
        a = a[1]
        l1 = list(str(a))
        l2 = list(str(b))
        if l1[0] > l2[0]:
            l2[0], l1[0] = l1[0], l2[0]
        m = max(m, (int("".join(l1))) + int("".join(l2)))
        return m

    if s1 == s2:
        l1 = list(str(a))
        l2 = list(str(b))
        # print(l1,l2)
        m = int("".join(l1)) + int("".join(l2))
        if l1[0] < l2[1]:
            l1[0], l2[1] = l2[1], l1[0]
            # print(l1,l2)
            m = max(m, (int("".join(l1))) + int("".join(l2)))
        l1 = list(str(a))
        l2 = list(str(b))
        # print(l1,l2)
        if l2[0] < l1[1]:
            l2[0], l1[1] = l1[1], l2[0]
            # print(l1,l2)
            m = max(m, (int("".join(l1))) + int("".join(l2)))

        return m


for _ in range(int(input())):
    a, b = map(int, input().split())
    # n = int(input())
    # inp=input().split()
    # s=input()
    # l1=[]
    # l1=list(map(int,input().split()))
    # l2 = list(map(int, input().split()))
    # l1=input().split()
    # l2=input().split()
    st += str(int(func(min(a, b), max(a, b)))) + "\n"
print(st)
