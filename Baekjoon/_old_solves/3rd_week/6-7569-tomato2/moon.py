# get inputs -> row: N, col: M, height: H
M, N, H = map(int, input('').split(' '))
box = []

for h in range(H):
    box.append([[*map(int, input('').split(' '))] for _ in range(N)])

# initialization
old = []
days = 0
finished = False

# execution
def BFS(box, old, H, N, M, days):
    directions = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]]
    
    while old:
        new = []
        for tomato in old:
            h, r, c = tomato
            for direction in directions:
                nh = h + direction[0]
                nr = r + direction[1]
                nc = c + direction[2]
                if nh >= 0 and nr >= 0 and nc >= 0 and nh < H and nr < N and nc < M:
                    if box[nh][nr][nc] == 0:
                        box[nh][nr][nc] = 1
                        new.append([nh, nr, nc])
        old = new
        days += 1
    return days
            

for h in range(H):
    for i in range(N):
        for j in range(M):
            if box[h][i][j] == 1:
                old.append([h, i, j])

days = BFS(box, old, H, N, M, days)

for h in range(H):
    for i in range(N):
        if 0 in box[h][i]:
            finished = True
            
if finished: print(-1)
else: print(days - 1)
