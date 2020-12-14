if __name__ == '__main__':
    t = int(input())
    answers = [' ' * 50] * t
    fac = [1] * 101
    for i in range(1, 101):
        fac[i] = fac[i - 1] * i
    for i in range(t):
        n = int(input())
        answers[i] = str(fac[n])
    print('\n'.join(answers))
