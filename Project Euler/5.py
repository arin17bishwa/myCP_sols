from math import gcd
from functools import reduce


def solve(n=20):
    return reduce(lambda x, y: (x * y) // gcd(x, y), [i for i in range(1, n + 1)])


if __name__ == '__main__':
    answer = solve()
    print(answer)
