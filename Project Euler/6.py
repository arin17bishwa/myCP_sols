def solve(n=100):
    sum_sq = pow((n * (n + 1)) >> 1, 2)
    sq_sum = (n * (n + 1) * (n * 2 + 1)) // 6
    return sum_sq - sq_sum


if __name__ == '__main__':
    answer = solve()
    print(answer)
