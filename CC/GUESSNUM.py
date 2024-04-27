# cook your dish here
import math


def divisors(m):
    l1 = []
    for i in range(1, int(math.sqrt(m)) + 1):
        if (m % i) == 0:
            if (m // i) == i:
                l1.append(i)
            else:
                l1.append(i)
                l1.append(m // i)
    return l1


def printDivisors(n):
    list = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:

            # Check if divisors are equal
            if n / i == i:
                print(i, end=" ")
            else:
                # Otherwise print both
                print(i, end=" ")
                list.append(int(n / i))


s = ""
for _ in range(int(input())):
    l1 = [int(y) for y in input().split()]
    a = l1[0]
    m = l1[1]
    # print(l1)
    l1 = divisors(m)
    # print(l1)
    l2 = []
    for d in l1:
        n = (m - d) / a
        # print(d,n)
        if (n >= d) and (n % 1) == 0 and (n % d) == 0:
            l2.append(int(n))
        # print(l2)
    l2.sort()
    # print(l2)
    s = s + str(len(l2)) + "\n"
    for i in l2:
        s = s + str(i) + " "
    s += "\n"

print(s)
