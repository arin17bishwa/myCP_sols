def func(x1,y1,x2,y2):
    if x1 != x2 and y1 != y2:
        x = abs(x1 - x2)
        y = abs(y1 - y2)
        if x!=y:
            print(-1)
        else:
            x3,x4=x1,x2
            y3,y4=y2,y1
            print(x3,y3,x4,y4)
    elif x1!=x2:
        y=abs(x1 - x2)
        x=y
        x3, x4 = x1, x2
        if y1+x<1001:
            y3=y4=y1+x
            print(x3, y3, x4, y4)
        elif y1-x>-1001:
            y3 = y4 = y1 - x
            print(x3, y3, x4, y4)
        else:
            print(-1)

    elif y1!=y2:
        x=abs(y1-y2)
        y=x
        y3,y4=y1,y2
        if x1+y<=1001:
            x3=x4=x1+y
            print(x3, y3, x4, y4)
        elif x1-y>-1001:
            x3=x4=x1-y
            print(x3, y3, x4, y4)
        else:
            print(-1)
    else:
        print(-1)

x1,y1,x2,y2=map(int,input().split())
func(x1,y1,x2,y2)