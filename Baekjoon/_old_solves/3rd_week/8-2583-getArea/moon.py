from collections import deque

# get inputs
M, N, K = map(int, input('').split(' '))
coords = [[*map(int, input('').split(' '))] for _ in range(K)]


# initialization
boxes = [[1] * N for _ in range(M)]
box_points = []
checked = [[False] * N for _ in range(M)]
qu = deque()
count_list = []
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]


# # execution
# turn boxes to 0 and rest to 1
for coord in coords:
    r1 = M - coord[1] - 1
    c1 = coord[0]
    r2 = M - coord[3] 
    c2 = coord[2] - 1
    for i in range(r2, r1+1):
        for j in range(c1, c2+1):
            boxes[i][j] = 0
            
# count 1s
for i in range(M):
    for j in range(N):
        if boxes[i][j] == 1 and not checked[i][j]:
            qu.append([i, j])
            checked[i][j] = True
            count = 0
            
            while qu:
                r, c = qu.popleft()
                count += 1
                for direction in directions:
                    nr = r + direction[0]
                    nc = c + direction[1]
                    if nr >= 0 and nc >= 0 and nr < M and nc < N:
                        if boxes[nr][nc] == 1 and not checked[nr][nc]:
                            qu.append([nr, nc])
                            checked[nr][nc] = True
            count_list.append(count)
            
print(len(count_list))
print(*sorted(count_list))
