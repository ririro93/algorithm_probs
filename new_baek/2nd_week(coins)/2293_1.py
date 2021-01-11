# from sys import stdin

# stdin = open('input.txt', 'r')
# input = stdin.readline

# input
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# init
ans = [1] + [0] * k
 
# exe
for coin in coins:
    for val in range(coin, k+1):
        ans[val] += ans[val-coin]
print(ans[-1])