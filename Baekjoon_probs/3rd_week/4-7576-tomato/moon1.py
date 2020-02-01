from collections import deque

# inputs -> N: num_row, M: num_col
N, M = map(int, input('').split(' '))
box = [[*map(int, input('').split(' '))] for _ in range(M)]
checked = [[False] * N for _ in range(M)]
qu = deque()
not_first = False

# get_new_box : iterate for one ripe tomato
def get_new_box(box, checked, qu, N, M):
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    
    while qu:
        # print('qu: ', qu)
        # print('checked: ', checked)
        # print('box: ', box, '\n')
        row, col = qu.popleft()
        checked[row][col] = True
        for direction in directions:
            nrow = row + direction[0]
            ncol = col + direction[1]
            if nrow >= 0 and ncol >= 0 and nrow < N and ncol < M:
                if box[nrow][ncol] == 0 and not checked[nrow][ncol]:
                    qu.append([nrow, ncol])
                    checked[nrow][ncol] = True
                    box[nrow][ncol] = box[row][col] + 1
                elif box[nrow][ncol] > 1:
                    if box[row][col] + 1 < box[nrow][ncol]:
                        box[nrow][ncol] = box[row][col] + 1
                        qu.append([nrow, ncol])



for i in range(M):
    for j in range(N):
        if box[i][j] == 1 and not checked[i][j]:
            qu.append([i, j])
            get_new_box(box, checked, qu, M, N)

# print('box: ')
max_time = 0
no_finish = False
for i in range(M):
    # print(box[i])
    if max(*box[i]) > max_time:
        max_time = max(*box[i])
    if 0 in box[i]:
        no_finish = True
if no_finish: print(-1)
else: print(max_time-1)
            
            
        