from collections import deque

# get input
num_cases = int(input(''))
cases = []
row_col_num_list = []
for case in range(num_cases):
    num_row, num_col, num_cabb = map(int, input('').split(' '))
    row_col_num_list.append([num_row, num_col])
    cases.append([[0] * num_col for i in range(num_row)])
    for _ in range(num_cabb):
        row, col = map(int, input('').split(' '))
        cases[case][row][col] = 1

# cases =         [[[1, 0, 0, 0, 0, 0, 0, 0],
#                   [1, 1, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 1, 0, 0, 0],
#                   [0, 0, 0, 0, 1, 0, 0, 0],
#                   [0, 0, 1, 1, 0, 1, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 1, 1, 1, 0],
#                   [0, 0, 0, 0, 1, 1, 1, 0],
#                   [0, 0, 0, 0, 1, 1, 1, 0]],
#                  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]]
# num_row = 10
# num_col = 8
# num_cases = 2


# initialization

def get_new_looking(now, direction, num_row, num_col):
    new_row = now[0] + direction[0]
    new_col = now[1] + direction[1]
    if new_row >= 0 and new_row < num_row and new_col >= 0 and new_col < num_col:
        return [new_row, new_col]
    else:
        return None
    
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
worm_count_list = []
    
# execution
for i in range(num_cases):
    qu = deque()
    checked = []
    case_now = cases[i]
    num_worms = 0
    num_row = row_col_num_list[i][0]
    num_col = row_col_num_list[i][1]
    
    for row in range(num_row):
        for col in range(num_col):
            if [row, col] not in checked and case_now[row][col] == 1:
                finished = False
                new_cabbage = [row, col]
                qu.append(new_cabbage)
                checked.append(new_cabbage)
                while not finished:
                    # print('qu: ', qu)
                    looking = qu.popleft()
                    # if looking is cabbage, check neighbooring grounds
                    if case_now[looking[0]][looking[1]] == 1:
                        for direction in directions:
                            new_looking = get_new_looking(looking, direction, num_row, num_col)
                            # if new_looking is cabbage, add to qu
                            if new_looking and new_looking not in checked and case_now[new_looking[0]][new_looking[1]] == 1:
                                qu.append(new_looking)
                                checked.append(new_looking)
                    if not qu:
                        finished = True
                    # print('checked: ', checked)
                num_worms += 1
    # print('num_worms: ', num_worms)
    worm_count_list.append(num_worms)
# print('worm_count_list: ', worm_count_list)
for i in range(num_cases):
    print(worm_count_list[i])