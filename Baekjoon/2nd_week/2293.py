# from sys import stdin

# stdin = open('input.txt', 'r')
# input = stdin.readline

# inputs
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# init
cnt = 0

# exe
def sol(k, coins):
    global cnt
    my_list = coins[:]
    while True:
        coin = my_list.pop()
        if coin <= k:
            break
    q =  k // coin
    for num in range(q, -1, -1):
        r = k - num * coin
        # print("k: ", k, "coin: ", coin, "num: ", num, "r: ", r)
        if r == 0:
            cnt += 1
        elif len(my_list) >= 2:
            sol(r, my_list)
        elif len(my_list) == 1:
            if r % my_list[0] == 0:
                cnt += 1
                    
sol(k, coins)
print(cnt)