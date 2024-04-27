def func(x, y):
    a, b = min(x, y), max(x, y)
    s = pow(min(max(a + a, b), max(b + b, a)), 2)
    return s


def main():
    st = ""
    # s=0
    # l=['ABSINTH', 'BEER', 'BRANDY', 'CHAMPAGNE', 'GIN', 'RUM', 'SAKE', 'TEQUILA', 'VODKA', 'WHISKEY', 'WINE']
    for _ in range(int(input())):
        x, y = map(int, input().split())
        # x=input()

        st += str(func(x, y)) + "\n"
    print(st)


main()
