from sys import stdin
from collections import deque

# stdin = open('input.txt', 'r')
input = stdin.readline

# functions
def BFS(W, H, K):
    # init
    checked = [[[False] * (K+1) for _ in range(W)] for _ in range(H)]
    start = [0, 0, 0]
    deq = deque([start])
    checked[0][0][0] = True
    result = 1
    
    # exec
    if W == 1 and H == 1:
        return 0
    while deq:
        l = len(deq)
        for _ in range(l):
            r, c, k = deq.popleft()
            
            # horse movement
            if k < K:
                for dr, dc in horse_dirs:
                    nr, nc = r+dr, c+dc
                    if nr == H-1 and nc == W-1:
                        return result
                    if 0 <= nr < H and 0 <= nc < W and not checked[nr][nc][k+1] and G[nr][nc] == 0:
                        deq.append([nr, nc, k+1])
                        checked[nr][nc][k+1] = True
            
            # monkey movement
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if nr == H-1 and nc == W-1:
                    return result
                if 0 <= nr < H and 0 <= nc < W and not checked[nr][nc][k] and G[nr][nc] == 0:
                    deq.append([nr, nc, k])
                    checked[nr][nc][k] = True
        result += 1
    return -1
                        

# inputs
K = int(input())
W, H = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(H)]

# init
horse_dirs = [
    [2, 1],
    [2, -1],
    [-2, 1],
    [-2, -1],
    [1, 2],
    [1, -2],
    [-1, 2],
    [-1, -2]
]
dirs = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1]
]

print(BFS(W, H, K))