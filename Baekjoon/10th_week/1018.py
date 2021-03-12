from sys import stdin
from collections import deque

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N, M = map(int, input().split())
Board = [input().rstrip() for _ in range(N)]

# init
result = 64

# exec
for r in range(N-7):
    for c in range(M-7):
        cnt1 = cnt2 = 0
        for i in range(r, r+8):
            for j in range(c, c+8):
                if (i+j) % 2 == 0:
                    if Board[i][j] == 'B':
                        cnt1 += 1
                    else:
                        cnt2 += 1
                else:
                    if Board[i][j] == 'W':
                        cnt1 += 1
                    else:
                        cnt2 += 1
        result = min(result, cnt1, cnt2)
print(result)