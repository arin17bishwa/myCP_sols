#global l#,dp
from random import randint
q=60
tests=10000
count=correct=0
dp = [[{'row': 0, 'col': 0, 'score': 0} for _ in range(q)] for _ in range(q)]
l = [[0] * q for _ in range(q)]
li=[]


def transformer(a,b,c,d,e):
    st=''
    st=str(a)+' '+str(b)+' '+str(c)+' '+str(d)+' '+str(e)
    #print('query',st)
    return (counting(st))

def special(n,r,val):
    global l,dp
    mid=(n//2)-1
    aft=mid+1
    l[r][mid]=val
    l[r][aft]=val
    if r==0:
        dp[r][mid]['col']=val
        dp[r][mid]['row']=dp[r][mid-1]['row']+val
        dp[r][mid]['score']=dp[r][mid]['row']

        dp[r][aft]['col'] = val
        dp[r][aft]['row'] = dp[r][aft - 1]['row'] + val
        dp[r][aft]['score'] = dp[r][aft]['row']
    else:
        dp[r][mid]['col'] = val+dp[r-1][mid]['col']
        dp[r][mid]['row'] = dp[r][mid - 1]['row'] + val
        dp[r][mid]['score'] =val+ dp[r-1][mid-1]['score']+dp[r-1][mid]['col']+dp[r][mid-1]['row']

        dp[r][aft]['col'] = val + dp[r - 1][aft]['col']
        dp[r][aft]['row'] = dp[r][aft - 1]['row'] + val
        dp[r][aft]['score'] = val + dp[r - 1][aft - 1]['score'] + dp[r - 1][aft]['col'] + dp[r][aft - 1]['row']


def func(n):
    global l,dp
    row=col=1
    #dp=[[{'row':0,'col':0,'score':0} for _ in range(n)] for _ in range(n)]

    while row<=n:
        r=row-1
        col=1
        t=transformer(1,1,col,row,n)
        x=t#int(input())
        allcol=x
        col+=1
        while col<=(n//2):

            c=col-1
            t=transformer(1,1,col,row,n)
            y=t#int(input())
            if row==1:
                k=x-y
                if col-1==1:#first box
                    dp[r][c - 1]['col'] = k
                    dp[r][c-1]['row']=k
                    dp[r][c - 1]['score'] = k
                else:
                    dp[r][c-1]['row']=k+dp[r][c-2]['row']
                    dp[r][c-1]['col']=k#colsum
                    dp[r][c-1]['score']=k+dp[r][c-2]['score']
            else:
                k=x-y-dp[r-1][c-1]['col']

            if col-1==1:
                dp[r][c-1]['row']=k
                if row!=1:
                    dp[r][c - 1]['score'] = k+dp[r-1][c-1]['score']
                    dp[r][c - 1]['col'] = k+dp[r-1][c-1]['col']

            if row>1 and col-1>1:
                dp[r][c - 1]['row'] = k+dp[r][c-2]['row']
                dp[r][c - 1]['col'] = k+dp[r-1][c-1]['col']
                dp[r][c - 1]['score'] = k+dp[r-1][c-2]['score']+dp[r][c-2]['row']+dp[r-1][c-1]['col']
            l[r][c-1]=k
            x=y
            #print(dp[r])  ##########
            col+=1

        x=allcol
        dp[r][n-1]['score']=x
        if row==1:
            dp[r][n - 1]['row'] = x
        else:
            dp[r][n-1]['row']=x-dp[r-1][n-1]['score']
        col=n-1
        while col>(n//2):
            c=col-1

            t=transformer(1,1,1,row,col)
            y = t#int(input())
            dp[r][c]['score'] = y
            if row==1:
                k=x-y
                dp[r][c]['row'] = y
                dp[r][c+1]['col'] = k
                #dp[r][c]['score'] = y
            else:
                k=x-y-dp[r-1][c+1]['col']
                dp[r][c + 1]['col'] = k+dp[r-1][c+1]['col']
                dp[r][c]['row']=y-dp[r-1][c]['score']
            l[r][c+1]=k
            x=y
            #print(dp[r])  ##########
            col-=1

        bef,aft=(n//2)-1-1,(n//2)+1-1
        mid=(n//2)-1
        if row==1:
            diff=dp[r][aft]['score']-dp[r][bef]['score']
        else:
            diff = dp[r][aft]['row']-dp[r][bef]['row']#dp[r][aft]['score'] - dp[r][bef]['score']-dp[r-1][n//2]['col']-dp[r-1][aft]['col']
        #print('diss',row,diff)#####
        if diff!=1:
            special(n,r,diff//2)
        else:
            t=transformer(1,1,1,row,mid+1)
            y=t#int(input())
            if row==1:
                x=dp[r][aft]['row']
                #print('x',x)
                k1=x-y
                l[r][aft]=k1
                k2 = int(not k1)  # ~k1#-diff
                #print('k2', k2)  #########
                l[r][mid]=k2
                dp[r][mid]['col'] = k2
                dp[r][mid]['row']=k2+dp[r][mid-1]['row']
                dp[r][mid]['score']=dp[r][mid]['row']
                dp[r][aft]['col']=k1#+dp[r][mid]['col']
            else:
                x = dp[r][aft]['row']
                #print('x', x)#########
                y=y-dp[r-1][mid]['score']
                k1=x-y
                l[r][aft] = k1
                k2=int(not k1)#~k1#-diff
                #print('k2',k2)#########
                l[r][mid] = k2
                dp[r][mid]['col'] = k2+dp[r-1][mid]['col']
                dp[r][mid]['row'] = k2 + dp[r][mid - 1]['row']
                dp[r][mid]['score'] =k2+ dp[r-1][mid]['col']+dp[r][mid-1]['row']+dp[r-1][mid-1]['score']
                dp[r][aft]['col'] = k1 + dp[r-1][aft]['col']

        #print(dp[r])
        row+=1

    #for i,j in enumerate(dp):
     #   print(i+1,j)

def counting(st):
    global li,count
    count+=1
    whatever,row1,col1,row2,col2=map(int,st.split())
    s=0
    for i in range(row1-1,row2):
        for j in range(col1-1,col2):
            s+=li[i][j]
    #print(s)
    return (s)

for _ in range(tests):
    for i in range(q):
        lii = []
        for j in range(q):
            lii.append(randint(0, 1))
        li.append(lii)

    #print('original one:')
    for i in li:
        pass#print(*i)
    func(q)
    #print('original')
    for i in li:
        pass#print(*i)
    print()
    for i in l:
        pass#print(*i)
    mismatch=0
    for i in range(q):
        for j in range(q):
            if l[i][j]!=li[i][j]:
                print('mismatch at :',i+1,j+1)
                mismatch+=1
                #break
    if mismatch==0:
        correct+=1
    print('total queries:',count)
    print('correct:',correct)

print('\nAVERAGE QUERY:',count/tests)
if correct==tests:
    print('\nALL CORRECT')
'''
for _ in range(int(input())):
    st=''
    n,p=map(int,input().split())
    l = [[0] * n for _ in range(n)]
    dp = [[{'row': 0, 'col': 0, 'score': 0} for _ in range(n)] for _ in range(n)]
    func(n)
    print(2)
    for i in l:
        for j in i:
            st += str(j) + ' '
        st += '\n'
    print(st[:-1])
    x=input()
    if x==-1:
        break

'''

'''
        while col<=(n//2)+1:
            c=col-1
            print(1,1,col,row,col)
            y=int(input())
            if row==1:
                k=x-y
                dp[r][c-1]=k
            else:
                k=x-y-dp[r-1][c-1]
                dp[r][c-1]=k+dp[r-1][c-1]
            l[r][c-1]=k
            x=y
            col+=1
'''