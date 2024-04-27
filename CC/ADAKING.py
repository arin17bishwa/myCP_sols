def func(k):
    l = [["X"] * 8 for _ in range(8)]
    l[0][0] = "O"
    for i in range(8):
        for j in range(8):
            if i == 0 and j == 0:
                continue
            if k:
                l[i][j] = "."
                k -= 1

    s = "\n".join("".join(i) for i in l)
    return s


def main():
    st = ""
    for _ in range(int(input())):
        k = int(input())
        st += str(func(k - 1)) + "\n"
    print(st[:-1])


main()
