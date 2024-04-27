st = ""
global k


def transformer(i):
    return min(i, k)


for _ in range(int(input())):
    n, k = map(int, input().split())
    l1 = list(map(int, input().split()))
    l2 = list(map(transformer, l1))
    st += str(sum(l1) - sum(l2)) + "\n"
print(st)
