from collections import deque
import itertools

# get inputs
N = int(input())
country = [[*map(int, input().split(' '))] for _ in range(N)]
# for i in range(N):
    # print(country[i])

# initialization
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
continent_list = []
checked = [[False]*N for _ in range(N)]
qu = deque()
dist_min = 197

# execution
for i in range(N):
    for j in range(N):
        continent = []
        if country[i][j] == 1 and not checked[i][j]:
            qu.append([i, j])
            checked[i][j] = True
            continent.append([i, j])
            
            while qu:
                r, c = qu.popleft()
                for direction in directions:
                    [nr, nc] = [r+direction[0], c+direction[1]]
                    if nr >= 0 and nc >= 0 and nr < N and nc < N:
                        if country[nr][nc] == 1 and not checked[nr][nc]:
                            qu.append([nr, nc])
                            checked[nr][nc] = True
                            continent.append([nr, nc])
            continent_list.append(continent)
          

        

# print("continent_list[i]: ")
# for i in range(len(continent_list)):
#     print(continent_list[i])

for i in range(len(continent_list)):
    if i == 0:
        looking = list(itertools.chain.from_iterable(continent_list[1:]))
    elif i < len(continent_list) - 1:
        looking = list(itertools.chain.from_iterable(continent_list[0:i]+continent_list[i+1:]))
    else:
        looking = list(itertools.chain.from_iterable(continent_list[:-1]))
    # print("looking: ", looking)
    for j in range(len(continent_list[i])):
        # current x: cx, next x: nx
        cx, cy = continent_list[i][j]
        # print("\n cx, cy: ", cx, cy)
        for look in looking:
            nx, ny = look
            # print("nx, ny: ", nx, ny)
            dist = abs(nx-cx) + abs(ny-cy) -1 
            if dist < dist_min:
                dist_min = dist
print(dist_min)
            
            
            
            
            
            
                
                