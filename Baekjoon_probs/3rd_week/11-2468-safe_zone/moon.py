from collections import deque

# get inputs
N = int(input(''))
area = [[*map(int, input('').split(' '))] for _ in range(N)]
# print(area)


# initialization
max_height = 2
direcs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
cnt_list = []


# # execution
# find highest building
for i in range(N):
    if max(area[i]) > max_height:
        max_height = max(area[i])

# iterate for each rain height
for height in range(0, max_height):
    checked = [[False] * N for _ in range(N)]
    qu = deque()
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not checked[i][j] and area[i][j] > height:
                qu.append([i, j])
                checked[i][j] = True
                
                while qu:
                    r, c = qu.popleft()
                    for direc in direcs:
                        nr = r + direc[0]
                        nc = c + direc[1]
                        if nr >= 0 and nc >= 0 and nr < N and nc < N:
                            if not checked[nr][nc] and area[nr][nc] > height:
                                qu.append([nr, nc])
                                checked[nr][nc] = True
                cnt += 1
    cnt_list.append(cnt)
    
# print("cnt_list: ", cnt_list)
print(max(cnt_list))
                