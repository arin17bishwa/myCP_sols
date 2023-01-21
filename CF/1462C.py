from itertools import combinations


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(dix.get(n, -1))

    return


if __name__ == '__main__':
    perms = []
    dix = {}
    nums = [(i + 1) for i in range(9)]
    for i in range(1, 10):
        perms.extend(combinations(nums, i))
    for ele in perms:
        s = sum(ele)
        x = int(''.join(map(str, ele)))
        if s in dix:
            if x < dix[s]:
                dix[s] = x
        else:
            dix[s] = x
    main()
