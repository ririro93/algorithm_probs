from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())
streets = list(map(int, input().split()))
prices = list(map(int, input().split()))

# init
min_price = prices[0]
result = 0

# exec
for i in range(N-1):
    min_price = min(min_price, prices[i])
    result += streets[i] * min_price
print(result)