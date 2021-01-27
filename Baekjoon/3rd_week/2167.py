from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs -> add zero padding
N, M = map(int, input().split())
G = [[0]*(M+1)] + [[0]+[*map(int, input().split())] for _ in range(N)]
K = int(input())

# function
def solve(i, j, x, y):
    result = 0
    for a in range(i, x+1):
        for b in range(j, y+1):
            result += G[a][b]
    return result

# exe
for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(solve(i, j, x, y))