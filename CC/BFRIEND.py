s = ""


def func(l1, a, b, c):
    l2 = l1[:]
    l2.append(b)
    l2.sort()
    k = c
    ind2 = l2.index(b)
    if ind2 == 0:
        k += abs(l2[1] - b) + abs(a - l2[1])

    elif ind2 == len(l2) - 1:
        k += abs(l2[len(l2) - 2] - b) + abs(a - l2[len(l2) - 2])

    else:
        k += min(
            abs(l2[ind2 - 1] - b) + abs(a - l2[ind2 - 1]),
            abs(l2[ind2 + 1] - b) + abs(a - l2[ind2 + 1]),
        )

    return k


for _ in range(int(input())):
    n, a, b, c = map(int, input().split())
    l1 = list(map(int, input().split()))
    s += str(func(l1, a, b, c)) + "\n"
print(s)
