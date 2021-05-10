from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# functions
def clean(R, C, D):
    global N, M, result

    if not checked[R][C]:
        checked[R][C] = True
        result += 1

    curr_dirs = [directions[(i-D)%4] for i in range(4)]
    for i in range(4):
        dr, dc = directions[(i-D)%4]
        nr, nc = R+dr, C+dc
        if 0 <= nr < N and 0 <= nc < M and G[nr][nc] == 0 and not checked[nr][nc]:
            clean(nr, nc, (D-i-1)%4)
            break
    else:
        dr, dc = back[D]
        nr, nc = R+dr, C+dc
        if 0 <= nr < N and 0 <= nc < M and G[nr][nc] == 0:
            clean(nr, nc, D)



##########################################################    
# inputs
N, M = map(int, input().split())
R, C, D = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]

# init
checked = [[False] * M for _ in range(N)]
directions = [[0, -1], [1, 0], [0, 1], [-1, 0]] # 서, 남, 동, 북
back = [[1, 0], [0, -1], [-1, 0], [0, 1]]
result = 0

# exec
clean(R, C, D)
print(result)