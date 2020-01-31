from collections import deque
import copy

# get inputs
num_col, num_row = map(int, input('').split(' '))
orig_box = []
for row in range(num_row):
    orig_box.append(list(map(int, input('').split(' '))))

# print(box)

# # example input
# num_col = 6
# num_row = 4

# num_col = 5
# num_row = 5

# num_col = 2
# num_row = 2
# box = [[0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 1]]

# orig_box = [[0, -1, 0, 0, 0, 0],
#        [-1, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 1]]

# orig_box = [[-1, 1, 0, 0, 0],
#            [0, -1, -1, -1, 0],
#            [0, -1, -1, -1, 0],
#            [0, -1, -1, -1, 0],
#            [0, 0, 0, 0, 0]]

# orig_box = [[1, -1],
#             [-1, 1]]

box = copy.deepcopy(orig_box)

# initialization
qu = deque()
looking = [0, 0]
time = [[0] * num_col for i in range(num_row)]
ripe_list = []
max_time = 0
cant_finish = False

def add_next_spaces_to_qu(looking, num_row, num_col, checked, qu, box, time):
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    for direction in directions:
        new_row = looking[0] + direction[0]
        new_col = looking[1] + direction[1]
        if new_row >= 0 and new_row < num_row and new_col >= 0 and new_col < num_col and [new_row, new_col] not in checked and box[new_row][new_col] == 0:
            qu.append([new_row, new_col])
            checked.append([new_row, new_col])
            box[new_row][new_col] = 1
            if time[new_row][new_col] == 0:
                time[new_row][new_col] = time[looking[0]][looking[1]] + 1
            elif time[looking[0]][looking[1]] + 1 < time[new_row][new_col]:
                time[new_row][new_col] = time[looking[0]][looking[1]] + 1
    

# # execution
# add ripe tomato coords to ripe_list
for row in range(num_row):
    for col in range(num_col):
        if box[row][col] == 1:
            ripe_list.append([row, col])
            
for ripe in ripe_list:
    qu.append(ripe)
    checked = []
    box = copy.deepcopy(orig_box)
    # print('orig box: ', orig_box)
    # print('box: ', box)
    while qu:
        # print('qu: ', qu)
        # print('checked: ', checked)
        # print('time: ', time, '\n')
        looking = qu.popleft()
        checked.append(looking)
        add_next_spaces_to_qu(looking, num_row, num_col, checked, qu, box, time)
        # print('box: ', box)
        # print('time: ')

# 원래 익었어서 0 인애들 바꾸기
for ripe in ripe_list:
    time[ripe[0]][ripe[1]] = -1
    
# 원래 빈칸도 다 바꾸기
for row in range(num_row):
    for col in range(num_col):
        if orig_box[row][col] == -1:
            time[row][col] = -1
        
for col in range(len(time)):
    # print(time[col])
    if 0 in time[col]: cant_finish = True
    if max(time[col]) > max_time:
        max_time = max(time[col])

if cant_finish: print(-1)
else: print(max_time)
        
    
            
