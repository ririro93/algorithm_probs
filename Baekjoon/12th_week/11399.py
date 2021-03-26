from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())
P = list(map(int, input().split()))

# init
result = 0

# exec
P.sort()
for i in range(N):
    result += (N-i) * P[i]

print(result)
