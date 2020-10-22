global l
z=0
def printing(l):
    s=''
    for i in l:
        for j in i:
            s += str(j) + ' '
        s += '\n'
    print(s[:-1])

def filling_up(r,c,dis,val):
    for i in range(r,r+dis):
        for j in range(c,c+dis):
            l[i][j]=val

def sidefill(r,c,v1,v2):
    l[r][c] = v1
    l[r][c + 1] = v2

def func(row,col,dis):
    if dis==2:
        x=f4(row,col)
    else:
        r, c = row - 1, col - 1
        f = 1
        print(1, row, col, row + dis-1, col + dis-1)
        x = int(input())
        rem = x
        if x==0:
            filling_up(r,c,dis,0)
        elif x==(dis*dis):
            filling_up(row,col,dis,1)
            rem-=x
        else:
            while row-r<dis and f:
                col=c+1
                while col-c<dis and f:
                    y=func(row,col,dis//2)
                    rem-=y
                    if not rem>0:
                        f=0
                    col+=(dis//2)
                row+=(dis//2)
    return x

def f4(row,col):
    r, c = row - 1, col - 1
    f = 1
    print(1,row,col,row+1,col+1)
    x = int(input())
    rem = x
    if rem==0:
        filling_up(r,c,2,0)
    elif rem==4:
        filling_up(r,c,2,1)
        rem-=4

    else:#rem==1,2,3
        while rem>0:
            y=f2(row,col)
            rem-=y
            row+=1
            z=0
            if rem==2:
                sidefill(r+1,c,1,1)
            elif rem==1:
                z = f1(row, col)
                if z == 1:
                    sidefill(r + 1, c, 1, 0)
                else:
                    sidefill(r + 1, c, 0, 1)
            rem=0
    return x

def f2(row,col):
    r, c = row - 1, col - 1
    print(1, row, col, row, col + 1)
    x = int(input())
    if x == 0:
        l[r][c] = l[r][c + 1] = 0
        return 0
    elif x == 2:
        l[r][c] = l[r][c + 1] = 1
        return 2
    else:
        y = f1(row, col)
        if y == 0:
            l[r][c] = 0
            l[r][c + 1] = 1
        else:
            l[r][c] = 1
            l[r][c + 1] = 0
        return 1

def f1(row,col):
    r, c = row - 1, col - 1
    print(1, row, col, row, col)
    x = int(input())
    return x

test=int(input())
for _ in range(test):
    dis=32
    n,p=map(int,input().split())
    l=[[0]*n for _ in range(n)]
    row=col=1
    br=bc=1
    func(1,1,32)
    func(1,29,32)
    func(29,1,32)
    func(29,29,32)
    
    #y=func(row,col,4)###
    print(2)
    printing(l)
    ans = int(input())
    if ans == -1:
        break

'''
base=1
    while (dis//2)>=4:
        #print('DIS',dis)
        br+=dis
        bc+=dis
        row=col=1
        for i in range(2*base+1):
            x=func(br,col,dis//2)
            col+=dis//2
        for i in range(2*base):
            x=func(row,bc,dis//2)
            row+=dis//2
        dis=dis//2
        base=2*base+1

'''