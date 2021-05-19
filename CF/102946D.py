def In():
    return int(input())


def main():
    n=In()
    l1=[]
    for i in range(n):
        print('? {} {}'.format(i,i))
        p=int(input())
        if p==n:
            l1.append(i)
            if len(l1)==2:
                break
    if len(l1)==1:
        return '! {}'.format(0)
    print('? {} {}'.format(l1[0],l1[1]))
    p1=int(input())
    if p1==n:
        return '! {}'.format(l1[1] - l1[0])
    return '! {}'.format((l1[0] - l1[1]) % n)


if __name__ == '__main__':
    print(main())
