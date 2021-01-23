from sys import stdin, stdout

stdin = open('change.in', 'r')
input = stdin.readline
f = open('2091_result.txt', 'a')

while True:
    # inputs
    P, C1, C2, C3, C4 = map(int, input().split())

    # init -> cache stores max number of coins needed for each price
    C = [[0, 0, 0, 0]] + [[-1, -1, -1, -1] for _ in range(P)]
    not_checked = [-1, -1, -1, -1]
    max_price = C1 + 5 * C2 + 10 * C3 + 25 * C4

    # exe
    ## if wanted price is higher than possible max price and if not enough 1 cents
    if P == C1 == C2 == C3 == C4 == 0:
        break
    elif P > max_price or P % 5 > C1:
        # print('0 0 0 0')
        f.write('Charlie cannot buy coffee.\n')
    else:
        ## fill the first prices with 1 cent coins
        for i in range(1, P+1):
            # check -1 cent
            if C[i-1][0] < C1 and C[i-1] != not_checked:
                C[i] = C[i-1][:]
                C[i][0] += 1
            
            # check -5 cents
            elif i - 5 >= 0 and C[i-5][1] < C2 and C[i-5] != not_checked:
                C[i] = C[i-5][:]
                C[i][1] += 1
            
            # check -10 cents
            elif i - 10 >= 0 and C[i-10][2] < C3 and C[i-10] != not_checked:
                C[i] = C[i-10][:]
                C[i][2] += 1

            # check -25 cents
            elif i - 25 >= 0 and C[i-25][3] < C4 and C[i-25] != not_checked:
                C[i] = C[i-25][:]
                C[i][3] += 1
            # if making 30 -> 5*1 + 1*25 better than 3*10
            if i - 25 >= 0 and C[i-25][3] < C4 and C[i-25] != not_checked:
                n = C[i-25][:]
                n[3] += 1
                if sum(n) > sum(C[i]):
                    C[i] = n[:]
        result = C[P]

        # for i, a in enumerate(C[:P+1]):
        #     print(i, a)
        if result == not_checked:
            # print('0 0 0 0')
            f.write('Charlie cannot buy coffee.\n')
        else:
            # print(*result)        
            f.write(f'Throw in {result[0]} cents, {result[1]} nickels, {result[2]} dimes, and {result[3]} quarters.\n')
f.close()