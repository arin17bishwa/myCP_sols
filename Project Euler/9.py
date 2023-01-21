def solve():
    for i in range(3,1000):
        for j in range(i,1000):
            x=i*i+j*j
            c=int(pow(x,0.5))
            if c*c==x:
                if i+j+c==1000:
                    return i*j*c


if __name__ == '__main__':
    answer=solve()
    print(answer)