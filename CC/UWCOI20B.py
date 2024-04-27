st = ""


def func(l1, n):
    even, odd = 0, 0
    for i in l1:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even * odd


for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split()))
    st += str(func(l1, n)) + "\n"

print(st)
