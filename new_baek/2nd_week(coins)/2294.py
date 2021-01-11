from sys import stdin

stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()

# function
def sol(n, k, coins):
    mx = int(1e5)+1
    ans = [0] + [mx] * k
    
    for coin in coins:
        if coin <= k:    
            for val in range(coin, k + 1):
                ans[val] = min(ans[val], ans[val-coin]+1)
    if ans[-1] == mx:
        return -1
    return ans[-1]

# exe
print(sol(n, k, coins))