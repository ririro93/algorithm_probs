from sys import stdin

stdin = open('input.txt', 'r')
input = stdin.readline

# functions
def DFS(i, j, r, c, cnt):
    """
    - 사방향이 한번 씩 나오고
    - 길이가 4 이상이고 
    - checked = True인 곳이랑 만나면 
    - -> 사이클이 존재한다
    """
    global N, M, result
    print(r, c, cnt)
    print(ds)

    for dr, dc, direction in [[1, 0, 0], [-1, 0, 1], [0, 1, 2], [0, -1, 3]]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < N and 0 <= nc < M:
            if cnt >= 4 and checked[nr][nc]:
                if ds[0] <= 0 and ds[1] <= 0 and ds[2] <= 0 and ds[3] <= 0:
                    result = True
                    return 

            if not checked[nr][nc] and G[nr][nc] == G[i][j]:
                ds[direction] -= 1

                checked[nr][nc] = True
                DFS(i, j, nr, nc, cnt+1)  
    return

def solve():
    global N, M, result
    for i in range(N):
        for j in range(M):
            if not checked[i][j]:
                print('###', i, j)
                ds = [1, 1, 1, 1]  # 네 방향 적어도 한번씩 움직여야됨
                checked[i][j] = True
                DFS(i, j, i, j, cnt=1)
                if result:
                    return 'Yes'
    return 'No'

# inputs
N, M = map(int, input().split())
G = [input().rstrip() for _ in range(N)]

# init
checked = [[False]*M for _ in range(N)]
result = False
ds = [1, 1, 1, 1]

# exec
print(solve())