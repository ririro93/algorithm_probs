from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline 

# inputs
N = int(input())
W = [int(input()) for _ in range(N)]

# init
result = 0

# exe
W.sort()
for i in range(N):
    result = max(result, W[i] * (N-i))
print(result)