global l, dp


def special(n, r, val):
    global l, dp
    mid = (n // 2) - 1
    aft = mid + 1
    l[r][mid] = val
    l[r][aft] = val
    if r == 0:
        dp[r][mid]['col'] = val
        dp[r][mid]['row'] = dp[r][mid - 1]['row'] + val
        dp[r][mid]['score'] = dp[r][mid]['row']

        dp[r][aft]['col'] = val
        dp[r][aft]['row'] = dp[r][aft - 1]['row'] + val
        dp[r][aft]['score'] = dp[r][aft]['row']
    else:
        dp[r][mid]['col'] = val + dp[r - 1][mid]['col']
        dp[r][mid]['row'] = dp[r][mid - 1]['row'] + val
        dp[r][mid]['score'] = val + dp[r - 1][mid - 1]['score'] + dp[r - 1][mid]['col'] + dp[r][mid - 1]['row']

        dp[r][aft]['col'] = val + dp[r - 1][aft]['col']
        dp[r][aft]['row'] = dp[r][aft - 1]['row'] + val
        dp[r][aft]['score'] = val + dp[r - 1][aft - 1]['score'] + dp[r - 1][aft]['col'] + dp[r][aft - 1]['row']


def func(n):
    global l, dp
    row = col = 1
    # dp=[[{'row':0,'col':0,'score':0} for _ in range(n)] for _ in range(n)]
    while row <= n:
        r = row - 1
        col = 1
        print(1, 1, col, row, n)
        x = int(input())
        allcol = x
        col += 1
        while col <= (n // 2):

            c = col - 1
            print(1, 1, col, row, n)
            y = int(input())
            if row == 1:
                k = x - y
                if col - 1 == 1:  # first box
                    dp[r][c - 1]['col'] = k
                    dp[r][c - 1]['row'] = k
                    dp[r][c - 1]['score'] = k
                else:
                    dp[r][c - 1]['row'] = k + dp[r][c - 2]['row']
                    dp[r][c - 1]['col'] = k  # colsum
                    dp[r][c - 1]['score'] = k + dp[r][c - 2]['score']
            else:
                k = x - y - dp[r - 1][c - 1]['col']

            if col - 1 == 1:
                dp[r][c - 1]['row'] = k
                if row != 1:
                    dp[r][c - 1]['score'] = k + dp[r - 1][c - 1]['score']
                    dp[r][c - 1]['col'] = k + dp[r - 1][c - 1]['col']

            if row > 1 and col - 1 > 1:
                dp[r][c - 1]['row'] = k + dp[r][c - 2]['row']
                dp[r][c - 1]['col'] = k + dp[r - 1][c - 1]['col']
                dp[r][c - 1]['score'] = k + dp[r - 1][c - 2]['score'] + dp[r][c - 2]['row'] + dp[r - 1][c - 1]['col']
            l[r][c - 1] = k
            x = y
            # print(dp[r])  ##########
            col += 1

        x = allcol
        dp[r][n - 1]['score'] = x
        if row == 1:
            dp[r][n - 1]['row'] = x
        else:
            dp[r][n - 1]['row'] = x - dp[r - 1][n - 1]['score']
        col = n - 1
        while col > (n // 2):
            c = col - 1

            print(1, 1, 1, row, col)
            y = int(input())
            dp[r][c]['score'] = y
            if row == 1:
                k = x - y
                dp[r][c]['row'] = y
                dp[r][c + 1]['col'] = k
                # dp[r][c]['score'] = y
            else:
                k = x - y - dp[r - 1][c + 1]['col']
                dp[r][c + 1]['col'] = k + dp[r - 1][c + 1]['col']
                dp[r][c]['row'] = y - dp[r - 1][c]['score']
            l[r][c + 1] = k
            x = y
            # print(dp[r])  ##########
            col -= 1

        bef, aft = (n // 2) - 1 - 1, (n // 2) + 1 - 1
        mid = (n // 2) - 1
        if row == 1:
            diff = dp[r][aft]['score'] - dp[r][bef]['score']
        else:
            diff = dp[r][aft]['row'] - dp[r][bef][
                'row']  # dp[r][aft]['score'] - dp[r][bef]['score']-dp[r-1][n//2]['col']-dp[r-1][aft]['col']
        # print('diss',row,diff)#####
        if diff != 1:
            special(n, r, diff // 2)
        else:
            print(1, 1, 1, row, mid + 1)
            y = int(input())
            if row == 1:
                x = dp[r][aft]['row']
                # print('x',x)
                k1 = x - y
                l[r][aft] = k1
                k2 = int(not k1)  # ~k1#-diff
                # print('k2', k2)  #########
                l[r][mid] = k2
                dp[r][mid]['col'] = k2
                dp[r][mid]['row'] = k2 + dp[r][mid - 1]['row']
                dp[r][mid]['score'] = dp[r][mid]['row']
                dp[r][aft]['col'] = k1  # +dp[r][mid]['col']
            else:
                x = dp[r][aft]['row']
                # print('x', x)#########
                y = y - dp[r - 1][mid]['score']
                k1 = x - y
                l[r][aft] = k1
                k2 = int(not k1)  # ~k1#-diff
                # print('k2',k2)#########
                l[r][mid] = k2
                dp[r][mid]['col'] = k2 + dp[r - 1][mid]['col']
                dp[r][mid]['row'] = k2 + dp[r][mid - 1]['row']
                dp[r][mid]['score'] = k2 + dp[r - 1][mid]['col'] + dp[r][mid - 1]['row'] + dp[r - 1][mid - 1]['score']
                dp[r][aft]['col'] = k1 + dp[r - 1][aft]['col']

        # print(dp[r])
        row += 1

    # for i,j in enumerate(dp):
    #   print(i+1,j)


for _ in range(int(input())):
    st = ''
    n, p = map(int, input().split())
    l = [[0] * n for _ in range(n)]
    dp = [[{'row': 0, 'col': 0, 'score': 0} for _ in range(n)] for _ in range(n)]
    func(n)
    print(2)
    for i in l:
        for j in i:
            st += str(j) + ' '
        st += '\n'
    print(st[:-1])
    x = input()
    if x == -1:
        break
