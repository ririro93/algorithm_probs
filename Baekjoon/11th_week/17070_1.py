from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())
House = [list(map(int, input().split())) for _ in range(N)]

## init
# number of [→, ↘, ↓] for each square
paths = [[[0]*3 for _ in range(N+1)] for _ in range(N+1)]

paths[1][2][0] = 1

# exec
for i in range(1, N+1):
    for j in range(1, N+1):
        if House[i-1][j-1] == 0:
            paths[i][j][0] += paths[i][j-1][0] + paths[i][j-1][2]
            paths[i][j][1] += paths[i-1][j][1] + paths[i-1][j][2]
            if House[i-2][j-1] == 0 and House[i-1][j-2] == 0:
                paths[i][j][2] += paths[i-1][j-1][0] + paths[i-1][j-1][1] + paths[i-1][j-1][2]
print(sum(paths[N][N]))