from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# functions
def DFS(i, j):
    stack = [[i, j]]

    while stack:
        r, c = stack.pop()
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M:
                if not checked[nr][nc] and G[nr][nc] == 1:
                    checked[nr][nc] = True
                    stack.append([nr, nc])


while True:
    # inputs
    M, N = map(int, input().split())
    if M == N == 0:
        break
    G = [list(map(int, input().split())) for _ in range(N)]

    # init
    dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
        [1, 1],
        [1, -1], 
        [-1, 1],
        [-1, -1]
    ]
    checked = [[False] * M for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(M):
            if not checked[i][j] and G[i][j] == 1:
                DFS(i, j)
                result += 1
    print(result)

