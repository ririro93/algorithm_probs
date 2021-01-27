# 그림 개수,
# 가장 넓은 그림 구하기

import numpy as np
from collections import deque
import timeit

# 런타임 계산해보기
start = timeit.default_timer()

#################################################################
# BFS
class BFS:
    def __init__(self, data):
        self.data = data
        self.row = 0
        self.col = 0
        self.checked = []
        self.islands = []
        self.counter = 0
        self.qu = deque()
    
    def get_data_val(self, coor):
        [i, j] = coor
        return self.data[i, j]
    
    def put_in_checked(self, data):
        self.checked.append(data)
    
    def put_in_qu(self, data):
        self.qu.append(data)
    
    def pull_from_qu(self):
        return self.qu.popleft()
    
    def put_in_island(self, count):
        self.islands.append(count)

# # initialization
# n, m = map(int, input('').split(' '))

# my_arr = np.zeros((n, m))
# for i in range(n):
#     my_arr[i] = list(map(int, input('').split(' ')))


# # test initialization
n = 200
m = 200
my_arr = np.zeros((n, m))
for i in range(n):
    for j in range(m):
        if np.random.random() > 0.5: temp = 1
        else: temp = 0
        my_arr[i][j] = temp

painting = BFS(my_arr)

# # execution
# [0, 0] 좌표가 checked에 있는지 확인하고 없으면 큐에 추가
for i in range(n):
    for j in range(m):
        if [i, j] not in painting.checked:
            painting.put_in_qu([i, j])

            # 큐가 비어있지 않으면 큐에서 좌표 하나 꺼내서 그 좌표값이랑 val 임시로 저장
            while painting.qu:
                temp_coor = painting.pull_from_qu()
                temp_val = painting.get_data_val(temp_coor)

                # checked 에 좌표 추가
                painting.put_in_checked(temp_coor)

                # 꺼낸 값이 1 이면 카운터 올리고, 인접한 애들 존재하고 checked 에 없으면 큐에 넣기, 큐에 이미 들어있지도 않아야됨
                if temp_val == 1:
                    painting.counter += 1
                    if [temp_coor[0]+1, temp_coor[1]] and [temp_coor[0]+1, temp_coor[1]] not in painting.checked and temp_coor[0]+1 < n and [temp_coor[0]+1, temp_coor[1]] not in painting.qu:
                        painting.put_in_qu([temp_coor[0]+1, temp_coor[1]])
                    if [temp_coor[0], temp_coor[1]+1] and [temp_coor[0], temp_coor[1]+1] not in painting.checked and temp_coor[1]+1 < m and [temp_coor[0], temp_coor[1]+1] not in painting.qu:
                        painting.put_in_qu([temp_coor[0], temp_coor[1]+1])
                    if [temp_coor[0]-1, temp_coor[1]] and [temp_coor[0]-1, temp_coor[1]] not in painting.checked and temp_coor[0]-1 >= 0 and [temp_coor[0]-1, temp_coor[1]] not in painting.qu:
                        painting.put_in_qu([temp_coor[0]-1, temp_coor[1]])
                    if [temp_coor[0], temp_coor[1]-1] and [temp_coor[0], temp_coor[1]-1] not in painting.checked and temp_coor[1]-1 >= 0 and [temp_coor[0], temp_coor[1]-1] not in painting.qu:
                        painting.put_in_qu([temp_coor[0], temp_coor[1]-1])

                # print('checking: ', temp_coor)
                # print(painting.qu)
                # print('counter: ', painting.counter)
                # print('checked: ', painting.checked, '\n')

            # 큐가 비었으면 counter 값을 islands에 append 하고 count값 초기화
            if painting.counter != 0:
                painting.put_in_island(painting.counter)
                painting.counter = 0
# print('islands: ', painting.islands)
print(len(painting.islands))
print(max(painting.islands))

################################################################
stop = timeit.default_timer()

print('Time: ', stop - start)  