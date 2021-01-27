from collections import deque

# initialization
N, M = map(int, input('').split(' '))

def split(word):
    return [int(i) for i in word]

maze = [[0] * M for i in range(N)]
for row in range(N):
    maze[row] = list(split(input('')))
    
qu = deque()
qu.append([0, 0])

checked = [[0,0]]

looking = [0, 0]

finished = False

directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

counter = 1
dist = [[0] * M for i in range(N)]

def find_new_looking(looking, direction, N, M):
    row = looking[0]+direction[0]
    col = looking[1]+direction[1]
    if row >= 0 and row < N and col >= 0 and col < M:
        return [row, col]
    else:
        return None
    
# # execution
while not finished:
    # pop qu and check for valid path
    looking = qu.popleft()
    
    # add paths to qu if valid
    for direction in directions:
        # 될돌아가야되는지 체크하고 counter에서도 빼기
        new_looking = find_new_looking(looking, direction, N, M)
        # 도착 못했으면 
        if new_looking and new_looking not in checked and maze[new_looking[0]][new_looking[1]] == 1:
            qu.append(new_looking)
            dist[new_looking[0]][new_looking[1]] = dist[looking[0]][looking[1]] + 1
            checked.append(new_looking)
        # 마지막 지점 도착하면 끝
        if new_looking == [N-1, M-1]:
            finished = True
            
    counter += 1
#     print('counter:' , counter)
#     print('checked: ', checked)
#     print('qu: ', qu, '\n')

# print(counter)       
# print(dist)
print(dist[N-1][M-1] + 1)
