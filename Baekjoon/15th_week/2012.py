from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())
expected = [int(input()) for _ in range(N)]

# init
expected.sort()
result = 0

# exec
for i in range(1, N+1):
    result += abs(i - expected[i-1])
print(result)