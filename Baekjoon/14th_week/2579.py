from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())
stairs = list(int(input()) for _ in range(N))

# init
max_per_stair = [[0, 0] for _ in range(N)]
max_per_stair[0][0] = stairs[0]

# exe
if N >= 2:
    max_per_stair[1][0] = stairs[1]
    max_per_stair[1][1] = max_per_stair[0][0] + stairs[1]

for i in range(2, N):
    max_per_stair[i][0] = max(max_per_stair[i-2]) + stairs[i]
    max_per_stair[i][1] = max_per_stair[i-1][0] + stairs[i]

print(max(max_per_stair[-1]))