from collections import deque

# get inputs
N = int(input(''))
house = [[*map(int, input(''))] for _ in range(N)]
# print(house)

# initialization
checked = [[False] * N for _ in range(N)]
group = deque()
counter = 0
counter_list = []
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

for i in range(N):
    for j in range(N):
        if house[i][j] == 1 and not checked[i][j]:
            checked[i][j] = True
            group.append([i, j])
            while group:
                # print(group)
                r, c = group.popleft()
                for direction in directions:
                    nr = r + direction[0]
                    nc = c + direction[1]
                    if nr >= 0 and nc >= 0 and nr < N and nc < N:
                        if not checked[nr][nc] and house[nr][nc] == 1:
                            group.append([nr, nc])
                            checked[nr][nc] = True
                            counter += 1
            counter_list.append(counter+1)
            counter = 0
            
print(len(counter_list))
for length in sorted(counter_list):
    print(length)