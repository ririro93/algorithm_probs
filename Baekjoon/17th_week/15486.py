from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())

# init
dp = [0] * (N+2)
max_val = 0

for i in range(1, N+1):
    period, price = map(int, input().split())
    start = i
    end = i + period - 1
    max_val = max(max_val, dp[start])
    if end + 1 <= N+1:
        dp[end+1] = max(max_val + price, dp[end+1])
print(max(dp))