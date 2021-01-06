from collections import deque
# from sys import stdin

# stdin = open("input.txt", "r")
# input = stdin.readline

# inputs
N = int(input())

# init
dirs = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, 2], [-2, 1], [-2, -1], [-1, -2]]

# functions
def knight(L, sx, sy, ex, ey):
    G = [[False for _ in range(L)] for _ in range(L)]
    G[sx][sy] = True
    deq = deque()
    deq.append([sx, sy])
    cnt = 0

    while deq:
        curr_len = len(deq)
        points = []
        cnt += 1
        for _ in range(curr_len):
            points.append(deq.popleft())
        for point in points:
                for d in dirs:
                    nx = point[0] + d[0]
                    ny = point[1] + d[1]
                    if nx == ex and ny == ey:
                        return cnt
                    elif 0 <= nx < L and 0 <= ny < L and not G[nx][ny]:
                        G[nx][ny] = True
                        deq.append([nx, ny])

# exe
for _ in range(N):
    L = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    
    if sx == ex and sy == ey:
        print(0)
    else:
        # knight() returns num of moves needed
        print(knight(L, sx, sy, ex, ey))