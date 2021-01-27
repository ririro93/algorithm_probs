from collections import deque
from sys import stdin, stdout
input = stdin.readline
print = stdout.write

dx, dy, dz = (-1, 1, 0, 0, 0, 0), (0, 0, -1, 1, 0, 0), (0, 0, 0, 0, -1, 1)
L, R, C, sx, sy, sz, ex, ey, ez = [0]*9

def bfs(a, dist):
    q = deque()
    q.append((sx, sy, sz))
    while q:
        x, y, z = q.popleft()
        if x == ex and y == ey and z == ez:
            print("Escaped in %d minute(s).\n" % dist[x][y][z])
            return
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if nx < 0 or nx >= L or ny < 0 or ny >= R or nz < 0 or nz >= C:
                continue
            if dist[nx][ny][nz] or a[nx][ny][nz] == '#':
                continue
            dist[nx][ny][nz] = dist[x][y][z] + 1
            q.append((nx, ny, nz))
    print("Trapped!\n")

while True:
    L, R, C = map(int, input().split())
    if L is 0:
        break
    a = [[[]*C for _ in range(R)] for _ in range(L)]
    dist = [[[0]*C for _ in range(R)] for _ in range(L)]
    for i in range(L):
        a[i] = [list(input().strip()) for _ in range(R)]
        input()
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if a[i][j][k] == 'S':
                    sx, sy, sz = i, j, k
                elif a[i][j][k] == 'E':
                    ex, ey, ez = i, j, k
    bfs(a, dist)
