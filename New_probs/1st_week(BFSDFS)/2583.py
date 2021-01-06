import sys
sys.setrecursionlimit(30000)

# inputs
M, N, K = map(int, input().split())

G = [[1 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            G[i][j] = 0

# init
ds = [[1, 0], [-1, 0], [0, 1], [0, -1]]
areas = []

# functions
def DFS(a, b):
    area = 1
    for d in ds:
        na = a + d[0]
        nb = b + d[1]
        if 0 <= na < M and 0 <= nb < N and G[na][nb]:
            G[na][nb] = 0
            area += DFS(na, nb)
            # print("na: ", na, "nb: ", nb, "area: ", area)
    return area

# exe
for i in range(M):
    for j in range(N):
        if G[i][j] == 1:
            G[i][j] = 0
            areas.append(DFS(i, j))
areas.sort()
print(len(areas))
print(*areas)
               
    
