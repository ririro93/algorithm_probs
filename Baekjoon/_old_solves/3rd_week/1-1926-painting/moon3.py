# numpy 쓰면 백준 문제 안된대 표준 라이브버리가 아니여서

from collections import deque

# initialization
n, m = map(int, input('').split(' '))

my_arr = [[0]*m for _ in range(n)]
for i in range(n):
    my_arr[i] = list(map(int, input('').split(' ')))


# # test initialization
# n = 6
# m = 5
# my_arr = ([[1, 1, 0, 1, 1],
#            [0, 1, 1, 0, 0],
#            [0, 0, 0, 0, 0],
#            [1, 0, 1, 1, 1],
#            [0, 0, 1, 1, 1],
#            [0, 0, 1, 1, 1]])

# my_arr = np.zeros((n, m))

# for i in range(n):
#     for j in range(m):
#         if np.random.random() > 0.5: temp = 1
#         else: temp = 0
#         my_arr[i][j] = temp

checked = [[False] * m for _ in range(n)]
          

qu = deque()

counter = 0
counter_list = [0]

def check_new(looking, my_arr, checked, n, m):
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    new_directions = []
    for direction in directions:
        new_row = looking[0] + direction[0]
        new_col = looking[1] + direction[1]
        
        if new_row >= 0 and new_col >=0 and new_row < n and new_col < m and not checked[new_row][new_col] and my_arr[new_row][new_col] == 1:
            qu.append([new_row, new_col])
            checked[new_row][new_col] = True
            
                

for i in range(n):
    for j in range(m):
        if my_arr[i][j] == 1 and not checked[i][j]:
            counter = 0
            # print('checked: \n', checked)
            qu.append([i, j])
            checked[i][j] = True
            # print('qu: ', qu)
            while qu:
                looking = qu.popleft()
                check_new(looking, my_arr, checked, n, m)
                counter += 1
            counter_list.append(counter)
# print(counter_list)
print(len(counter_list)-1)
print(max(counter_list))
            
          