"""
NOT DONE

"""
from math import gcd


def func(t,w,b):
    lcm=(w*b)//gcd(w,b)
    r=t%lcm
    x=min(b-1,w-1,t)



    pass


def main():
    t, w, b = map(int, input())
    print(func(t, w, b))

if __name__ == '__main__':
    main()
