s = ""
for _ in range(int(input())):
    n = int(input())
    l1 = [int(y) for y in input().split()]
    l1.sort()
    s += str(l1[0]) + "\n"
print(s)
